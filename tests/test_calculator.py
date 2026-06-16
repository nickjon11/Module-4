import pytest

from app.calculation.calculation import CalculationProgram

def test_program_add():
    calc = CalculationProgram.create("+", 5, 5)
    assert calc.get_result() == 10
def test_program_sub():
    calc = CalculationProgram.create("-", 10, 5)
    assert calc.get_result() == 5
def test_program_multply():
    calc = CalculationProgram.create("*", 4, 5)
    assert calc.get_result() == 20
def test_program_divide():
    calc = CalculationProgram.create("/", 20, 4)
    assert calc.get_result() == 5
def test_program_divide_by_zero():
    calc = CalculationProgram.create("/", 5, 0)
    with pytest.raises(ZeroDivisionError):
        calc.get_result()
def test_program_invalid():
    calc = CalculationProgram.create("%", 5, 5)
    with pytest.raises(ValueError):
        calc.get_result()