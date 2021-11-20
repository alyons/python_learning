from AoC2020.day_4 import count_valid_passport_fields, count_valid_passports

def main():
    print('Welcome to Day 4 of Advent of Code 2020')
    print('Reading data file and converting...')

    count = count_valid_passport_fields('./data/day4.txt')
    print(f'Passports with correct fields: {count}')

    count = count_valid_passports('./data/day4.txt')
    print(f'Valid Passports: {count}')


if __name__ == '__main__':
    main()
