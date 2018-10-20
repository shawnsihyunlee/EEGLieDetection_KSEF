import numpy as np
import pandas as pd
import os
import random

def readData(filepath):
    X = []
    y = []
    truthpath = filepath + "/truth"
    liepath = filepath + "/lie"
    
    print(truthpath)
    
    filelist = os.listdir(truthpath)
    try:
        for csvpath in filelist:
            xt = []
            csvpath = truthpath + "/" + csvpath
            csv = pd.read_csv(csvpath)
            for index, row in csv.iterrows():
                xt.append([int(row['A']), int(row['B'])])
            X.append(xt)
            y.append(1)
            print("appended " + csvpath)
    except:
        print("No truth directory!")

    try:
        filelist = os.listdir(liepath)
        for csvpath in filelist:
            xt = []
            csvpath = liepath + "/" + csvpath
            csv = pd.read_csv(csvpath)
            for index, row in csv.iterrows():
                xt.append([int(row['A']), int(row['B'])])
            X.append(xt)
            y.append(0)
            print("appended " + csvpath)

    except:
        print("No lie directory!")

    X = np.array(X)
    y = np.array(y)
    return X, y

def readDataShuffled(filepath):
    X = []
    y = []
    path = filepath + "/total"
    
    print(path)
    
    filelist = os.listdir(path)
    random.shuffle(filelist)
    
    try:
        for csvpath in filelist:
            xt = []
            csvpath = path + "/" + csvpath
            csv = pd.read_csv(csvpath)
            for index, row in csv.iterrows():
                xt.append([int(row['A']), int(row['B'])])
            X.append(xt)
            if("lie" in csvpath):
                y.append(0)
            else:
                y.append(1)
            print("appended " + csvpath)
    except:
        print("No truth directory!")

    X = np.array(X)
    y = np.array(y)
    return X, y

