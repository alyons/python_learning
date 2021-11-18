from AoC2020.day_1 import find_sum_pair, find_sum_triplets


def main():
    print('Welcome to Day 1 of Advent of Code 2020')
    print('Reading data file and converting...')

    data = []
    with open('./data/day1.txt') as f:
        for line in f:
            data.append(int(line))

    pair = find_sum_pair(2020, data)
    print('Found pair %d' % pair)

    triplets = find_sum_triplets(2020, data)
    print('Found triplets %d' % triplets)


if __name__ == '__main__':
    main()
