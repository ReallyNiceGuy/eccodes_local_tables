#!/usr/bin/python3

import sys


def get_fields(line):
    return [
        line[0:7].strip(),
        line[8:11].strip(),
        line[12:15].strip(),
        line[15:].strip(), ]


def save(block):
    if (len(block["items"]) != block["count"]):
        print(f"{block['filename']}: Mismatched entries", file=sys.stderr)
        print(block)
    with open(block["filename"], 'w') as f:
        for key, val in block["items"].items():
            print(f"{key} {key} {val}", file=f)


with open(sys.argv[1], encoding="latin1") as f:
    block = {}
    for line in f:
        fields = get_fields(line)
        if fields[0] != '':
            if len(block):
                save(block)
                block = {}
            block["filename"] = f"{int(fields[0])}.table"
            block["count"] = int(fields[1])
            block["items"] = {}
        else:
            if fields[1] != '':
                item = fields[1]
                block["items"][item] = fields[3]
            else:
                block["items"][item] += " " + fields[3]
