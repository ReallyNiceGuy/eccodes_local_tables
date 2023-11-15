#!/usr/bin/python3
import csv
import sys
import os
import shutil


basepath = sys.argv[2]
outpath = sys.argv[3]
with open(sys.argv[1]) as reference:
    refcsv = csv.reader(reference, delimiter='|')
    for items in refcsv:
        key = f"{int(items[0])}.table"
        if os.path.isfile(os.path.join(basepath, key)):
            os.makedirs(outpath, exist_ok=True)
            shutil.copyfile(os.path.join(basepath, key), os.path.join(outpath, key))
