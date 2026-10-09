from unittest.mock import Mock

from src import Main


def test_main_prints_student_report(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", Mock(side_effect=("Ali", "85")))

    Main.main()

    output = capsys.readouterr().out
    assert "Name: Ali" in output
    assert "Marks: 85" in output
    assert "Grade: A" in output


def test_main_handles_non_numeric_marks(monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", Mock(side_effect=("Ali", "not a number")))

    Main.main()

    assert "Error: Marks must be a number." in capsys.readouterr().out
