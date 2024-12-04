import pytest
from unittest.mock import patch
from io import StringIO
import sys

from menu import show_menu, select_menu  # Assuming functions are in a module named 'main'


def test_show_menu(capsys):
    show_menu()
    captured = capsys.readouterr()
    assert captured.out == 'Lotto\n---------\nA) Konto Ein- und Auszahlungen tätigen\nB) Lottotipps abgeben\nZ) Beenden\n'


def test_select_menu_valid_option(monkeypatch):
    def mock_input(prompt):
        return 'A'

    monkeypatch.setattr('builtins.input', mock_input)
    result = select_menu()
    assert result == 'A'


def test_select_menu_invalid_option(monkeypatch, capsys):
    # Mock input sequence to return invalid inputs ('X') and then a valid input ('A')
    def mock_input(prompt):
        if prompt == 'Ihre Wahl > ':
            return 'X'  # First invalid input
        return 'A'  # Then valid input

    # Patch the 'input' function using monkeypatch
    monkeypatch.setattr('builtins.input', mock_input)

    # Call select_menu() which will process the inputs
    result = select_menu()

    # Capture the printed output
    captured = capsys.readouterr()

    # Check if the error message for invalid input is printed once
    assert 'Bitte geben Sie eine gültige Wahl ein' in captured.out

    # Check that the function returns the valid selection 'A'
    assert result == 'A'





def test_select_menu_multiple_attempts(monkeypatch):
    def mock_input(prompt):
        responses = ['X', 'Y', 'A']
        return responses.pop(0)

    monkeypatch.setattr('builtins.input', mock_input)
    result = select_menu()
    assert result == 'A'
