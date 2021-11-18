from AoC2020.day_3 import trees_encountered

def main():
    print('Welcome to Day 3 of Advent of Code 2020')
    print('Reading data file and converting...')

    data = []
    with open('./data/day3.txt') as f:
        data = f.read().splitlines()

    count = trees_encountered(data, 3, 1)
    print('Hit %d trees' % count)

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
    count = 1
    for item in slopes:
        x, y = item
        count *= trees_encountered(data, x, y)

    print('Tree Matrix Value %d' % count)
    


if __name__ == '__main__':
    main()
