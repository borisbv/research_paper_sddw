"""Algoritmo de ranking ponderado para selección de top 5 tecnologías."""

from pathlib import Path

import pandas as pd


class RankingEngine:
    """Calcula ranking ponderado y selecciona las mejores tecnologías."""

    WEIGHTS = {
        "usabilidad": 0.40,
        "robustez": 0.30,
        "operabilidad": 0.30,
    }

    def compute_scores(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calcula puntuación global ponderada por tecnología."""
        df = df.copy()
        df["puntuacion_global"] = (
            df["usabilidad_score"] * self.WEIGHTS["usabilidad"]
            + df["robustez_score"] * self.WEIGHTS["robustez"]
            + df["operabilidad_score"] * self.WEIGHTS["operabilidad"]
        )
        df["puntuacion_global"] = df["puntuacion_global"].round(2)
        return df

    def get_top_n(self, df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
        """Retorna las top N tecnologías ordenadas por puntuación."""
        sorted_df = df.sort_values("puntuacion_global", ascending=False)

        # Aplicar desempate si es necesario
        sorted_df = self._apply_tiebreaker(sorted_df)

        return sorted_df.head(n).reset_index(drop=True)

    def _apply_tiebreaker(self, df: pd.DataFrame) -> pd.DataFrame:
        """Desempata por: cobertura de discapacidades > gratuidad > disponibilidad API."""
        df = df.copy()

        # Cobertura de discapacidades: contar cuántos tipos atiende
        def count_disabilities(val):
            if pd.isna(val):
                return 0
            return len([d.strip() for d in str(val).split(",") if d.strip()])

        df["_n_discapacidades"] = df["tipo_discapacidad"].apply(count_disabilities)

        # Gratuidad: 1 si tiene opción gratuita
        def is_free(val):
            return 1 if str(val).strip().upper() == "X" else 0

        if "gratuita" in df.columns:
            df["_gratuita"] = df["gratuita"].apply(is_free)
        else:
            df["_gratuita"] = 0

        # Disponibilidad API: 1 si tiene opción para desarrolladores
        def has_api(val):
            val_str = str(val).strip().lower()
            return 1 if val_str.startswith("sí") or val_str.startswith("si") else 0

        if "opcion_desarrolladores" in df.columns:
            df["_api"] = df["opcion_desarrolladores"].apply(has_api)
        else:
            df["_api"] = 0

        # Ordenar con criterios de desempate
        df = df.sort_values(
            ["puntuacion_global", "_n_discapacidades", "_gratuita", "_api"],
            ascending=[False, False, False, False],
        )

        # Limpiar columnas auxiliares
        df = df.drop(columns=["_n_discapacidades", "_gratuita", "_api"])

        return df

    def export_ranking(self, df: pd.DataFrame, output_dir: str) -> None:
        """Exporta ranking_global.csv con puntuaciones por dimensión."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        sorted_df = self._apply_tiebreaker(df)
        export_cols = [
            "indice", "nombre", "tipo_producto", "tipo_ia", "tipo_discapacidad",
            "usabilidad_score", "robustez_score", "operabilidad_score",
            "puntuacion_global",
        ]
        available = [c for c in export_cols if c in sorted_df.columns]
        sorted_df[available].to_csv(out / "ranking_global.csv", index=False)
