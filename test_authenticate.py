import unittest
from authenticate import login, load_people


class TestIntegration(unittest.TestCase):

    def test_load_people_integration(self):
        people = load_people()
        assert len(people) == 3
        assert people[0].givenname == "Inga"
        assert people[1].password == "secrät"
        assert people[2].balance == 23.00

    def test_login_valid(self, monkeypatch):
        monkeypatch.setattr('builtins.input', lambda _: 'geheim')

        person = login()
        assert person is not None
        assert person.givenname == "Inga"

    def test_login_invalid(self):
        try:
            login()
        except StopIteration:
            assert True
        else:
            assert False


if __name__ == '__main__':
    unittest.main()
