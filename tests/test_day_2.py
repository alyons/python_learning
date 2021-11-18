from AoC2020.day_2 import count_valid_passwords, count_valid_passwords_ex, parse_input, valid_password

test_cases = [
    '1-3 a: abcde',
    '1-3 b: cdefg',
    '2-9 c: ccccccccc',
]


def test_valid_password():
    assert valid_password('abcde', 'a', 1, 3) == True
    assert valid_password('cdefg', 'b', 1, 3) == False
    assert valid_password('ccccccccc', 'c', 2, 9) == True


def test_parse_input():
    assert parse_input(test_cases[0]) == { 'minimum': 1, 'maximum': 3, 'key': 'a', 'password': 'abcde' }


def test_count_valid_passwords():
    assert count_valid_passwords(test_cases) == 2


def test_count_valid_passwords_ex():
    assert count_valid_passwords_ex(test_cases) == 1
