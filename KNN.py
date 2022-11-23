import os
import re
import csv
import pickle

import numpy as np
import pandas as pd


storedData = pd.read_pickle('C:\\FERI\\PISZ\\addedIntervalsData.pickle')


class knn:
    def __init__(self, num_of_neighbours, method):
        self.k = num_of_neighbours
        self.distanceMethod = method

    def fit(self, data):
        self.learning_data = data

    def predict(self, test_data):
        self.k = ''

def cross_validation(classifier):
    data = pd.read_csv('C:\\FERI\\PISZ\\archive\\IRIS.csv')
    df = pd.DataFrame(data)
    split = np.array_split(df, 10)
    print(type(split))



def task3():
    while True:
        try:
            number = int(input("Number of neighbours: "))
            if number < 1:
                raise ValueError

            break
        except ValueError:
            print('Please enter a valid integer, greater than 0')
            print('')
            continue

    print('1 - Euclidean')
    print('2 - Manhattan')
    while True:
        try:
            method = int(input('Enter the number of preferred method: '))
            if method < 1 or method > 2:
                raise ValueError
            break
        except ValueError:
            print('Please enter the number 1 or 2')
            print('')
            continue

    classifier = knn(number, method)
    cross_validation(classifier)





task3()