import json
import  pandas as pd
from scipy.stats import skew,kurtosis
from sklearn.cluster import KMeans
import numpy as np
from sklearn import preprocessing


class data_gongwei():

    def __init__(self):
        pass

    def read_data(self):
        url = "D:/2018.4.27/data7m.txt"
        skew_list = []
        kurt_list = []
        with open(url) as f:
            data = f.readline()
            while data:
                data_json_process = []
                data_json = json.loads(data)
                for i in data_json['data'][1:len(data_json['data'])-1].split(','):
                    data_json_process.append(float(i))
                skew_list.append(skew(data_json_process))
                kurt_list.append(kurtosis(data_json_process))
                data = f.readline()

        return skew_list,kurt_list


    def kmeans_cluster(self):
        skew_list,kurt_list = data_gongwei().read_data()
        # print(max(skew_list))
        # print(min(skew_list))
        # print(max(kurt_list))
        # print(min(kurt_list))

        skew_list = [[i] for  i in list(preprocessing.scale(np.array(skew_list)))]
        kurt_list = [[i] for  i in list(preprocessing.scale(np.array(kurt_list)))]


        clf1 = KMeans(n_clusters=2, random_state=0).fit(skew_list)
        clf2 = KMeans(n_clusters=2, random_state=0).fit(kurt_list)
        # s = clf.fit_transform(np.array(skew_list).reshape(1,-1))
        return clf1.labels_,clf2.labels_

skew_label, kurt_label = data_gongwei().kmeans_cluster()

print(skew_label)
print(kurt_label)