import os
import pytest
from scripts.validate_structure import validate_structure
from scripts.validate_citations import validate_citations
from scripts.validate_figure_sync import validate_figures

def test_validate_structure_fail_missing_dir(tmp_path):
    os.chdir(tmp_path)
    os.makedirs("paper")
    # No subdirs created
    with pytest.raises(SystemExit):
        validate_structure("paper")

def test_validate_citations_success(tmp_path):
    os.chdir(tmp_path)
    os.makedirs("paper/sections")
    os.makedirs("paper/references")
    
    # Mock BibTeX
    with open("paper/references/references.bib", "w") as f:
        f.write("@article{test_key, title={Test Paper}}")
        
    # Mock Section with citation
    with open("paper/sections/01-intro.md", "w") as f:
        f.write("According to \\cite{test_key}, this works.")
        
    # Should not exit (success)
    validate_citations("paper")

def test_validate_citations_fail_missing_key(tmp_path):
    os.chdir(tmp_path)
    os.makedirs("paper/sections")
    os.makedirs("paper/references")
    
    with open("paper/references/references.bib", "w") as f:
        f.write("@article{real_key, title={Real}}")
        
    with open("paper/sections/01-intro.md", "w") as f:
        f.write("According to \\cite{fake_key}, this fails.")
        
    with pytest.raises(SystemExit):
        validate_citations("paper")
