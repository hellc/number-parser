import pytest
import csv
from number_parser import parse, parse_number
from tests import HUNDREDS_DIRECTORY, PERMUTATION_DIRECTORY
from tests import get_test_files

LANG = 'ru'


class TestNumberParser():
    @pytest.mark.parametrize(
        "test_input,expected",
        [
            ("ноль", 0),
            ("один", 1),
            ("два", 2),
            ("три", 3),
            ("четыре", 4),
            ("шесть", 6),
            ("пятнадцать", 15),
            ("двадцать пять", 25),
            ("тридцать", 30),
            ("сорок", 40),
            ("сорок четыре", 44),
            ("девяносто", 90),
            ("сто", 100),
            ("двести", 200),
            ("триста пятьдесят семь", 357),
            ("пятьсот девяносто шесть", 596),
            ("восемьсот девяносто один", 891),
            ("две тысячи", 2_000),
            ("две тысячи двадцать", 2_020),
            ("семь тысяч четыре", 7_004),
            ("двадцать один миллион", 21_000_000),
            ("двадцать один миллион семьдесят три", 21_000_073),

            # Advanced/Formal forms
            ("одного", 1),
            ("одному", 1),
            ("одним", 1),
            ("одном", 1),
            ("двух", 2),
            ("двум", 2),
            ("двумя", 2),
            ("трех", 3),
            ("трем", 3),
            ("тремя", 3),
            ("четырех", 4),
            ("четырем", 4),
            ("четырьмя", 4),
            ("шести", 6),
            ("шестью", 6),
            ("тридцати", 30),
            ("тридцать", 30),
            ("тридцатью", 30),
            ("сорока", 40),
            ("девяноста", 90),
            ("ста", 100),
            ("двухсот", 200),
            ("двумстам", 200),
            ("двумястами", 200),
            ("двухстах", 200),
            ("двести пятьдесят шесть", 256),
            ("двухсот пятидесяти шести", 256),
            ("двумястами пятьюдесятью шестью", 256),
            ("пятьюстами", 500),
            ("пятисот девяноста шести", 596),
            ("пятистам девяноста шести", 596),
            ("пятьсот девяносто шесть", 596),
            ("пятьюстами девяноста шестью", 596),
            ("пятистах девяноста шести", 596),
            ("тысяче", 1_000),
            ("двадцать одним миллионом", 21_000_000),
        ]
    )
    def test_parse_number(self,  expected,  test_input):
        assert parse_number(test_input, LANG) == expected

    def test_parse_number_till_hundred(self):
        for filename in get_test_files(HUNDREDS_DIRECTORY, f'{LANG}_'):
            with open(filename, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    assert parse_number(row['text'], LANG) == int(row['number'])

    def test_parse_number_permutations(self):
        for filename in get_test_files(PERMUTATION_DIRECTORY, f'{LANG}_'):
            with open(filename, "r") as csv_file:
                csv_reader = csv.DictReader(csv_file)
                for row in csv_reader:
                    assert parse_number(row['text'], LANG) == int(row['number'])
