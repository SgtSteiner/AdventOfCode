"""
Enunciado del problema: https://adventofcode.com/2020/day/4

"""

import os
import re

def check_byr(byr):
    valid = False
    if byr.isnumeric():
        return 1920 <= int(byr) <= 2002
    return valid

def check_iyr(iyr):
    valid = False
    if iyr.isnumeric():
        return 2010 <= int(iyr) <= 2020
    return valid

def check_eyr(eyr):
    valid = False
    if eyr.isnumeric():
        return 2020 <= int(eyr) <= 2030
    return valid

def check_hgt(hgt):
    valid = False
    if re.search("cm$", hgt):
        return 150 <= int(hgt[:-2]) <= 193
    elif re.search("in$", hgt):
        return 59 <= int(hgt[:-2]) <= 76
    return valid

def check_hcl(hcl):
    if re.search(r"\A#[0-9a-f]{6}$", hcl):
        return True
    else:
        return False

def check_ecl(ecl):
    return ecl in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def check_pid(pid):
    if re.search("^\d{9}$", pid):
        return True
    else:
        return False

def check_format(passport):
    result = []
    for field in passport:
        name, value = field.split(":")
        if name == "byr":
            result.append(check_byr(value))
        elif name == "iyr":
            result.append(check_iyr(value))
        elif name == "eyr":
            result.append(check_eyr(value))
        elif name == "hgt":
            result.append(check_hgt(value))
        elif name == "hcl":
            result.append(check_hcl(value))
        elif name == "ecl":
            result.append(check_ecl(value))
        elif name == "pid":
            result.append(check_pid(value))
    return sum(result) == 7

def check_passport(passport, format=False):
    fields = [field[:3] for field in passport]
    valid_fields = set(MANDATORY).issubset(set(fields))
    if format:
        if valid_fields:
            return check_format(passport)
        else:
            return False
    else:
        return valid_fields



MANDATORY = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

# Read datafile
filePath = os.path.relpath('../data/input_day04.txt')
with open(filePath,'r') as f:
     data = f.read().split("\n\n")

passports = [element.replace("\n", " ").split() for element in data]

# --- Part 1 ---
result_count = 0
for passport in (passports):
    if check_passport(passport):
        result_count +=1
    fields = []
    
print(f"Resultado parte 1: {result_count}")

# --- Part 2 ---
result_count = 0
for passport in (passports):
    if check_passport(passport, format=True):
        result_count +=1
    fields = []
    
print(f"Resultado parte 2: {result_count}")