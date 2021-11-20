from AoC2020.day_4 import count_valid_passport_fields


def test_count_valid_passport_fields():
    assert count_valid_passport_fields('./tests/day4.txt') == 2
