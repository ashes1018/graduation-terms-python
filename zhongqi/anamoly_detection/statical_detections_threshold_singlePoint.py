import json
import numpy as np
import datetime

url = "C:/Users/l.c/Desktop/tasks/graduation projection/midterm/data/data/test.txt"
epoch = 10


def data_clean():
    f = open(url)
    line = f.readline()
    value_process = []
    count = 0
    a = []

    while line:
        line = json.loads(line)
        value = line['data'][1:len(line['data']) - 1]
        length = len(value.split(','))

        value_process.append(float(value.split(',')[565]))
        count = count + 1

        if count % 10 == 0:
            a.append(np.mean(value_process))
            value_process.clear()
            if count % 30 == 0:
                x_predict = a[0] * 0.4 + a[1] * 0.6
                if abs(x_predict - a[2]) > 2:
                    time = line['time']
                    # time = datetime.datetime.fromtimestamp(float(line['time']) / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
                    print(str(time) + "-----alert")

                # if abs(x_predict - a[2]) > 4:
                #     # time = datetime.datetime.fromtimestamp(float(line['time']) / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
                #     time = line['time']
                #     print(str(time) + "alert!!!")
                #
                # if abs(x_predict - a[2]) > 6:
                #     # time = datetime.datetime.fromtimestamp(float(line['time']) / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
                #     time = line['time']
                #     print(str(time) + "alert!!!!!!!")
                a.clear()
        line = f.readline()


value_process = data_clean()
