from src.operations import add, sub
def test_add():
    assert add(1,5) == 6
    assert add(2,3) == 5
    assert add(1.5,2) == 3.5


def test_sub():
    assert sub(9,5) == 4
    assert sub(9,5.5) == 3.5
    assert sub(9,1) == 8
