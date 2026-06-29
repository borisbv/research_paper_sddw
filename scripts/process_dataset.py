"""Procesamiento del dataset de 41 tecnologías IA para accesibilidad web WCAG 2.2."""

import json
from pathlib import Path

import numpy as np
import pandas as pd


class DataProcessor:
    """Transforma el CSV categórico de tecnologías en datos numéricos analizables."""

    # Mapeo categórico → numérico según design.md
    PRECISION_MAP = {"Baja": 1, "Media": 3, "Alta": 5}
    TIEMPO_RESPUESTA_MAP = {"Lento": 1, "Moderado": 3, "Rápido": 5}
    NAV_TECLADO_MAP = {"No compatible": 0, "No": 0, "Parcial": 3, "Total": 5}
    COMANDOS_VOZ_MAP = {"No": 0, "Parcial": 3, "Sí": 5, "Si": 5}

    # Filas de encabezado a saltar en el CSV
    HEADER_ROWS_TO_SKIP = 3

    def __init__(self, csv_path: str):
        self.csv_path = csv_path

    def load_csv(self) -> pd.DataFrame:
        """Lee el CSV y retorna dataframe limpio con las 41 tecnologías."""
        df_raw = pd.read_csv(self.csv_path, header=None, encoding="utf-8")

        # Saltar filas de encabezado (las primeras filas son metadatos)
        # Los datos comienzan donde la columna 0 tiene un número de índice
        data_rows = []
        for idx, row in df_raw.iterrows():
            raw_val = row.iloc[0]
            try:
                num = int(float(raw_val))
                if 1 <= num <= 99:
                    data_rows.append(row)
            except (ValueError, TypeError):
                continue

        df = pd.DataFrame(data_rows).reset_index(drop=True)

        # Asignar nombres de columna
        col_names = [
            "indice", "nombre", "descripcion", "url",
            "pago", "gratuita", "costo", "opcion_desarrolladores",
            "fortalezas", "oportunidades", "debilidades",
            "version", "ultima_actualizacion",
            "categoria", "referencias_bib",
            "tipo_producto", "tipo_ia", "tipo_discapacidad",
            "precision", "sensibilidad", "tiempo_respuesta",
            "multidispositivo", "multi_navegador", "multi_os",
            "config_previa", "nav_teclado", "comandos_voz"
        ]

        # Ajustar si hay más o menos columnas
        if len(df.columns) >= len(col_names):
            df = df.iloc[:, :len(col_names)]
            df.columns = col_names
        else:
            df.columns = col_names[:len(df.columns)]

        # Limpiar espacios en columnas de texto
        for col in df.columns:
            if df[col].dtype == object:
                df[col] = df[col].astype(str).str.strip()

        df["indice"] = pd.to_numeric(df["indice"], errors="coerce").astype(int)

        return df

    def map_categorical_to_numeric(self, df: pd.DataFrame) -> pd.DataFrame:
        """Aplica mapeo categórico → numérico según tabla de conversión del design."""
        df = df.copy()

        # Limpiar valores antes del mapeo
        def clean_val(s):
            return str(s).strip().rstrip(" ").split(" ")[0] if pd.notna(s) else s

        # Precisión y Sensibilidad usan el mismo mapeo
        for col in ["precision", "sensibilidad"]:
            df[f"{col}_clean"] = df[col].apply(clean_val)
            # Manejar valores especiales como "Alta en ampliación y lectura"
            df[f"{col}_clean"] = df[f"{col}_clean"].apply(
                lambda x: "Alta" if str(x).startswith("Alta") else x
            )
            df[f"{col}_num"] = df[f"{col}_clean"].map(self.PRECISION_MAP)

        # Tiempo de respuesta
        df["tiempo_respuesta_clean"] = df["tiempo_respuesta"].apply(clean_val)
        df["tiempo_respuesta_clean"] = df["tiempo_respuesta_clean"].apply(
            lambda x: "Rápido" if str(x).lower().startswith("r") else x
        )
        df["tiempo_respuesta_num"] = df["tiempo_respuesta_clean"].map(self.TIEMPO_RESPUESTA_MAP)

        # Navegación por teclado
        df["nav_teclado_clean"] = df["nav_teclado"].apply(clean_val)
        df["nav_teclado_num"] = df["nav_teclado_clean"].map(self.NAV_TECLADO_MAP)

        # Comandos de voz
        df["comandos_voz_clean"] = df["comandos_voz"].apply(clean_val)
        df["comandos_voz_clean"] = df["comandos_voz_clean"].apply(
            lambda x: "Sí" if str(x).lower().startswith("s") else x
        )
        df["comandos_voz_num"] = df["comandos_voz_clean"].map(self.COMANDOS_VOZ_MAP)

        # Robustez: evaluar multidispositivo, multi-navegador, multi-OS
        # Multidispositivo: contar cuántas plataformas soporta (escala 1-5)
        def score_multidispositivo(val):
            val = str(val).strip().lower()
            if val in ("todas", "all"):
                return 5
            platforms = [p.strip() for p in val.replace(",", " ").split() if p.strip()]
            platforms = [p for p in platforms if p not in ("n/a", "nan", "no", "aplica")]
            if not platforms or val in ("no aplica", "no", "n/a", "nan"):
                return 1
            count = len(platforms)
            if count >= 3:
                return 5
            elif count == 2:
                return 3
            return 1

        def score_multi_navegador(val):
            val = str(val).strip().lower()
            if val in ("todos", "all"):
                return 5
            if val in ("n/a", "nan", "no aplica", "no"):
                return 1
            browsers = [b.strip() for b in val.replace(",", " ").split() if b.strip()]
            browsers = [b for b in browsers if b not in ("n/a", "nan")]
            count = len(browsers)
            if count >= 3:
                return 5
            elif count == 2:
                return 3
            return 1

        def score_multi_os(val):
            val = str(val).strip().lower()
            if val in ("todos", "all"):
                return 5
            if val in ("n/a", "nan", "no aplica", "no", "no compatible"):
                return 1
            if "parcial" in val:
                return 3
            oses = [o.strip() for o in val.replace(",", " ").split() if o.strip()]
            oses = [o for o in oses if o not in ("n/a", "nan")]
            count = len(oses)
            if count >= 3:
                return 5
            elif count == 2:
                return 3
            return 1

        df["multidispositivo_num"] = df["multidispositivo"].apply(score_multidispositivo)
        df["multi_navegador_num"] = df["multi_navegador"].apply(score_multi_navegador)
        df["multi_os_num"] = df["multi_os"].apply(score_multi_os)

        # Calcular dimensiones agregadas
        df["usabilidad_score"] = df[["precision_num", "sensibilidad_num", "tiempo_respuesta_num"]].mean(axis=1)
        df["robustez_score"] = df[["multidispositivo_num", "multi_navegador_num", "multi_os_num"]].mean(axis=1)
        df["operabilidad_score"] = df[["nav_teclado_num", "comandos_voz_num"]].mean(axis=1)

        return df

    def compute_descriptive_stats(self, df_num: pd.DataFrame) -> dict:
        """Calcula media, mediana, SD por dimensión."""
        stats = {}
        for dim in ["usabilidad", "robustez", "operabilidad"]:
            col = f"{dim}_score"
            stats[dim] = {
                "media": round(float(df_num[col].mean()), 2),
                "mediana": round(float(df_num[col].median()), 2),
                "desviacion_estandar": round(float(df_num[col].std()), 2),
            }
        return stats

    def generate_disability_matrix(self, df: pd.DataFrame) -> pd.DataFrame:
        """Genera matriz cruzada tecnología × tipo de discapacidad."""
        disability_types = ["Visual", "Motora", "Cognitiva", "Auditiva"]
        matrix_data = []

        for _, row in df.iterrows():
            disc_str = str(row.get("tipo_discapacidad", ""))
            disabilities = [d.strip() for d in disc_str.split(",")]
            entry = {"nombre": row["nombre"]}
            for dt in disability_types:
                entry[dt] = 1 if any(dt.lower() in d.lower() for d in disabilities) else 0
            matrix_data.append(entry)

        matrix = pd.DataFrame(matrix_data)
        matrix = matrix.set_index("nombre")
        return matrix

    def export_all(self, df_num: pd.DataFrame, stats: dict,
                   matrix: pd.DataFrame, output_dir: str) -> None:
        """Exporta todos los archivos procesados."""
        out = Path(output_dir)
        out.mkdir(parents=True, exist_ok=True)

        # Exportar dataset procesado
        export_cols = [
            "indice", "nombre", "tipo_producto", "tipo_ia", "tipo_discapacidad",
            "precision", "precision_num", "sensibilidad", "sensibilidad_num",
            "tiempo_respuesta", "tiempo_respuesta_num",
            "multidispositivo_num", "multi_navegador_num", "multi_os_num",
            "nav_teclado", "nav_teclado_num", "comandos_voz", "comandos_voz_num",
            "usabilidad_score", "robustez_score", "operabilidad_score",
        ]
        available_cols = [c for c in export_cols if c in df_num.columns]
        df_num[available_cols].to_csv(out / "tecnologias_procesadas.csv", index=False)

        # Exportar matriz de discapacidad
        matrix.to_csv(out / "matriz_discapacidad.csv")

        # Exportar estadísticas descriptivas
        with open(out / "estadisticas_descriptivas.json", "w", encoding="utf-8") as f:
            json.dump(stats, f, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    csv_path = Path(__file__).parent.parent / "temp_context" / \
        "AI-accesibilidad W3C 2 (Base de datos).xlsx - Tecnologías.csv"
    output_dir = Path(__file__).parent.parent / "paper" / "data"

    proc = DataProcessor(str(csv_path))
    df = proc.load_csv()
    print(f"Tecnologías cargadas: {len(df)}")

    df_num = proc.map_categorical_to_numeric(df)
    stats = proc.compute_descriptive_stats(df_num)
    matrix = proc.generate_disability_matrix(df)

    proc.export_all(df_num, stats, matrix, str(output_dir))
    print(f"Archivos exportados a {output_dir}")
    print(f"Estadísticas: {json.dumps(stats, indent=2, ensure_ascii=False)}")
