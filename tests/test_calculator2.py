from unittest.mock import patch
from app.calculator import calculator


def test_exit_command():
    with patch("builtins.input", side_effect=["exit"]):
        calculator.main()


def test_help_command():
    with patch("builtins.input", side_effect=["help", "exit"]):
        calculator.main()


def test_history_empty():
    calculator.history.clear()

    with patch("builtins.input", side_effect=["history", "exit"]):
        calculator.main()


def test_addition_flow():
    calculator.history.clear()

    with patch("builtins.input", side_effect=["+", "5", "5", "exit"]):
        calculator.main()

    assert "5.0 + 5.0 = 10.0" in calculator.history


def test_subtraction_flow():
    calculator.history.clear()

    with patch("builtins.input", side_effect=["-", "10", "3", "exit"]):
        calculator.main()

    assert "10.0 - 3.0 = 7.0" in calculator.history


def test_multiplication_flow():
    calculator.history.clear()

    with patch("builtins.input", side_effect=["*", "4", "5", "exit"]):
        calculator.main()

    assert "4.0 * 5.0 = 20.0" in calculator.history


def test_division_flow():
    calculator.history.clear()

    with patch("builtins.input", side_effect=["/", "10", "2", "exit"]):
        calculator.main()

    assert "10.0 / 2.0 = 5.0" in calculator.history


def test_value_error_flow():
    calculator.history.clear()

    with patch("builtins.input", side_effect=["+", "abc", "exit"]):
        calculator.main()

    assert calculator.history == []


def test_zero_division_flow():
    calculator.history.clear()

    with patch("builtins.input", side_effect=["/", "10", "0", "exit"]):
        calculator.main()

    assert all("10.0 / 0.0" not in item for item in calculator.history)

def test_force_full_main_execution():
    calculator.history.clear()

    with patch(
        "builtins.input",
        side_effect=[
            "+", "1", "1",
            "-", "2", "1",
            "*", "2", "2",
            "/", "4", "2",
            "help",
            "history",
            "unknown",
            "1", "1",
            "exit"
        ]
    ):
        calculator.main()

def test_final_main_path():
    calculator.history.clear()

    with patch(
        "builtins.input",
        side_effect=[
            "+", "1", "1",
            "history",
            "exit"
        ]
    ):
        calculator.main()

def test_invalid_command_flow():
    calculator.history.clear()

    with patch(
        "builtins.input",
        side_effect=[
            "unknown",
            "0",
            "0",
            "history",
            "exit"
        ]
    ):
        calculator.main()

    assert calculator.history == []