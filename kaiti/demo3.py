import numpy as np
from sklearn.ensemble import IsolationForest
import json
from sklearn.cluster import KMeans
from numpy import mean,var,std,ptp,median
import matplotlib.pyplot as plt


class demo3():

    def __init__(self):
        pass

    def data_process(self):
        url = 'C:/Users/l.c/Desktop/科研/毕设/开题/工程文件/trace.txt'
        l = []
        with open(url,'rb') as f:
            line = f.readline()
            i = 0
            while i < 400:
                if line:
                    data = json.loads(line)
                    # temp = data['data'].split(']')[0][1:len(data['data'].split(']')[0])]
                    temp = data['data'].split(']')[0].split(',')[1:1000]
                    temp2 = [float(x) for x in temp]
                    temp_list = [round(std(temp2),2), round(ptp(temp2),2)]
                    l.append(temp_list)
                    i = i+1
                    line = f.readline()
        t1 = [[3.55,150.00],[3.53,152.00],[3.51,153.00],[3.45,150.00],[3.44,152.00],[3.32,153.00],
                 [3.60, 153.43],[3.07,150.00],[3.05,153.00],[3.33,158.00],[3.66,156.00],[3.54,153.00]]
        for i in t1:
            l.append(i)
        return l

    def draw_cluster(self):
        l = demo3().data_process()
        num_samples = len(l)
        print(l)
        clf = KMeans(n_clusters=2)
        s = clf.fit(l)
        centroids = clf.labels_
        mark = ['or', 'ob', 'og', 'ok', '^r', '+r', 'sr', 'dr', '<r', 'pr']
        print(centroids)
        for i in range(num_samples):
            plt.plot(l[i][0],l[i][1],mark[clf.labels_[i]])
        mark = ['Dr', 'Db', 'Dg', 'Dk', '^b', '+b', 'sb', 'db', '<b', 'pb']
        centroids = clf.cluster_centers_
        for i in range(2):
            plt.plot(centroids[i][0], centroids[i][1], mark[i], markersize=12)
            # print centroids[i, 0], centroids[i, 1]
        plt.show()





    def demo3_test(self):
        url = 'C:/Users/l.c/Desktop/machine learning/machinelearninginaction/Ch10/testSet.txt'
        file = open(url)
        data = []
        i = 0
        while i < 20:
            for line in file.readlines():
                lineArr = line.strip().split(' ')
                data.append([float(lineArr[0]), float(lineArr[1])])
                i = i +1
        return data



# data = demo3().demo3_test()
# print(data)
demo3().draw_cluster()