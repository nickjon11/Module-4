import pytest

from app.operations.add import add
from app.operations.subtract import subtract
from app.operations.multiply import multiply
from app.operations.divide import divide

@pytest.mark.parametrize(
    "a,b,result",
    [
        (5, 5, 10),
        (2,  3, 5),
        (-1, 1, 0)
    ]
)
def test_add(a,b,result):
    assert add(a,b) == result
@pytest.mark.parametrize(
    "a,b,result",
    [
        (10,5,5),
        (5,2,3)
    ]
)
def test_subtract(a,b,result):
    assert subtract(a,b) == result
@pytest.mark.parametrize(
    "a,b,result",
    [
        (2,3,6),
        (5,5,25)
    ]
)
def test_multiply(a,b,result):
    assert multiply(a,b) == result
@pytest.mark.parametrize(
    "a,b,result",
    [
        (10,2,5),
        (20,4,5)
    ]
)
def test_divide(a,b,result):
    assert divide(a,b) == result
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(5,0)
