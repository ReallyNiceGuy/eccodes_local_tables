#!/usr/bin/python3


# From
# F;XX;YYY;Name;Unit;Scale;Reference;Width
# To
# code|abbreviation|type|name|unit|scale|reference|width|crex_unit|crex_scale|crex_width
# Unit type conversion
# CCITT IA5;string
# CODE TABLE;table
# FLAG TABLE;flag
# if scale > 0;long
# if scale < 0;double

# crex_width
# if type != table and type != flag then crex_width = witdh/8
# else crex_width = ceil(ln(width)/ln(2))

import sys
import csv
import math


def make_type(unit, scale):
    if unit == 'CCITT IA5':
        return 'string'
    if unit == 'CODE TABLE':
        return 'table'
    if unit == 'FLAG TABLE':
        return 'flag'
    if scale <= 0:
        return 'long'
    return 'double'


def crex_width(btype, width, scale):
    if btype == "table" or btype == "flag":
        return int(math.ceil(math.log(width)/math.log(2)))
    return int(math.ceil(width/8))


with open(sys.argv[1], newline='', encoding='latin1') as f:
    tb = csv.reader(f, delimiter=';')
    for line in tb:
        if len(line) == 0:
            continue
        code = f"{line[0]}{line[1]}{line[2]}"
        abbreviation = f"entry{code}"
        name = line[3].strip()
        unit = line[4].upper()
        scale = int(line[5])
        reference = int(line[6])
        width = int(line[7])
        btype = make_type(unit,scale)
        print(f"{code}|{abbreviation}|{btype}|{name}|{unit}|{scale}|{reference}|{width}|{unit}|{scale}|{crex_width(btype, width, scale)}")
