import pytest
from AoC2020.day_1 import find_sum_pair, find_sum_triplets

test_input = [1721, 979, 366, 299, 675, 1456]


def test_find_sum_pair():
    assert find_sum_pair(2020, test_input) == 514579


def test_find_sum_triplets():
    assert find_sum_triplets(2020, test_input) == 241861950
