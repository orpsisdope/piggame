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


def test_medium_mode_uses_random_threshold(monkeypatch):
    monkeypatch.setattr(intel_mod.random, "randint", lambda a, b: 18)
    ai = Intelligence("medium")
    assert ai.should_hold(17) is False
    assert ai.should_hold(18) is True


def test_hard_mode_uses_random_threshold(monkeypatch):
    monkeypatch.setattr(intel_mod.random, "randint", lambda a, b: 24)
    ai = Intelligence("hard")
    assert ai.should_hold(23) is False
    assert ai.should_hold(24) is True


def test_bananas_mode_uses_random_threshold(monkeypatch):
    monkeypatch.setattr(intel_mod.random, "randint", lambda a, b: 30)
    ai = Intelligence("bananas")
    assert ai.should_hold(29) is False
    assert ai.should_hold(30) is True