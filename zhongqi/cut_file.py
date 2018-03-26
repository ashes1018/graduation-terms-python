import json

class cutfile():
    def __init__(self):
        pass

    def cut_1(self):
        file = open('C:/Users/l.c/Desktop/tasks/毕设/中期/2018.1.4数据/emcas-2018.01.04_trace.txt')
        file2 = open('C:/Users/l.c/Desktop/tasks/毕设/中期/2018.1.4数据/emcas-2018.01.04_trace_200.txt','w')
        i = 0
        while i < 50:
            line = file.readline()
            file2.write(line)
            i = i + 1

    def read_time(self):
        file = open('C:/Users/l.c/Desktop/tasks/毕设/中期/2018.1.4数据/emcas-2018.01.04_trace.txt')
        file2 = open('C:/Users/l.c/Desktop/tasks/毕设/中期/2018.1.4数据/emcas-2018.01.04_trace_200.txt')
        line1 = file.readline()
        line2 = file2.readline()
        trace_time = []
        warning_time = []

        while line1:
            line1 = file.readline()
            trace_time.append(json.loads(line1)['@timestamp'])


        while line2:
            line2 = file2.readline()
            warning_time.append(json.loads(line2)['@timestamp'])
            # print(json.loads(line2)['@timestamp'])
        return trace_time,warning_time


temp = cutfile()
trace_time, warning_time = temp.read_time()
print(len(trace_time))
print(len(warning_time))