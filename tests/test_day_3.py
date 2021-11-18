from AoC2020.day_3 import trees_encountered


test_case = ''


with open('./tests/day3.txt') as f:
    test_case = f.read().splitlines()


def test_trees_encountered():
    assert trees_encountered(test_case, 3, 1) == 7
