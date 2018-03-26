import pandas as pd
import os
import  numpy as np
import random
import matplotlib.pyplot as plt
import json
from pandas.plotting import autocorrelation_plot
from statsmodels.sandbox.stats.diagnostic import  acorr_ljungbox



plt.rcParams['font.sans-serif']=['SimHei']

def sequence_chart():
    url = "C:/Users/l.c\Desktop/tasks/graduation projection/midterm/data/data/train_trace_2.txt"
    data = []
    data_1 = []
    with open(url) as f:
        line = f.readline()
        i = 0
        while i < 1000:
            data = json.loads(line)['data']
            data = data[1:len(data)-1]
            data_1.append(float(data.split(',')[0]))
            line = f.readline()
            i += 1

    fig,ax = plt.subplots()
    x = range(0,1000)
    y =data_1
    plt.plot(x,y)
    plt.legend()
    plt.show()
    return data_1

def autocorr():
    data_1 = sequence_chart()
    autocorrelation_plot(data_1)
    plt.show()


def boxpierce_test():
    # fig,ax = plt.subplots(2,2)
    data_1 = sequence_chart()


    qljungbox, pval, qboxpierce, pvalbp = acorr_ljungbox(data_1, boxpierce=True)
    print(len(pval))
    # for i in range(len(pval)):
    #     print("true data:",qljungbox[i], pval[i], qboxpierce[i], pvalbp[i])

    plt.plot(range(0, len(qljungbox)), qljungbox)
    plt.plot(range(0, len(qboxpierce)), qboxpierce)

    plt.legend()



    # ax[0, 0].plot(range(0,len(pval)), qljungbox, label = "ql")
    # ax[0, 0].plot(range(0,len(pval)), qboxpierce, label = "qb")
    #
    # ax[0,1].plot(range(0,len(pval)), label="pval",)
    # ax[0,1].plot(range(0,len(pvalbp)), label="pvalbp")
    #
    # ax[0,0].legend()
    # ax[0,1].legend()
    plt.show()


def pval_test():
    data_1 = sequence_chart()

    qljungbox, pval, qboxpierce, pvalbp = acorr_ljungbox(data_1, boxpierce=True)
    plt.plot(range(0, len(pval)), pval)
    plt.plot(range(0, len(pvalbp)), pvalbp)
    plt.legend()
    plt.show()

boxpierce_test()
pval_test()