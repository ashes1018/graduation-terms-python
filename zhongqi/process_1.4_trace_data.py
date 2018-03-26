import json
import datetime
from collections import Counter
import matplotlib.pyplot as plt


class trace_process():
    def __init__(self,read_url,write_url):
        self.read_url = read_url
        self.write_url = write_url

    # 对trace数据处理的第一步,针对字段顺序及格式的处理
    def process_chase_1(self):
        f = open(self.read_url)
        line = f.readline()
        i = 0
        trace_dict = {}
        while i < 2644:
            line = f.readline()
            line_json = json.loads(line)
            value = float(line_json["traceInTime"])
            del(line_json['type'])
            del (line_json['message'])
            del(line_json['traceInTime'])
            key = json.dumps(line_json)
            trace_dict[key] = value
            # time.append(float(line_json["traceInTime"]))
            i = i+1

        # 找出出现trace数据中一个时间戳出现两次的数据
        # sub = [i for i in time if time.count(i) > 1]
        # print(sub)
        print(len(trace_dict))
        return trace_dict

    # 对trace数据处理的第二步，主要是对traceInTime这个字段处理，使之符合json处理的格式
    def process_chase_2(self):
        trace_dict = demo.process_chase_1()

        new_trace_dict = sorted(trace_dict.items(), key=lambda item: item[1])


        f = open(self.write_url,'w')
        for i in new_trace_dict:
            # print(i)
            temp = []
            x = datetime.datetime.fromtimestamp(i[1] / 1000).strftime('%Y-%m-%d %H:%M:%S.%f')
            temp.append(i[0] + ' ' + x)
            # print(temp)
            temp_process = str(temp).split('}')
            temp_process_2 = '"'+'traceInTime'+'"'+ ':' +'"'+temp_process[1]+'"'+', '+ temp_process[0][1:len(temp_process[0])]
            temp_process_3 = temp_process_2[:42]
            temp_process_33 = temp_process_3[:14]
            temp_process_333 = temp_process_3[16:]
            temp_process_4 = temp_process_2[49:]
            res = '{'+temp_process_33+" "+'"'+temp_process_333+'"'+", "+temp_process_4+'}'
            f.write(res+'\n')

    # 步骤2在数据写入时候，将除了traceInTime之外的字段当做key值，traceInTime当做value值，发现有重复key字段，说明存在同一时间写入多次的操作。
    def process_chase_3(self):
        f = open("C:/Users/l.c/Desktop/tasks/electromagnetism/2018.1.4_data_analysis/emcas-2018.01.04_trace_process.txt",'r')
        line = f.readline()
        centerFreq = []
        while line:
            line_json = json.loads(line)
            centerFreq.append(line_json['centerFreq'])
            line = f.readline()

        return centerFreq




    def trace_pic_analysis(self):
        x = ['30-500', '500-1000', '1000-2700', '2700-6000']
        y = [677, 675, 659, 623]
        fig  = plt.figure()
        plt.xlabel("frequency range")
        plt.ylabel("number")
        plt.title("number of various frequencies")
        plt.bar(range(len(y)),y,0.4,color='rgb',tick_label = x)
        plt.savefig('C:/Users/l.c/Desktop/tasks/electromagnetism/2018.1.4_data_analysis/frequency.jpg')
        plt.show()






read_url = "C:/Users/l.c/Desktop/tasks/electromagnetism/2018.1.4_data_analysis/emcas-2018.01.04_trace.txt"
write_url = "C:/Users/l.c/Desktop/tasks/electromagnetism/2018.1.4_data_analysis/emcas-2018.01.04_trace_process.txt"
demo = trace_process(read_url,write_url)
centerFreq = demo.process_chase_3()
print(centerFreq)


# demo.trace_pic_analysis()
