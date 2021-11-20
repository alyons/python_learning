from typing import List
from copy import deepcopy
import re

def parse_passport_data(filePath: str) -> List[str]:
    output = []
    rawData = []
    passport = []

    with open(filePath) as f:
        rawData = f.readlines()

    for item in rawData:
        if (item.isspace()):
            output.append(deepcopy(passport))
            passport.clear()
        else:
            passport += item.strip().split(' ')

    if len(passport) > 0:
        output.append(passport)

    return output


def validate_passport_fields(passport: List[str]) -> bool:
    fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

    for item in fields:
        if not(any(item in field for field in passport)):
            return False

    return True


def validate_birth_year(data: str) -> bool:
    year = int(data.split(':')[1])
    return year >= 1920 and year <= 2002


def validate_issue_year(data: str) -> bool:
    year = int(data.split(':')[1])
    return year >= 2010 and year <= 2020


def validate_expiration_year(data: str) -> bool:
    year = int(data.split(':')[1])
    return year >= 2020 and year <= 2030


def validate_height(data: str) -> bool:
    pattern = re.compile(r'(?P<height>\d+)(?P<unit>cm|in){1}')
    match = pattern.search(data.split(':')[1])

    if match is None:
        return False
    
    height = int(match.group('height'))
    unit = match.group('unit')

    if (unit == 'cm'):
        return height >= 150 and height <= 193
    else:
        return height >= 59 and height <= 76


def validate_hair_color(data: str) -> bool:
    pattern = re.compile(r'#[a-f0-9]{6}')
    return pattern.match(data.split(':')[1])


def validate_eye_color(data: str) -> bool:
    valid_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    color = data.split(':')[1]
    return color in valid_colors


def validate_passport_id(data: str) -> bool:
    pattern = re.compile(r'^[0-9]{9}$')
    return pattern.match(data.split(':')[1])


def validate_passport(passport: List[str]) -> bool:

    if not(validate_passport_fields(passport)):
        return False

    for item in passport:
        if 'byr' in item:
            if not(validate_birth_year(item)):
                return False
        if 'iyr' in item:
            if not(validate_issue_year(item)):
                return False
        if 'eyr' in item:
            if not(validate_expiration_year(item)):
                return False
        if 'hgt' in item:
            if not(validate_height(item)):
                return False
        if 'hcl' in item:
            if not(validate_hair_color(item)):
                return False
        if 'ecl' in item:
            if not(validate_eye_color(item)):
                return False
        if 'pid' in item:
            if not(validate_passport_id(item)):
                return False

    return True


def count_valid_passport_fields(filePath: str) -> int:
    count = 0
    passports = parse_passport_data(filePath)
    for item in passports:
        if (validate_passport_fields(item)):
            count += 1
    
    return count
    

def count_valid_passports(filePath: str) -> int:
    count = 0
    passports = parse_passport_data(filePath)
    for item in passports:
        if (validate_passport(item)):
            count += 1
    
    return count
