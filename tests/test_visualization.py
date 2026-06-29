"""Tests para el pipeline de visualización académica."""

import json
import sys
from pathlib import Path

import pandas as pd
import pytest

sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from process_dataset import DataProcessor
from ranking_engine import RankingEngine


@pytest.fixture
def processor():
    csv_path = Path(__file__).parent.parent / "temp_context" / \
        "AI-accesibilidad W3C 2 (Base de datos).xlsx - Tecnologías.csv"
    return DataProcessor(str(csv_path))


@pytest.fixture
def df_num(processor):
    df = processor.load_csv()
    return processor.map_categorical_to_numeric(df)


@pytest.fixture
def scored(df_num):
    engine = RankingEngine()
    return engine.compute_scores(df_num)


@pytest.fixture
def top5(scored):
    engine = RankingEngine()
    return engine.get_top_n(scored, n=5)


@pytest.fixture
def matrix(processor):
    df = processor.load_csv()
    return processor.generate_disability_matrix(df)


@pytest.fixture
def stats(processor, df_num):
    return processor.compute_descriptive_stats(df_num)


@pytest.fixture
def viz():
    from visualization_pipeline import VisualizationPipeline
    return VisualizationPipeline()


class TestPlotDisabilityDistribution:
    """Tarea 2.1: Figura de distribución por tipo de discapacidad."""

    def test_creates_png_file(self, viz, matrix, tmp_path):
        path = viz.plot_disability_distribution(matrix, tmp_path)
        assert path.exists()
        assert path.suffix == ".png"

    def test_filename_matches_convention(self, viz, matrix, tmp_path):
        path = viz.plot_disability_distribution(matrix, tmp_path)
        assert path.name == "fig-distribucion-discapacidad.png"

    def test_file_is_not_empty(self, viz, matrix, tmp_path):
        path = viz.plot_disability_distribution(matrix, tmp_path)
        assert path.stat().st_size > 0


class TestPlotDimensionComparison:
    """Tarea 2.2: Figura comparativa de puntuaciones por dimensión."""

    def test_creates_png_file(self, viz, stats, tmp_path):
        path = viz.plot_dimension_comparison(stats, tmp_path)
        assert path.exists()
        assert path.suffix == ".png"

    def test_filename_matches_convention(self, viz, stats, tmp_path):
        path = viz.plot_dimension_comparison(stats, tmp_path)
        assert path.name == "fig-comparativa-dimensiones.png"

    def test_file_is_not_empty(self, viz, stats, tmp_path):
        path = viz.plot_dimension_comparison(stats, tmp_path)
        assert path.stat().st_size > 0


class TestPlotTop5Ranking:
    """Tarea 2.3: Figura de ranking top 5."""

    def test_creates_png_file(self, viz, top5, tmp_path):
        path = viz.plot_top5_ranking(top5, tmp_path)
        assert path.exists()
        assert path.suffix == ".png"

    def test_filename_matches_convention(self, viz, top5, tmp_path):
        path = viz.plot_top5_ranking(top5, tmp_path)
        assert path.name == "fig-ranking-top5.png"

    def test_file_is_not_empty(self, viz, top5, tmp_path):
        path = viz.plot_top5_ranking(top5, tmp_path)
        assert path.stat().st_size > 0


class TestExportTableDisabilityMatrix:
    """Tarea 2.4a: Tabla Markdown de matriz tecnología × discapacidad."""

    def test_creates_markdown_file(self, viz, matrix, tmp_path):
        path = viz.export_table_disability_matrix(matrix, tmp_path)
        assert path.exists()
        assert path.suffix == ".md"

    def test_contains_markdown_table_syntax(self, viz, matrix, tmp_path):
        path = viz.export_table_disability_matrix(matrix, tmp_path)
        content = path.read_text(encoding="utf-8")
        assert "|" in content
        assert "---" in content

    def test_contains_all_disability_types(self, viz, matrix, tmp_path):
        path = viz.export_table_disability_matrix(matrix, tmp_path)
        content = path.read_text(encoding="utf-8")
        for dt in ["Visual", "Motora", "Cognitiva", "Auditiva"]:
            assert dt in content

    def test_contains_technology_names(self, viz, matrix, tmp_path):
        path = viz.export_table_disability_matrix(matrix, tmp_path)
        content = path.read_text(encoding="utf-8")
        assert "Chat GPT" in content
        assert "JAWS" in content


class TestExportTableTop5Comparison:
    """Tarea 2.4b: Tabla comparativa top 5 vs promedios generales."""

    def test_creates_markdown_file(self, viz, top5, stats, tmp_path):
        path = viz.export_table_top5_comparison(top5, stats, tmp_path)
        assert path.exists()
        assert path.suffix == ".md"

    def test_contains_markdown_table_syntax(self, viz, top5, stats, tmp_path):
        path = viz.export_table_top5_comparison(top5, stats, tmp_path)
        content = path.read_text(encoding="utf-8")
        assert "|" in content
        assert "---" in content

    def test_contains_dimension_headers(self, viz, top5, stats, tmp_path):
        path = viz.export_table_top5_comparison(top5, stats, tmp_path)
        content = path.read_text(encoding="utf-8")
        for dim in ["Usabilidad", "Robustez", "Operabilidad"]:
            assert dim in content

    def test_contains_promedio_general(self, viz, top5, stats, tmp_path):
        path = viz.export_table_top5_comparison(top5, stats, tmp_path)
        content = path.read_text(encoding="utf-8")
        assert "Promedio general" in content

    def test_contains_top5_names(self, viz, top5, stats, tmp_path):
        path = viz.export_table_top5_comparison(top5, stats, tmp_path)
        content = path.read_text(encoding="utf-8")
        for name in top5["nombre"].tolist():
            assert name in content
