import pandas as pd
import numpy as np

#filename = input("EEG data file name:")
#filename += ".csv"
#
#timefile = input("Time data file name:")
#timefile += ".txt"

name = input("Enter folder name: ")
b = input("Lie or truth: ")

filename = name + "/" + b + "/" + b + ".csv"
timefile = name + "/" + b + "/" + "times.txt"


tf = pd.read_csv(filename)
f = open(timefile, "r")

times = f.readlines()
timepairs = []
for time in times:
    time = tuple(float(i) for i in time.split(','))
    timepairs.append(time)

i = 1

for (start, end) in timepairs:
    startH = int(round(start * 256))
    endH = int(round(end * 256))
    tf.iloc[startH:endH].to_csv(name + "/" + b + "/" + name + "_" + b + str(i) + ".csv", index = False)
    print("Exporting question " + str(i) + "...")
    i += 1

print("Export complete!")




