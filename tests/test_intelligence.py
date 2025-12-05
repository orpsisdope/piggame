import src.intelligence as intel_mod
from src.intelligence import Intelligence




def test_level_is_stored():
    ai = Intelligence("medium")
    assert ai.level == "medium"