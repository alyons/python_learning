from AoC2020.day_2 import count_valid_passwords, count_valid_passwords_ex


def main():
    print('Welcome to Day 2 of Advent of Code 2020')
    print('Reading data file and converting...')

    data = []
    with open('./data/day2.txt') as f:
        for line in f:
            data.append(line)

    count = count_valid_passwords(data)
    print('Found %d valid passwords' % count)

    count = count_valid_passwords_ex(data)
    print('Found %d valid passwords ex' % count)


if __name__ == '__main__':
    main()
