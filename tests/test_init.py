import os
import shutil
import pytest
from scripts.research_init import init_research

def test_init_paper(tmp_path):
    # Change current directory to temp path
    os.chdir(tmp_path)

    init_research("paper")

    # Assert folders exist
    assert os.path.exists("paper/sections")
    assert os.path.exists("paper/references")
    assert os.path.exists("paper/figures")
    assert os.path.exists("paper/data")
    assert os.path.exists("paper/scripts")

    # Assert core files exist
    assert os.path.exists("paper/metadata.yaml")
    assert os.path.exists("paper/_quarto.yml")
    assert os.path.exists("paper/outline.md")

def test_init_book(tmp_path):
    os.chdir(tmp_path)
    init_research("book")
    assert os.path.exists("book/sections")
    assert os.path.exists("book/metadata.yaml")

def test_init_invalid_type(tmp_path):
    os.chdir(tmp_path)
    with pytest.raises(SystemExit):
        init_research("magazine")