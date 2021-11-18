from typing import List


def trees_encountered(map: List[str], mX: int, mY: int) -> int:
    count = 0
    x = 0
    y = 0
    width = len(map[y])

    while y < len(map):
        if (map[y][x] == '#'):
            count += 1

        x += mX
        if (x >= width):
            x -= width

        y += mY

    return count
