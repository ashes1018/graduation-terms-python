import json
import datetime
import numpy as np
import matplotlib.pyplot as plt
import time
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential
from numpy import arange, sin, pi, random

np.random.seed(1234)
sequence_length = 100


class detect_lstm():
    def __init__(self,url):
        self.url = url


    def process_data(self):
        f = open(self.url)
        line = f.readline()
        count = 0
        temp = []
        while line:
            line = json.loads(line)['data']
            line = line[1:len(line) - 1]
            temp.append(float(line.split(',')[565]))
            line = f.readline()
        return temp

    def z_norm(self, data):
        data_mean = data.mean()
        data_std = data.std()
        data -= data_mean
        data /=  data_std
        return data_std,data_mean

    def split_data(self,train_start, train_end, test_start, test_end):
        data = detect_lstm().process_data()
        print("length of data:",len(data))

        print("create training data...")
        res = []
        for i in range(train_start, train_end - sequence_length):
            res.append(data)

