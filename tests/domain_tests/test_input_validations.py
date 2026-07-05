import pytest
from domain import input_validations

class TestIsEmpty:

    @pytest.mark.parametrize(
        "area, expected",
        [
            ("Geografia", "Geografia"),
            ("Python 3", "Python 3"),
            ("Ciência", "Ciência"),
        ],
    )
    def test_valid_is_empty(self, area, expected):
        result = input_validations.is_empty(area)

        assert result == expected

    @pytest.mark.parametrize(
        "area, expected",
        [
            ("                         ", None),
            ("\t", None),
            ("\n", None)
        ]
    )

    def test_invalid_is_empty(self, area, expected):
        result = input_validations.is_empty(area)

        assert result == expected

class TestCheckNumber:

    @pytest.mark.parametrize(
        "area, expected",
        [
            ("Python 3", "Python 3"),
            ("Ciência", "Ciência"),
            ("História", "História")
        ]
    )

    def test_valid_check_number(self, area, expected):
        result = input_validations.check_number(area)

        assert result == expected

    @pytest.mark.parametrize(
        "area, expected",
        [
            ("147966", None),
            ("123456", None),
            ("789456412312345677962623898547741238", None)
        ]
    )

    def test_invalid_check_number(self, area, expected):
        result = input_validations.check_number(area)

        assert result == expected

    @pytest.mark.parametrize(
        "area, expected",
        [
            ("123 456", None),
            ('①②③', None),
            ('٠١٢٣', None)
        ]
    )

    def test_edge_cases_check_number(self, area, expected):
        result = input_validations.check_number(area)

        assert result == expected


class TestCheckLength:
    @pytest.mark.parametrize(
        "area, expected",
        [
            ("Ciencia", "Ciencia"),
            ("   ", "   "),
            ("123456", "123456")
        ]
    )

    def test_valid_length(self, area, expected):
        result = input_validations.check_length(area)

        assert result == expected

    @pytest.mark.parametrize(
        "area, expected",
        [
            ("pqwoeuegiohubjkajopwefisvnofvifdjdjdopefvifdjdnsjdopefwiovdjfisjisdfsdjifjsdifjisodjfisd", None),
            ("a", None)
        ]
    )

    def test_invalid_length(self, area, expected):
        result = input_validations.check_length(area)

        assert result == expected