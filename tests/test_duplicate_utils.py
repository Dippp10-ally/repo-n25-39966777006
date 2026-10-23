from src.duplicate_utils import unique


def test_unique_removes_duplicates():
    assert unique([1, 2, 1, 3]) == [1, 2, 3]


def test_unique_keeps_order():
    assert unique(["b", "a", "b"]) == ["b", "a"]
