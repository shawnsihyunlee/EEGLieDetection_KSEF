# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 12:40:43 2018

@author: Shawn
"""
import pandas as pd

filename = input("Enter filename without extension: ")

filename += ".txt"

alist = []
blist = []

f = open(filename, "r")
lines = f.readlines()

for i in range(len(lines)):
    if lines[i][0] == 'A':
        line = lines[i+1]
        for num in line.split(","):
            if '\n' in num:
                num = num[:-1]
            alist.append(int(num))
        
    if lines[i][0] == 'B':
        line = lines[i+1]
        for num in line.split(","):
            if '\n' in num:
                num = num[:-1]
            blist.append(int(num))
f.close()

zipped = list(zip(alist, blist))

data = pd.DataFrame(zipped, columns = ['A', 'B'])

data.to_csv(filename[:-4] + '.csv', index = False)

print("Successfully converted!")