#!/usr/bin/python3

import csv
import sys

with open(sys.argv[1], encoding="latin1") as f:
    tabled = csv.reader(f,delimiter=';')
    seq = {}
    for line in tabled:
        items = list(map(str.strip,line))
        if len(items) == 0:
            continue
        if line[0].startswith('#'):
            continue
        if (items[0] == ''):
            seq[seqid].append(f"{int(items[3])}{int(items[4]):02d}{int(items[5]):03d}")
        else:
            seqid = f"{int(items[0])}{int(items[1]):02d}{int(items[2]):03d}"
            if seqid in seq:
                raise RuntimeError(f"{seqid} already exists")
            seq[seqid] = [f"{int(items[3])}{int(items[4]):02d}{int(items[5]):03d}"]

for seqid, items in seq.items():
    print(f'"{seqid}" = [ {", ".join(items)} ]')
