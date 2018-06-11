from  scipy.stats import skew,kurtosis,pearsonr
import json
import numpy as np
from sklearn import svm

from sklearn import  preprocessing
from sklearn.metrics import precision_score,recall_score,f1_score


import sys
sys.path.append("C:/yulan/python workspace/graduate_terms/zhongqi/data_gongwei_kmeans.py")
from zhongqi.data_gongwei_kmeans import data_gongwei






class data_gongwei_supervised():

    def __init__(self):
        pass

    def set_labels(self):
        url1 = "D:/2018.4.27/data10000.txt"
        url2 = "D:/2018.4.27/data8000.txt"
        train_trace_skew = []

        train_warning_skew = []

        train_trace_kurt = []
        train_warning_kurt = []

        for line in open(url1):
            train_trace_process = []
            line = json.loads(line)['data']
            line = line[1:len(line)-1]
            for i in line.split(','):
                train_trace_process.append(float(i))
            train_trace_skew.append(skew(train_trace_process))
            train_trace_kurt.append(kurtosis(train_trace_process))
        # train_trace_skew = train_trace_skew[:9400]
        # train_trace_skew_valid = train_trace_skew[9400:]



        for line in open(url2):
            train_warning_process = []
            line = json.loads(line)['data']
            line = line[1:len(line)-1]
            for i in line.split(','):
                train_warning_process.append(float(i))
            train_warning_skew.append(skew(train_warning_process))
            train_warning_kurt.append(kurtosis(train_warning_process))
        # train_warning_skew = train_warning_skew[:7500]
        # train_warning_skew_valid = train_warning_skew[7500:]


        train_trace_skew = list(preprocessing.scale(np.array(train_trace_skew)))
        train_warning_skew = list(preprocessing.scale(np.array(train_warning_skew)))
        train_trace_kurt = list(preprocessing.scale(np.array(train_trace_kurt)))
        train_warning_kurt = list(preprocessing.scale(np.array(train_warning_kurt)))

        # train_trace_skew_valid = list(preprocessing.scale(np.array(train_trace_skew_valid)))
        # train_warning_skew_valid = list(preprocessing.scale(np.array(train_warning_skew_valid)))

        return train_trace_skew,train_warning_skew,train_trace_kurt, train_warning_kurt


    def fit_predict(self):
        train_trace_skew, train_warning_skew, train_trace_kurt,train_warning_kurt = data_gongwei_supervised().set_labels()
        train_skew_dataset = train_trace_skew + train_warning_skew
        train_skew_dataset = [[i] for  i in train_skew_dataset]
        label = list(np.append(np.zeros(10000, dtype=np.int),np.ones(8000, dtype=np.int)))
        label = [[i] for  i in label]
        clf1 = svm.SVC()
        clf2 = svm.SVC()
        skew_test, kurt_test = data_gongwei().read_data()
        skew_test = preprocessing.scale(np.array(skew_test))
        kurt_test = preprocessing.scale(np.array(kurt_test))

        skew_test = [[i] for i in skew_test]
        kurt_test = [[i] for i in kurt_test]

        train_kurt_dataset = train_trace_kurt + train_warning_kurt
        train_kurt_dataset = [[i] for i in train_kurt_dataset]


        clf1.fit(train_skew_dataset, label)

        clf2.fit(train_kurt_dataset, label)

        return  clf1.predict(skew_test),clf2.predict(kurt_test)


    # 计算pearson相关系数。这需要在知道测试集数据标签的前提下，或者在已经通过多个特征训练出测试集数据标签的情况下，才能进行测试集标签与单特征的相关性。
    def cal_corr(self):
        train_trace_skew, train_warning_skew, train_trace_kurt, train_warning_kurt = data_gongwei_supervised().set_labels()
        train_skew = train_trace_skew + train_warning_skew
        train_kurt = train_trace_kurt + train_warning_kurt

        skew_predict, kurt_predict = data_gongwei_supervised().fit_predict()
        peason_skew_kurt = pearsonr(np.array(skew_predict), np.array(kurt_predict))
        print(peason_skew_kurt)


        true_label = list(np.append(np.ones(600, dtype=np.int), np.zeros(400, dtype=np.int)))
        skew_precision = precision_score(true_label, skew_predict, average='binary')
        kurt_precision = precision_score(true_label, kurt_predict, average='binary')


        peason_skew = pearsonr(np.array(true_label), np.array(skew_predict))
        peason_kurt = pearsonr(np.array(true_label), np.array(kurt_predict))
        return skew_precision, kurt_precision, peason_skew, peason_kurt




skew_precision, kurt_precision, peason_skew, peason_kurt = data_gongwei_supervised().cal_corr()

print(skew_precision)
print(kurt_precision)
print(peason_skew)
print(peason_kurt)






