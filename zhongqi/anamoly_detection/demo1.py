import numpy as np
import json


f = open("D:/20171018/0.txt")
line = f.readline()
count = 0
while count < 1000:
    line = json.loads(line)
    print("ss")
    print(line['startFreq'])
    line = f.readline()
    count +=1
    # if str(line['startFreq']) is '20':
    #     print(line['startFreq']+line['data'].split(']')[1])
    #     count += 1
    #     line = f.readline()

