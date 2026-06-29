"""Tests para el algoritmo de ranking y selección top 5."""

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
def engine():
    return RankingEngine()


class TestWeights:
    def test_weights_sum_to_one(self, engine):
        total = sum(engine.WEIGHTS.values())
        assert abs(total - 1.0) < 1e-9, f"Los pesos suman {total}, no 1.0"

    def test_has_three_dimensions(self, engine):
        assert len(engine.WEIGHTS) == 3
        for dim in ["usabilidad", "robustez", "operabilidad"]:
            assert dim in engine.WEIGHTS


class TestComputeScores:
    def test_adds_score_column(self, engine, df_num):
        result = engine.compute_scores(df_num)
        assert "puntuacion_global" in result.columns

    def test_scores_are_positive(self, engine, df_num):
        result = engine.compute_scores(df_num)
        assert (result["puntuacion_global"] >= 0).all()

    def test_all_41_technologies_scored(self, engine, df_num):
        result = engine.compute_scores(df_num)
        assert len(result) == 41


class TestTopN:
    def test_returns_5_technologies(self, engine, df_num):
        scored = engine.compute_scores(df_num)
        top5 = engine.get_top_n(scored, n=5)
        assert len(top5) == 5

    def test_top5_sorted_descending(self, engine, df_num):
        scored = engine.compute_scores(df_num)
        top5 = engine.get_top_n(scored, n=5)
        scores = top5["puntuacion_global"].tolist()
        assert scores == sorted(scores, reverse=True)

    def test_top5_has_required_fields(self, engine, df_num):
        scored = engine.compute_scores(df_num)
        top5 = engine.get_top_n(scored, n=5)
        for col in ["nombre", "puntuacion_global", "usabilidad_score", "robustez_score", "operabilidad_score"]:
            assert col in top5.columns


class TestExportRanking:
    def test_export_creates_csv(self, engine, df_num, tmp_path):
        scored = engine.compute_scores(df_num)
        engine.export_ranking(scored, str(tmp_path))
        assert (tmp_path / "ranking_global.csv").exists()

    def test_export_csv_has_41_rows(self, engine, df_num, tmp_path):
        scored = engine.compute_scores(df_num)
        engine.export_ranking(scored, str(tmp_path))
        exported = pd.read_csv(tmp_path / "ranking_global.csv")
        assert len(exported) == 41
