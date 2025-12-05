import src.intelligence as intel_mod
from src.intelligence import Intelligence




def test_level_is_stored():
    ai = Intelligence("medium")
    assert ai.level == "medium"


def test_easy_mode_uses_random_threshold(monkeypatch):
    monkeypatch.setattr(intel_mod.random, "randint", lambda a, b: 12)
    ai = Intelligence("easy")
    assert ai.should_hold(11) is False
    assert ai.should_hold(12) is True