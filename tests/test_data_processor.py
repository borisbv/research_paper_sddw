"""Tests para el procesamiento del dataset de tecnologías IA-accesibilidad."""

import json
import sys
from pathlib import Path

import pandas as pd
import pytest

# Agregar scripts/ al path
sys.path.insert(0, str(Path(__file__).parent.parent / "scripts"))

from process_dataset import DataProcessor


@pytest.fixture
def processor():
    csv_path = Path(__file__).parent.parent / "temp_context" / "AI-accesibilidad W3C 2 (Base de datos).xlsx - Tecnologías.csv"
    return DataProcessor(str(csv_path))


class TestLoadCSV:
    def test_loads_41_technologies(self, processor):
        df = processor.load_csv()
        assert len(df) == 41, f"Se esperaban 41 tecnologías, se obtuvieron {len(df)}"

    def test_has_required_columns(self, processor):
        df = processor.load_csv()
        required = ["nombre", "tipo_producto", "tipo_ia", "tipo_discapacidad",
                     "precision", "sensibilidad", "tiempo_respuesta",
                     "multidispositivo", "multi_navegador", "multi_os",
                     "nav_teclado", "comandos_voz"]
        for col in required:
            assert col in df.columns, f"Falta columna: {col}"

    def test_no_null_names(self, processor):
        df = processor.load_csv()
        assert df["nombre"].notna().all(), "Hay nombres nulos"


class TestCategoricalMapping:
    def test_precision_mapping(self, processor):
        df = processor.load_csv()
        df_num = processor.map_categorical_to_numeric(df)
        valid_values = {1, 3, 5}
        actual = set(df_num["precision_num"].dropna().unique())
        assert actual.issubset(valid_values), f"Valores inesperados en precisión: {actual - valid_values}"

    def test_nav_teclado_mapping(self, processor):
        df = processor.load_csv()
        df_num = processor.map_categorical_to_numeric(df)
        valid_values = {0, 3, 5}
        actual = set(df_num["nav_teclado_num"].dropna().unique())
        assert actual.issubset(valid_values), f"Valores inesperados en nav_teclado: {actual - valid_values}"

    def test_comandos_voz_mapping(self, processor):
        df = processor.load_csv()
        df_num = processor.map_categorical_to_numeric(df)
        valid_values = {0, 3, 5}
        actual = set(df_num["comandos_voz_num"].dropna().unique())
        assert actual.issubset(valid_values), f"Valores inesperados en comandos_voz: {actual - valid_values}"


class TestDescriptiveStats:
    def test_stats_structure(self, processor):
        df = processor.load_csv()
        df_num = processor.map_categorical_to_numeric(df)
        stats = processor.compute_descriptive_stats(df_num)
        for dim in ["usabilidad", "robustez", "operabilidad"]:
            assert dim in stats, f"Falta dimensión: {dim}"
            for metric in ["media", "mediana", "desviacion_estandar"]:
                assert metric in stats[dim], f"Falta métrica {metric} en {dim}"

    def test_stats_values_are_numeric(self, processor):
        df = processor.load_csv()
        df_num = processor.map_categorical_to_numeric(df)
        stats = processor.compute_descriptive_stats(df_num)
        for dim in stats:
            for metric in stats[dim]:
                assert isinstance(stats[dim][metric], (int, float)), \
                    f"{dim}.{metric} no es numérico"


class TestDisabilityMatrix:
    def test_matrix_has_4_disability_types(self, processor):
        df = processor.load_csv()
        matrix = processor.generate_disability_matrix(df)
        expected = {"Visual", "Motora", "Cognitiva", "Auditiva"}
        assert expected.issubset(set(matrix.columns)), \
            f"Faltan tipos de discapacidad: {expected - set(matrix.columns)}"

    def test_matrix_has_technologies(self, processor):
        df = processor.load_csv()
        matrix = processor.generate_disability_matrix(df)
        assert len(matrix) > 0, "Matriz vacía"


class TestExport:
    def test_export_creates_files(self, processor, tmp_path):
        df = processor.load_csv()
        df_num = processor.map_categorical_to_numeric(df)
        stats = processor.compute_descriptive_stats(df_num)
        matrix = processor.generate_disability_matrix(df)
        processor.export_all(df_num, stats, matrix, str(tmp_path))

        assert (tmp_path / "tecnologias_procesadas.csv").exists()
        assert (tmp_path / "matriz_discapacidad.csv").exists()
        assert (tmp_path / "estadisticas_descriptivas.json").exists()

    def test_exported_json_is_valid(self, processor, tmp_path):
        df = processor.load_csv()
        df_num = processor.map_categorical_to_numeric(df)
        stats = processor.compute_descriptive_stats(df_num)
        matrix = processor.generate_disability_matrix(df)
        processor.export_all(df_num, stats, matrix, str(tmp_path))

        with open(tmp_path / "estadisticas_descriptivas.json") as f:
            data = json.load(f)
        assert "usabilidad" in data
