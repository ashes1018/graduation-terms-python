import math
import numpy as np
import matplotlib.pyplot as plt
import json
import datetime
from scipy.stats import entropy
from zhongqi.anamoly_detection import utils


class cusum():

    def __init__(self):
        pass

    #   return data2{time: data1}
    def load_data(self, url):
        f = open(url)
        line = f.readline()
        data1 = []
        data2 = {}
        while line:
            data = json.loads(line)['data']
            time = json.loads(line)['time']
            time = datetime.datetime.fromtimestamp(float(time) / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
            data = data[1:len(data) - 1]
            for i in data.split(','):
                data1.append(float(i))
            # print(data1)
            data2[time] = data1
            data1 = []
            line = f.readline()
        return data2

        # based on entroy
    def window_split0(self, url):
        data = cusum().load_data(url)
        base_process = {}
        for (key, value) in data.items():
            base_process[key] = value[565]
        return base_process

    # based on entroy
    def window_split(self,url):
        base = [19.0468, 19.5561, 19.2619, 18.8752, 19.0573, 18.8339, 19.2258, 19.817, 19.6027, 19.2829]
        data = cusum().load_data(url)
        entropy_process = {}
        for (key,value) in data.items():
            entropy_process[key] = cusum().cal_entroy(base, value[560:570])
        return  entropy_process


        # based on mean value
    def window_split2(self, url):
        data = cusum().load_data(url)
        mean_process = {}
        for (key, value) in data.items():
            # print(sum(value[564:567])/3)
            mean_process[key] = sum(value[564:567])/3
        return mean_process


        # based on mean var
    def window_split3(self, url):
        data = cusum().load_data(url)
        var_process = {}
        for (key, value) in data.items():
            var_process[key] = np.var(value[560:570])
        return var_process


    def cal_entroy(self, x, y):
        # use api from scipy
        KL1 = entropy(x,y)
        # way 2
        # KL2 = 0
        # for i in range(len(x)):
        #     KL2 += x[i] * np.log(x[i] / y[i])
        return KL1


    def estimate_h(self, vals):
        return 4.0 * utils.stddev(vals)

    def bulid_k(self, vals, ma ,s = 1.5):
        md = s * utils.stddev(vals) + ma
        return (md - ma) / (math.log(md, math.e) - math.log(ma, math.e))

    def cusum(self, vals, k ,h):
        shvals = []
        hlist = []
        shift = 0
        count = 0
        normal_point = 0
        for val in vals:
            hlist.append(h)
            shift += max(0, val -k + shift)
            if(shift == 0):
                normal_point += 1
            shvals.append(shift)
            if shift >= h:
                print("alarm")
                shift = 0
                count += 1
        print(count)
        print(normal_point)
        return (shvals, hlist)

if __name__ == "__main__":
    temp = cusum()

    data2 =  [19.8921, 19.6689, 19.6079, 19.7223, 19.2608, 19.2385, 18.945, 19.5867, 19.738, 19.9228, 19.6033, 19.6091, 19.0941, 19.9209, 19.1984, 19.5095, 19.0502, 19.6787, 19.6731, 19.7698, 20.0229, 19.3845, 19.8917, 19.7554, 19.5302, 19.5214, 19.218, 19.2709, 19.6168, 19.4278, 19.5331, 19.6835, 19.7217, 19.749, 19.3141, 19.8694, 19.4887, 19.5996, 19.1879, 19.6044, 19.6288, 19.2633, 19.2633, 19.3296, 19.3844, 19.5993, 19.9438, 19.4836, 19.7916, 18.9623, 19.7256, 19.6654, 19.81, 19.7147, 19.5158, 19.7635, 19.4408, 19.2301, 19.9743, 19.8932, 33.1625, 32.6344, 33.211, 33.2764, 33.9231, 32.9925, 32.6936, 33.4764, 33.0999, 32.6118, 32.0418, 32.0027, 32.5558, 32.1868, 32.2629, 31.9404, 32.5592, 32.3619, 32.2953, 31.4362, 31.1081, 30.5129, 30.0534, 30.1158, 29.8837, 30.4081, 28.8907, 27.4088, 31.285, 32.313, 32.342, 31.1015, 32.3293, 33.4409, 33.2661, 32.0613, 31.3783, 31.2744, 30.5021, 30.2182]





    # k = temp.bulid_k(data, np.mean(data))
    # h = temp.estimate_h(data2)
    # print(h)
    # shvals, hlist = temp.cusum(data, k, h)
    # plt.plot(shvals, "-go")
    # plt.plot(hlist, "-rx")
    # plt.show()

    # data_process = temp.window_split("E:/2018.5.2/1.txt")
    # base_data = list(data_process.values())[550:700]
    # h = temp.estimate_h(base_data)
    # print(h)

    # data_test = temp.window_split("E:/2018.5.2/2.txt")
    #
    # base_data = list(data_test.values())[200:300]
    # h = temp.estimate_h(base_data)
    # print(h)
    #
    # test_data = list(data_test.values())[100:150]
    # k = temp.bulid_k(test_data, np.mean(test_data))
    # shvals, hlist = temp.cusum(test_data, k, h)
    # plt.plot(shvals, "-go")
    # plt.plot(hlist, "-rx")
    # plt.show()


    # data = temp.window_split0("E:/2018.4.27/data0m.txt")
    data = [60.1476, 60.1389, 59.9241, 59.0461, 60.3852, 59.6358, 59.5352, 60.3413, 60.2105, 59.6076, 59.324, 59.4554, 59.7672, 59.8834, 59.7732, 59.6183, 59.2916, 59.0804, 58.9084, 59.096, 59.505, 59.6717, 59.5005, 59.4569, 59.9523, 59.6174, 59.6703, 59.5733, 59.6703, 59.5504, 59.5836, 59.6651, 59.6458, 59.5501, 59.5858, 59.5708, 59.6408, 59.6479, 59.6221, 59.5727, 59.614, 59.5384, 59.4381, 59.3804, 59.5026, 59.7139, 59.894, 59.9678, 59.7595, 59.8083]








    # base_data = list(data.values())[200:300]
    h = temp.estimate_h(data2)
    print(h)

    # print(list(data.values())[:50])
    print(list(data))

    test_data = list(data)
    # test_data = list(data.values())[:50]
    k = temp.bulid_k(test_data, np.mean(test_data))
    print(k)



    shvals, hlist = temp.cusum(test_data, k, h)
    print(shvals)
    plt.plot(shvals, "-go")
    plt.plot(hlist, "-rx")
    plt.show()