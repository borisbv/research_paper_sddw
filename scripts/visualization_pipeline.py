"""Pipeline de visualización académica para el paper IA-accesibilidad WCAG 2.2."""

from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


class VisualizationPipeline:
    """Genera figuras académicas de alta calidad (300 DPI) y tablas Markdown."""

    DPI = 300
    STYLE = "seaborn-v0_8-whitegrid"
    COLORS = ["#2c7bb6", "#d7191c", "#fdae61", "#abd9e9"]

    def _setup_style(self):
        plt.style.use(self.STYLE)
        plt.rcParams.update({
            "font.size": 11,
            "axes.titlesize": 13,
            "axes.labelsize": 12,
            "figure.dpi": self.DPI,
        })

    # --- Figuras ---

    def plot_disability_distribution(self, matrix: pd.DataFrame,
                                     output_dir: Path) -> Path:
        """Genera gráfico de barras: tecnologías por tipo de discapacidad.

        Args:
            matrix: DataFrame con columnas Visual, Motora, Cognitiva, Auditiva
                    e índice = nombre de tecnología.
            output_dir: Directorio de salida.

        Returns:
            Path al archivo PNG generado.
        """
        self._setup_style()
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        counts = matrix.sum().sort_values(ascending=False)

        fig, ax = plt.subplots(figsize=(8, 5))
        bars = ax.bar(counts.index, counts.values, color=self.COLORS[:len(counts)],
                      edgecolor="black", linewidth=0.5)

        for bar, val in zip(bars, counts.values):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
                    str(int(val)), ha="center", va="bottom", fontweight="bold")

        ax.set_xlabel("Tipo de discapacidad")
        ax.set_ylabel("Número de tecnologías")
        ax.set_title("Distribución de tecnologías por tipo de discapacidad atendida")
        ax.set_ylim(0, counts.max() + 2)

        fig.tight_layout()
        path = output_dir / "fig-distribucion-discapacidad.png"
        fig.savefig(path, dpi=self.DPI, bbox_inches="tight")
        plt.close(fig)
        return path

    def plot_dimension_comparison(self, stats: dict,
                                  output_dir: Path) -> Path:
        """Genera gráfico comparativo de puntuaciones medias por dimensión.

        Args:
            stats: Dict con claves usabilidad, robustez, operabilidad,
                   cada una con media, mediana, desviacion_estandar.
            output_dir: Directorio de salida.

        Returns:
            Path al archivo PNG generado.
        """
        self._setup_style()
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        dims = ["Usabilidad", "Robustez", "Operabilidad"]
        keys = ["usabilidad", "robustez", "operabilidad"]
        means = [stats[k]["media"] for k in keys]
        stds = [stats[k]["desviacion_estandar"] for k in keys]

        fig, ax = plt.subplots(figsize=(7, 5))
        x = np.arange(len(dims))
        bars = ax.bar(x, means, yerr=stds, capsize=5,
                      color=self.COLORS[:3], edgecolor="black", linewidth=0.5)

        for bar, m in zip(bars, means):
            ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.15,
                    f"{m:.2f}", ha="center", va="bottom", fontweight="bold")

        ax.set_xticks(x)
        ax.set_xticklabels(dims)
        ax.set_ylabel("Puntuación media (escala 0-5)")
        ax.set_title("Comparativa de puntuaciones por dimensión evaluada")
        ax.set_ylim(0, 5.5)

        fig.tight_layout()
        path = output_dir / "fig-comparativa-dimensiones.png"
        fig.savefig(path, dpi=self.DPI, bbox_inches="tight")
        plt.close(fig)
        return path

    def plot_top5_ranking(self, top5: pd.DataFrame,
                          output_dir: Path) -> Path:
        """Genera gráfico de barras horizontales con desglose por dimensión.

        Args:
            top5: DataFrame con las 5 mejores tecnologías, con columnas
                  nombre, usabilidad_score, robustez_score, operabilidad_score.
            output_dir: Directorio de salida.

        Returns:
            Path al archivo PNG generado.
        """
        self._setup_style()
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        top5_sorted = top5.sort_values("puntuacion_global", ascending=True)
        names = top5_sorted["nombre"].tolist()
        y = np.arange(len(names))

        usab = top5_sorted["usabilidad_score"].values * 0.40
        rob = top5_sorted["robustez_score"].values * 0.30
        oper = top5_sorted["operabilidad_score"].values * 0.30

        fig, ax = plt.subplots(figsize=(9, 5))
        ax.barh(y, usab, label="Usabilidad (40%)", color=self.COLORS[0],
                edgecolor="black", linewidth=0.5)
        ax.barh(y, rob, left=usab, label="Robustez (30%)", color=self.COLORS[1],
                edgecolor="black", linewidth=0.5)
        ax.barh(y, oper, left=usab + rob, label="Operabilidad (30%)",
                color=self.COLORS[2], edgecolor="black", linewidth=0.5)

        for i, total in enumerate(top5_sorted["puntuacion_global"].values):
            ax.text(total + 0.05, i, f"{total:.2f}", va="center", fontweight="bold")

        ax.set_yticks(y)
        ax.set_yticklabels(names)
        ax.set_xlabel("Puntuación global ponderada")
        ax.set_title("Ranking de las 5 mejores tecnologías de IA para accesibilidad web")
        ax.legend(loc="upper left", fontsize=9, bbox_to_anchor=(0.0, -0.12), ncol=3)
        ax.set_xlim(0, 5.5)

        fig.tight_layout()
        path = output_dir / "fig-ranking-top5.png"
        fig.savefig(path, dpi=self.DPI, bbox_inches="tight")
        plt.close(fig)
        return path

    # --- Tablas Markdown ---

    def export_table_disability_matrix(self, matrix: pd.DataFrame,
                                        output_dir: Path) -> Path:
        """Exporta matriz tecnología × discapacidad como tabla Markdown.

        Args:
            matrix: DataFrame con columnas Visual, Motora, Cognitiva, Auditiva.
            output_dir: Directorio de salida.

        Returns:
            Path al archivo .md generado.
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        lines = []
        lines.append("| Tecnología | Visual | Motora | Cognitiva | Auditiva |")
        lines.append("|---|:---:|:---:|:---:|:---:|")

        for name, row in matrix.iterrows():
            cells = [
                "✓" if row.get(dt, 0) == 1 else ""
                for dt in ["Visual", "Motora", "Cognitiva", "Auditiva"]
            ]
            lines.append(f"| {name} | {' | '.join(cells)} |")

        path = output_dir / "tabla-matriz-discapacidad.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        return path

    def export_table_top5_comparison(self, top5: pd.DataFrame, stats: dict,
                                      output_dir: Path) -> Path:
        """Exporta tabla comparativa top 5 vs promedios generales.

        Args:
            top5: DataFrame con las 5 mejores tecnologías.
            stats: Dict con estadísticas descriptivas por dimensión.
            output_dir: Directorio de salida.

        Returns:
            Path al archivo .md generado.
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        lines = []
        lines.append("| Tecnología | Usabilidad | Robustez | Operabilidad | Global |")
        lines.append("|---|:---:|:---:|:---:|:---:|")

        for _, row in top5.iterrows():
            lines.append(
                f"| {row['nombre']} "
                f"| {row['usabilidad_score']:.2f} "
                f"| {row['robustez_score']:.2f} "
                f"| {row['operabilidad_score']:.2f} "
                f"| {row['puntuacion_global']:.2f} |"
            )

        lines.append(
            f"| **Promedio general** "
            f"| {stats['usabilidad']['media']:.2f} "
            f"| {stats['robustez']['media']:.2f} "
            f"| {stats['operabilidad']['media']:.2f} "
            f"| — |"
        )

        path = output_dir / "tabla-comparativa-top5.md"
        path.write_text("\n".join(lines), encoding="utf-8")
        return path


if __name__ == "__main__":
    import json
    from process_dataset import DataProcessor
    from ranking_engine import RankingEngine

    base = Path(__file__).parent.parent
    csv_path = base / "temp_context" / \
        "AI-accesibilidad W3C 2 (Base de datos).xlsx - Tecnologías.csv"
    figures_dir = base / "figures"
    data_dir = base / "paper" / "data"

    proc = DataProcessor(str(csv_path))
    df = proc.load_csv()
    df_num = proc.map_categorical_to_numeric(df)
    stats = proc.compute_descriptive_stats(df_num)
    matrix = proc.generate_disability_matrix(df)

    engine = RankingEngine()
    scored = engine.compute_scores(df_num)
    top5 = engine.get_top_n(scored, n=5)

    viz = VisualizationPipeline()

    p1 = viz.plot_disability_distribution(matrix, figures_dir)
    print(f"Figura generada: {p1}")

    p2 = viz.plot_dimension_comparison(stats, figures_dir)
    print(f"Figura generada: {p2}")

    p3 = viz.plot_top5_ranking(top5, figures_dir)
    print(f"Figura generada: {p3}")

    t1 = viz.export_table_disability_matrix(matrix, data_dir)
    print(f"Tabla generada: {t1}")

    t2 = viz.export_table_top5_comparison(top5, stats, data_dir)
    print(f"Tabla generada: {t2}")
