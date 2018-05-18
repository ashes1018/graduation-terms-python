from __future__ import division
import numpy as np
import heapq
import math
import json
import datetime
import matplotlib.pyplot as plt
import requests
import http.client
import tornado.web
import tornado.ioloop




connection = http.client.HTTPConnection('')


def load_data(url):
    f = open(url)
    line = f.readline()
    data2 = {}
    while line:
        data1 = []
        data = json.loads(line)['data']
        time = json.loads(line)['time']
        time = datetime.datetime.fromtimestamp(float(time) / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
        data = data[1:len(data) - 1]
        for i in data.split(','):
            data1.append(float(i))
        # print(data1)
        # 返回”时间：data“的字典格式。
        data2[time] = data1
        # data1.clear()
        line = f.readline()
    return data2



def get_freq(data):
    pass

def get_statu(value, h):
    if value > h:
        return True
    else:
        return False

def get_meetingPlcaeId():
    pass

def get_DeviceId():
    pass

def get_warningStartTime(symbol, place_id, device_id, start_time, point, anomaly_times):
    dict = {"symbol":symbol,"place_id":place_id,"device_id":device_id,
            "start_time":start_time, "point_number":point, "anomaly_times":anomaly_times}
    return json.dumps(dict)


def get_fullWarningInfo(symbol, place_id, device_id, start_time, end_time, anomaly_point, anomaly_times, warning_points):
    dict = {"symbol":symbol, "place_id":place_id, "device_id":device_id,
            "start_time":start_time, "end_time":end_time, "anomaly_point":anomaly_point,
            "anomaly_times":anomaly_times,"warning_points":warning_points}
    return json.dumps(dict)


def http_post(url, values):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, values, headers=headers)
    return response

def gen_threshold():
    pass

def draw_point(point_list, count, time1, time2):
    x = range(len(point_list))
    y = point_list
    plt.figure()
    plt.plot(x, y)
    plt.title('anomaly at point:' + str(count) + '  from' + str(time1) + '  to' + str(time2))
    plt.xlabel("point list")
    plt.ylabel("energy value")
    plt.show()


class detect(tornado.web.RequestHandler):
    #
    # def __init__(self, ):
    #     pass


    def get(self):
        threshold = [30.9304, 30.6832, 31.3027, 31.5458, 31.0486, 31.0386, 31.0614, 31.1846, 31.4685, 31.0328, 31.1438, 31.9861, 31.7407, 31.8309, 31.9573, 33.4985, 33.176, 31.704, 30.4669, 30.5003, 30.5107, 30.5124, 30.7562, 31.4352, 31.2193, 31.8461, 30.9072, 31.0037, 30.8145, 31.015, 30.5552, 30.9652, 30.5038, 31.5331, 31.9086, 31.2599, 31.5075, 31.2608, 30.8159, 31.0411, 32.0432, 32.362899999999996, 33.036100000000005, 34.5001, 32.971199999999996, 32.6154, 32.4437, 32.414699999999996, 31.5627, 31.2305, 31.4121, 31.4988, 31.2734, 30.9076, 31.7554, 31.9422, 31.8712, 31.8356, 31.2229, 31.5372, 31.4034, 31.991, 31.3289, 31.215, 31.4854, 31.5363, 32.3662, 31.5637, 33.1706, 34.128299999999996, 34.2666, 33.6685, 32.1876, 32.525400000000005, 32.326899999999995, 33.0332, 33.3992, 33.4137, 33.8046, 33.091, 32.5226, 32.510000000000005, 32.4114, 32.872, 33.0852, 33.1546, 33.575900000000004, 32.8405, 32.3491, 33.332899999999995, 32.7513, 33.7912, 32.8417, 33.521100000000004, 33.9116, 33.9345, 36.1349, 34.856300000000005, 34.3692, 33.146699999999996, 33.9065, 33.936499999999995, 33.9735, 33.0586, 33.1699, 33.371700000000004, 33.3, 33.5054, 33.4858, 33.1369, 33.098, 33.0522, 33.1462, 33.1122, 33.8275, 33.8975, 33.7575, 33.415800000000004, 33.2876, 33.6803, 33.547, 33.5082, 33.4987, 33.396100000000004, 32.908, 33.3455, 33.3435, 33.7492, 33.812200000000004, 33.1507, 33.0061, 33.7495, 33.5426, 33.3765, 33.775800000000004, 33.333600000000004, 33.349599999999995, 33.6464, 33.116299999999995, 33.1329, 32.7504, 33.3019, 33.0715, 33.1235, 33.2565, 32.9315, 32.9143, 32.5229, 32.9947, 32.5095, 32.6963, 32.639399999999995, 32.3778, 31.9417, 31.9558, 32.3996, 32.6616, 32.6916, 32.4834, 31.8714, 32.3444, 32.3049, 32.076899999999995, 31.7406, 31.9706, 31.9249, 31.9831, 32.1563, 32.109700000000004, 31.7964, 32.0197, 31.6378, 31.7475, 31.5847, 31.9011, 31.1916, 31.3912, 31.3422, 31.4542, 31.6454, 31.3047, 30.9393, 30.9739, 31.6371, 30.9173, 30.605, 31.0201, 30.9809, 31.3676, 31.1691, 30.9272, 30.897, 30.9179, 30.748, 30.9209, 30.8693, 30.431, 30.3576, 30.7057, 30.4475, 30.6779, 30.7545, 30.3803, 30.5563, 30.2594, 30.2745, 30.5575, 30.4287, 30.3004, 30.0206, 30.7879, 30.4168, 30.1693, 30.0896, 30.155, 29.6786, 30.501, 30.171, 30.1607, 30.2176, 30.3421, 30.5512, 30.2916, 30.3981, 30.347, 30.0299, 30.2216, 30.2078, 30.5949, 30.255, 29.5951, 30.389, 30.0731, 30.2604, 30.6826, 30.6491, 29.8859, 29.7358, 29.6197, 30.2557, 30.5865, 30.1745, 30.2225, 29.8182, 29.9006, 30.1844, 30.1035, 30.3322, 30.3208, 29.9026, 30.2489, 30.3666, 30.3003, 30.0239, 30.207, 29.8948, 30.2693, 30.3672, 30.235, 30.5128, 30.3852, 30.2791, 30.3594, 30.6367, 30.3547, 30.2135, 30.0477, 30.3208, 30.4304, 30.4971, 30.7433, 30.4241, 30.4501, 30.9376, 31.069, 30.337, 30.3268, 30.4484, 30.63, 31.3901, 30.8479, 30.8447, 30.7269, 30.8378, 30.6179, 30.5532, 30.448, 30.463, 30.8537, 30.6893, 30.7663, 30.7447, 30.4291, 30.7093, 30.6949, 30.7184, 30.6053, 30.5528, 30.5975, 30.7072, 31.1524, 31.001, 30.7116, 30.2468, 30.5166, 30.3279, 30.5195, 31.9814, 30.6543, 30.3905, 30.9014, 30.334, 30.2244, 30.451, 31.1309, 30.4017, 30.4552, 30.4198, 30.6683, 30.7177, 30.893, 30.4765, 30.5332, 30.232, 30.3121, 30.2379, 30.2149, 30.0962, 30.2995, 30.4943, 30.2928, 29.9734, 30.1662, 30.1923, 30.3066, 30.7112, 30.2105, 30.3873, 30.1439, 30.2914, 30.3656, 30.2403, 30.218, 29.7876, 30.0853, 30.2847, 30.1559, 30.5483, 30.5939, 29.7175, 30.5101, 30.3177, 30.2844, 30.1977, 29.9795, 29.8758, 30.1173, 30.0314, 29.9318, 29.8473, 30.3892, 30.0177, 29.5093, 30.3615, 30.125, 30.021, 29.9912, 30.3182, 29.6107, 29.492, 29.5222, 29.8565, 29.7341, 29.8706, 29.9519, 29.7281, 29.7599, 29.6811, 30.0681, 29.9868, 29.8596, 29.7977, 29.8755, 30.1031, 29.8768, 29.3875, 29.9523, 29.8072, 29.6905, 30.1791, 29.968, 29.7937, 29.8089, 29.5113, 30.0411, 29.9899, 30.2405, 30.0104, 29.5128, 29.9798, 29.628, 29.5471, 29.5254, 29.9008, 29.8707, 29.7407, 29.9371, 30.2443, 29.8882, 41.705799999999996, 29.8398, 29.8859, 29.9645, 30.0392, 29.8195, 29.9983, 29.9696, 30.1456, 29.9931, 30.0226, 29.6536, 30.2409, 29.5412, 29.827, 30.329, 29.7839, 30.3085, 30.1429, 30.3936, 29.7662, 30.0299, 30.08, 29.8911, 30.0459, 29.3485, 29.9987, 29.8571, 29.8172, 29.7054, 30.3789, 29.9775, 29.6727, 29.8926, 30.1428, 29.7988, 30.1102, 29.4575, 30.195, 30.6779, 29.9457, 30.0489, 29.919, 29.6942, 29.7085, 30.5701, 29.7764, 29.4297, 30.2236, 30.1165, 30.422, 30.3168, 29.9606, 30.1277, 30.6409, 30.1125, 29.994, 30.2376, 30.0488, 30.9805, 29.9811, 29.8877, 30.0342, 29.8043, 29.8534, 29.9823, 29.8109, 30.1186, 29.7563, 30.3078, 30.1307, 30.1979, 30.0385, 30.0938, 29.9001, 30.1043, 30.1625, 29.9427, 30.0879, 30.4786, 29.9787, 30.4333, 30.0924, 30.0762, 29.6694, 30.0489, 30.1106, 30.177, 30.1096, 29.5302, 30.2785, 30.2912, 30.2672, 30.2629, 30.1366, 30.6361, 30.8118, 30.5167, 30.2909, 29.8669, 30.0756, 30.2934, 30.4055, 31.3328, 29.8039, 29.8751, 29.6918, 29.4779, 29.385, 29.5741, 29.4124, 29.8226, 29.5597, 29.5519, 29.8653, 29.7183, 29.6636, 29.7414, 29.5889, 29.4847, 29.2244, 29.4357, 29.8169, 29.9084, 30.2011, 29.3119, 29.3314, 29.8923, 29.2382, 29.4481, 29.4164, 29.0727, 29.339, 29.6463, 29.8049, 29.8348, 29.6087, 29.4003, 29.5981, 29.9888, 29.8505, 29.943, 29.8847, 29.3232, 29.2586, 30.1084, 29.6659, 29.6822, 29.7437, 29.8161, 29.671, 29.928, 29.6093, 29.8733, 29.2619, 29.7477, 29.4936, 29.8165, 29.4745, 29.5538, 29.1826, 29.8826, 29.2155, 29.4032, 30.1013, 29.1259, 29.4422, 29.1723, 29.404, 29.5108, 29.2677, 29.6992, 29.3949, 29.7417, 28.9045, 29.46, 29.1709, 29.512, 29.8783, 29.6663, 29.4451, 29.4691, 29.8195, 29.3703, 29.4778, 29.6407, 29.0563, 29.1248, 29.377, 29.5724, 29.7847, 29.4693, 29.5567, 29.6322, 29.5143, 29.8271, 29.5693, 29.7824, 29.6617, 29.4211, 29.2119, 29.6764, 29.0869, 29.332, 29.6172, 29.893, 29.2152, 29.6515, 29.6301, 29.5639, 29.6247, 29.7198, 29.2272, 29.6953, 29.9605, 29.7573, 29.4005, 29.6994, 29.9005, 29.2545, 28.958, 29.3918, 29.6442, 29.7036, 29.8216, 29.5567, 29.4526, 29.4566, 29.8171, 29.6944, 29.4869, 29.5794, 30.0428, 29.8529, 29.7023, 29.7529, 29.308, 29.5276, 29.4463, 29.5083, 29.4454, 29.8551, 29.3983, 29.6143, 29.9207, 29.5996, 30.2133, 29.447, 29.4882, 29.7988, 29.6413, 29.5734, 30.0187, 29.7111, 29.8584, 29.7952, 29.7668, 29.7828, 29.7466, 29.8264, 29.8252, 30.082, 29.867, 29.5729, 29.8737, 29.7743, 29.7074, 29.8094, 29.9214, 29.7213, 29.8772, 29.8918, 29.7435, 29.5505, 29.7195, 29.7372, 29.826, 29.4636, 29.3475, 29.5014, 29.9411, 29.8847, 30.2783, 29.855, 30.0536, 30.3864, 29.9748, 29.5484, 29.925, 29.6934, 29.5637, 29.7645, 29.7108, 30.0249, 29.5809, 29.5886, 29.8682, 29.3862, 29.8261, 29.8372, 29.8376, 29.8325, 30.1037, 29.9066, 30.2194, 30.1218, 30.144, 29.8423, 29.2274, 29.3169, 29.6106, 29.6783, 29.7462, 29.7587, 29.8873, 29.8226, 29.747, 29.4739, 29.2389, 29.4143, 29.4643, 29.7921, 29.5664, 30.2171, 29.6105, 29.8645, 30.0658, 29.3825, 29.5015, 29.3458, 29.4774, 29.5459, 29.5113, 29.5974, 29.3489, 29.2791, 30.0334, 29.7417, 29.3384, 29.7847, 29.634, 29.9814, 29.4831, 29.8054, 29.5307, 29.7787, 29.9982, 29.6053, 29.4353, 29.7228, 29.9603, 29.5709, 29.7799, 29.1808, 29.446, 29.4927, 29.8744, 29.3288, 29.6056, 30.2609, 29.8553, 29.5578, 29.8778, 29.9319, 30.1035, 29.3724, 30.0415, 29.5167, 29.5998, 29.6468, 29.7954, 29.7244, 29.7051, 29.772, 29.0695, 29.7686, 29.9605, 29.5, 29.3755, 29.4931, 29.6315, 29.4765, 29.7966, 29.8641, 30.1605, 29.6084, 30.1107, 29.4442, 29.4632, 29.3665, 29.3875, 30.2021, 30.2031, 29.334, 29.6273, 29.4616, 29.6042, 29.7994, 29.6558, 29.9746, 29.6186, 29.7643, 29.9687, 29.9206, 30.0116, 29.997, 29.5815, 30.1398, 29.5775, 29.6813, 29.5324, 29.5644, 29.9242, 29.5805, 29.8748, 29.6404, 29.6122, 29.8687, 30.1089, 30.0876, 29.7067, 29.977, 29.7254, 29.9156, 29.9309, 29.9508, 29.8939, 29.5809, 29.7112, 29.941, 29.9878, 30.0297, 30.267, 29.6705, 29.8216, 30.2052, 30.1422, 30.4266, 29.9301, 30.0847, 30.2521, 30.2031, 29.9057, 29.9591, 29.9568, 30.0004, 30.023, 30.3306, 30.007, 30.2149, 29.9133, 29.8173, 29.9676, 29.9325, 30.553, 30.5021, 29.8282, 29.9088, 29.8021, 29.7788, 30.3959, 29.87, 30.0004, 29.7389, 30.1166, 29.6887, 29.626, 29.9959, 30.2027, 30.6707, 30.1753, 30.0632, 30.2721, 29.9164, 30.1155, 30.1442, 30.0445, 29.8715, 30.3498, 29.8836, 30.0044, 29.9198, 30.2004, 30.0171, 29.7373, 30.2589, 30.1741, 30.6065, 30.4026, 30.2305, 30.0662, 29.9752, 29.9537, 30.1942, 29.9368, 30.3416, 30.1982, 30.1468, 30.1407, 30.2602, 30.0947, 29.7239, 29.7466, 30.7086, 29.9256, 30.2685, 30.1926, 30.152, 30.5454, 29.5073, 30.4845, 30.088, 31.3968, 29.9902, 29.7078, 30.0169, 29.7982, 29.6809, 29.6124, 29.9536, 29.6678, 29.7199, 29.9233, 29.9769, 30.3705, 29.7466, 29.7202, 29.765, 29.5373, 29.7892, 29.9465, 30.0652, 30.0893, 29.4916, 29.8287, 29.5052, 29.887, 29.686, 29.636, 29.394, 29.469, 30.0235, 29.1456, 29.8207, 29.5169, 29.8771, 29.3091, 29.3548, 29.5381, 29.6599, 30.0502, 30.01, 29.7105, 29.759, 29.2671, 29.7617, 29.7663, 29.6049, 30.2432, 29.4709, 30.0985, 29.7073, 30.0711, 29.7199, 29.4225, 29.9139, 29.8596, 29.4398, 30.2403, 29.6831, 29.5381, 29.3497, 29.7479, 30.2217, 29.5995, 29.7519, 29.5932, 30.019, 29.5195, 29.5479, 30.1277, 29.6667, 29.5142, 30.2087, 29.2198, 29.4695, 29.6549, 29.6074, 29.4316, 29.4757, 29.859, 29.9356, 29.9294, 29.1679, 29.2728, 29.446, 29.8438, 29.9045, 29.4207, 29.5055, 29.3757, 30.1822, 30.1949, 29.4505, 29.7653, 29.9636, 29.5556, 29.9215, 29.9219, 29.9478, 29.6131, 30.1398, 29.2544, 29.8206, 29.9708]

        data = load_data('D:/2018.4.27/data_test.txt')

        # count用于对一条数据的维数进行计数
        count = 0
        l = len(threshold)
        anomaly_list = {}
        # 监测列表用于记录每个频点处，大于对应阈值的次数，初始每个点处的次数都为0
        monitor = [0] * l
        point_cache = [[] for x in range(l)]
        status = [False] * l
        x = 0
        y = 0
        test_list1 = []
        test_list2 = []
        # 对每一条数据
        for i in data:
            # 对每条待比较数据和阈值中的每个频点的比较
            for (m, n) in zip(threshold, data[i]):
                # 如果对应频点大于阈值
                if n > m:
                    # 返回字典形式，字典的key值表示产生告警时间，value值表示频点值及产生告警值大小。
                    # anomaly_list[i] = str(count / l * 100 + 200) + '|' + str(n)
                    # 监测频点处的告警次数加1
                    monitor[count] += 1
                    # 将异常频点值加入对应列表，供后续画图
                    point_cache[count].append(n)
                    # 如果某频点处大于阈值，且大于阈值的次数大于5次，记录下当前的时间
                    if n > m and monitor[count] > 5:
                        warning_dict = []
                        time1 = i
                        warning_start = get_warningStartTime("under warning", "1", "2", time1,
                                                             str(count / l * 100 + 200), monitor[count])

                        if x < 10:
                            test_list1.append(warning_start)
                            x+=1
                        # self.write(warning_start)
                        # self.write(',')
                    # if monitor[count]  > 5:
                    #     status[count] = True
                    status[count] = get_statu(monitor[count], 5)

                    # if monitor[count] % 5 == 0:
                    #     print('point ' + str(count) + ' still alert!' + str(status[count]))

                # 如果对应频点小于阈值
                if n < m:
                    # 如果当前频点小于阈值但出现大于阈值的次数大于5
                    if n < m and monitor[count] > 5:
                        # 记录下当前时间
                        time2 = i
                        # 一次告警结束，给出完整告警信息
                        fullWarningInfo = get_fullWarningInfo("end warning", "1", "2", time1, time2,
                                                              str(count / l * 100 + 200), monitor[count], point_cache[count])

                        test_list2.append(fullWarningInfo)
                        # self.write(fullWarningInfo)
                        # print("start time:" + str(time1) + "  end time:" + str(time2)+"  anomaly point:"+str(count)+"  anomaly times:"+str(monitor[count]))
                        # 告警结束，将该频点超过阈值的次数置零
                        monitor[count] = 0
                        # 绘制异常频点图像
                        # draw_point(point_cache[count], count, time1, time2)
                        # 一次告警结束，异常频点列表清零
                        point_cache[count].clear()
                        status[count] = False
                    #   如果出现的是小量超过阈值的情况，可认为不是告警。此时，对应频点告警数置0，对应告警缓存清空。
                    elif n < m and 0 < monitor[count] <= 5:
                        monitor[count] = 0
                        point_cache[count].clear()
                # 对下一个频点进行检测
                count += 1
            # 一轮检测结束,count置0
            count = 0
        print(test_list1)
        print(test_list2)
        # return anomaly_list, monitor

if __name__ == '__main__':
    # 创建一个应用对象
    app = tornado.web.Application([(r'/', detect)])
    # 绑定一个监听端口
    app.listen(8888)
    # 启动web程序，开始监听端口的连接
    tornado.ioloop.IOLoop.current().start()








