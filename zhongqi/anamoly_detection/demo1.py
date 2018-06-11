import numpy as np
import json


# f = open("D:/20171018/0.txt")
# line = f.readline()
# count = 0
# while count < 1000:
#     line = json.loads(line)
#     print("ss")
#     print(line['startFreq'])
#     line = f.readline()
#     count +=1
    # if str(line['startFreq']) is '20':
    #     print(line['startFreq']+line['data'].split(']')[1])
    #     count += 1
    #     line = f.readline()

# a = [[5,6,7],[2,3,4],[3,4,5],[8,1,10]]
# # print(len(a))
#
# for j in range(len(a[0])):
#     b = []
#     for i in range(len(a)):
#         b.append(a[i][j])
#     print(max(b))







# with open('E:/2017.10.20 data/warning_1.txt') as f:
#     line  = f.readline()
#     ff = open('E:/2017.10.20 data/warning_2.txt', 'w')
#     while line:
#         line = json.loads(line)
#         if float(line['anomaly_times']) > 200:
#             # line['anomaly_point'] = float(line['anomaly_point']) * 4-400
#             data = str(line['anomaly_times'])+'|'+str(line['start_time']) + '|'+str(line['end_time'])+ '|'+str(line['anomaly_point'])\
#                    +'|'+str(line['device_id'])
#             ff.write(data+"\n")
#         line = f.readline()




# with open('D:/2017.10.20 data/54/0.txt') as f:
#     line = f.readline()
#     result = []
#     while line:
#         line = json.loads(line)
#         if float(line['startFreq']) == 400:
#             result.append(line)
#         line = f.readline()
#
#
# result.sort(key=lambda x:x["traceInTime"])
# f_w = open('D:/2017.10.20 data/54/f_w.txt','a')
# for i in result:
#     f_w.write(str(i)+'\n')



# a = [3,3,3,3,3,3,3,3]
# b = [[4,4,8,2,1,1,4,4],[5,5,5,2,1,1,4,4],[6,6,6,2,1,1,4,4]]
# c = [4,4,4,2,1,1,4,4]
# d = [{'a':[4,4,8,2,1,1,4,4]},{'b':[5,5,5,2,1,1,4,4]},{'c':[6,6,6,2,1,1,4,4]}]
# e = [[4,4,8,2,1,1,4,4],[5,5,5,2,1,1,4,4],[6,6,6,2,1,1,4,4]]


# for i in range(len(d)):
#     for count in range(len(a)):
#         print(d[i][count])


# for i in d:
#     # print(list(i.values())[0][0])
#     for count in range(len(a)):
#         if list(i.values())[0][count] > a[count]:
#             print(list(i.values())[0][count])


# count = 0
# for i in b:
#     print(i)
#     for (m,n) in zip(a,i):
#         if n > m:
#             count += 1
#             if count > 2:
#                 break
#             print(n)


# print(len(b))
#
# for k in range(len(b)):
#     for i in range(len(a)):
#         if a[i] < b[k][i]:
#             print('ss')

#
# import socket
#
# PORT = 9999
# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP socket对象
# s.bind(('', PORT))  # 绑定地址
# s.listen(1)  # 监听TCP，1代表：操作系统可以挂起(未处理请求时等待状态)的最大连接数量。该值至少为1
# conn, addr = s.accept()  # 开始被动接受TCP客户端的连接。
# print('连接的地址', repr(addr))
#
# while 1:
#     data = conn.recv(10000)
#     print(data)



f = open('D:/trace2.txt','r')
data = f.readline()
count1 = []
count2 = []
count3 = []
count4 = []


while data:

    data = str(data)

    time = data.split('|')[1]
    collectorId = data.split('|')[2]
    startFreq = data.split('|')[3]
    stopFreq = data.split('|')[4]
    rbw = data.split('|')[5]
    pointNum = data.split('|')[9]
    value = data.split('|')[10]
    value_process = value[1:len(value) - 6]

    v = []
    for k in value_process.split(','):
        v.append(float(k))


    if startFreq == '30':
        count1.append(len(v))

    if startFreq == '500':
        count2.append(len(v))

    if startFreq == '1000':
        count3.append(len(v))

    if startFreq == '2700':
        count4.append(len(v))

    data = f.readline()

print(count1)
print(count2)
print(count3)
print(count4)























