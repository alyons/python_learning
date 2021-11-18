from typing import List
import re


def parse_input(input: str) -> dict:
    pattern = re.compile(r'(?P<minimum>\d+)-(?P<maximum>\d+) (?P<key>\w{1}): (?P<password>\w+)')
    matches = pattern.search(input)
    dict = matches.groupdict()
    dict['minimum'] = int(dict['minimum'])
    dict['maximum'] = int(dict['maximum'])
    return dict


def valid_password(password: str, character: str, min: int, max: int) -> bool:
    count = password.count(character)

    return count >= min and count <= max

def valid_password_ex(password: str, character: str, first: int, second: int) -> bool:
    return (password[first - 1] == character) ^ (password[second - 1] == character)


def count_valid_passwords(input: 'List[str]') -> int:
    count = 0
    
    for item in input:
        values = parse_input(item)
        if (valid_password(values['password'], values['key'], values['minimum'], values['maximum'])):
            count += 1

    return count

def count_valid_passwords_ex(input: 'List[str]') -> int:
    count = 0
    
    for item in input:
        values = parse_input(item)
        if (valid_password_ex(values['password'], values['key'], values['minimum'], values['maximum'])):
            count += 1

    return count


