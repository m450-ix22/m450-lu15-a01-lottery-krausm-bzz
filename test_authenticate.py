import pytest
from unittest.mock import patch
from authenticate import login, load_people


@pytest.fixture
def mock_functions(monkeypatch):
    def dummy_input(prompt):
        return 'secrät'

    monkeypatch.setattr('builtins.input', dummy_input)


def test_correct_login(mock_functions):
    with patch('builtins.input', side_effect=['secrät']):
        person = login()
        assert person.givenname == 'Peter'


def test_incorrect_login(mock_functions):
    with patch('builtins.input', side_effect=['wrong', 'secrät']):
        person = login()
        assert person.givenname == 'Peter'


def test_multiple_users_login(mock_functions):
    with patch('builtins.input', side_effect=['geheim']):
        person = login()
        assert person.givenname == 'Inga'

    with patch('builtins.input', side_effect=['passWORT']):
        person = login()
        assert person.givenname == 'Beatrice'


def test_load_people(mock_functions):
    people_list = load_people()
    assert len(people_list) == 3
    assert people_list[0].givenname == 'Inga'
    assert people_list[1].givenname == 'Peter'
    assert people_list[2].givenname == 'Beatrice'

    assert people_list[0].password == 'geheim'
    assert people_list[1].password == 'secrät'
    assert people_list[2].password == 'passWORT'
    assert people_list[0].balance == 14.00
    assert people_list[1].balance == 7.00
    assert people_list[2].balance == 23.00


def test_multiple_incorrect_passwords(mock_functions):
    with patch('builtins.input', side_effect=['wrong1', 'wrong2', 'secrät']):
        person = login()
        assert person.givenname == 'Peter'
