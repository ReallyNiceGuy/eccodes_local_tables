#!/usr/bin/python3
import csv
import sys

trans = {}
with open(sys.argv[1]) as reference:
    with open(sys.argv[2]) as base:
        refcsv = csv.reader(reference, delimiter='|')
        for items in refcsv:
            trans[items[0]]=items[1]
        basecsv = csv.reader(base, delimiter='|')
        for items in basecsv:
            if items[0] in trans:
                items[1] = trans[items[0]]
                print('|'.join(items))
