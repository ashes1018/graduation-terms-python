import  json
import numpy as np
class data_test():

    def __init__(self):
        pass

    def read_data(self):
        url = "E:/es_data_test/test/0.txt"
        i = 0

        with open(url) as f:
            line = f.readlines()
            print(len(line))



data_test().read_data()