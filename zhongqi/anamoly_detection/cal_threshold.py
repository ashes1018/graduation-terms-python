import json
import socket


PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP socket对象
s.bind(('', PORT))  # 绑定地址
s.listen(1)  # 监听TCP，1代表：操作系统可以挂起(未处理请求时等待状态)的最大连接数量。该值至少为1
conn, addr = s.accept()  # 开始被动接受TCP客户端的连接。
print('连接的地址', repr(addr))


f_1 = open("D:/qdfh/threshold/back1.txt", 'w')
f_2 = open("D:/qdfh/threshold/back2.txt",'w')
f_3 = open("D:/qdfh/threshold/back3.txt", 'w')
f_4 = open("D:/qdfh/threshold/back4.txt",'w')
f_5 = open("D:/qdfh/threshold/back5.txt", 'w')




f_threshold = open("D:/qdfh/threshold/threshold.txt",'w')



count_1 = 0
count_2 = 0
count_3 = 0
count_4 = 0
count_5 = 0

# 连续采1000条用来计算背景
while count_1 < 1000 or count_2 < 1000 or count_3 < 1000 or count_4 < 1000 or count_5 < 1000:
    data = conn.recv(10000)

    if not data:
        print("连接中断")
        break

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
        if count_1 == 1000:
            continue
        f_1.write(str(v)+'\n')
        count_1 += 1


    if startFreq == '500':
        if count_2 == 1000:
            continue
        f_2.write(str(v) + '\n')
        count_2 += 1

    if startFreq == '1000':
        if count_3 == 1000:
            continue
        f_3.write(str(v) + '\n')
        count_3 += 1

    if startFreq == '2000':
        if count_4 == 1000:
            continue
        f_4.write(str(v) + '\n')
        count_4 += 1

    if startFreq == '4000':
        if count_5 == 1000:
            continue
        f_5.write(str(v) + '\n')
        count_5 += 1



#计算第1段阈值
with open("D:/qdfh/threshold/back1.txt",'r') as f:
    bg_list=[]
    line = f.readline()

    print(len(line.split(',')))

    while line:
        # print(line[1:len(line)-2])
        line = line[1:len(line)-2].split(',')

        line_process = []
        for i in line:
            line_process.append(float(i))
        bg_list.append(line_process)
        line = f.readline()

point_num = len(bg_list[0])


bg_list_aft = [0] * point_num
bg_list_times = [0] * point_num

for i in range(point_num):
    b=[]
    for j in range(len(bg_list)):
        b.append(bg_list[j][i])
    bg_list_aft[i]=max(b)
    bg_list_times[i]=1.25*max(b)



#bg_list_aft为最大值保持的背景迹线list
# print(bg_list_aft)

#bg_list_times为乘以倍数的阈值曲线

print("第一段的阈值是：")
print(bg_list_times)
f_threshold.write("第一段阈值是："+'\n')
f_threshold.write(str(bg_list_times) + '\n')

# print(len(bg_list_aft))
print(len(bg_list_times))




#计算第2段阈值
with open("D:/qdfh/threshold/back2.txt",'r') as f:
    bg_list=[]
    line = f.readline()

    print(len(line.split(',')))

    while line:
        # print(line[1:len(line)-2])
        line = line[1:len(line)-2].split(',')

        line_process = []
        for i in line:
            line_process.append(float(i))
        bg_list.append(line_process)
        line = f.readline()

point_num = len(bg_list[0])

bg_list_aft = [0] * point_num
bg_list_times = [0] * point_num

for i in range(point_num):
    b=[]
    for j in range(len(bg_list)):
        b.append(bg_list[j][i])
    bg_list_aft[i]=max(b)
    bg_list_times[i]=1.25*max(b)




#bg_list_times为乘以倍数的阈值曲线

print("第二段的阈值是：")
print(bg_list_times)

f_threshold.write("第二段阈值是："+'\n')
f_threshold.write(str(bg_list_times) + '\n')
print(len(bg_list_times))


#计算第3段阈值
with open("D:/qdfh/threshold/back3.txt",'r') as f:
    bg_list=[]
    line = f.readline()

    print(len(line.split(',')))

    while line:
        # print(line[1:len(line)-2])
        line = line[1:len(line)-2].split(',')

        line_process = []
        for i in line:
            line_process.append(float(i))
        bg_list.append(line_process)
        line = f.readline()

point_num = len(bg_list[0])


bg_list_aft = [0] * point_num
bg_list_times = [0] * point_num

for i in range(point_num):
    b=[]
    for j in range(len(bg_list)):
        b.append(bg_list[j][i])
    bg_list_aft[i]=max(b)
    bg_list_times[i]=1.25*max(b)



#bg_list_times为乘以倍数的阈值曲线

print("第三段的阈值是：")
print(bg_list_times)
f_threshold.write("第三段阈值是："+'\n')
f_threshold.write(str(bg_list_times) + '\n')

# print(len(bg_list_aft))
print(len(bg_list_times))


#计算第4段阈值
with open("D:/qdfh/threshold/back4.txt",'r') as f:
    bg_list=[]
    line = f.readline()

    print(len(line.split(',')))

    while line:
        # print(line[1:len(line)-2])
        line = line[1:len(line)-2].split(',')

        line_process = []
        for i in line:
            line_process.append(float(i))
        bg_list.append(line_process)
        line = f.readline()

point_num = len(bg_list[0])


bg_list_aft = [0] * point_num
bg_list_times = [0] * point_num

for i in range(point_num):
    b=[]
    for j in range(len(bg_list)):
        b.append(bg_list[j][i])
    bg_list_aft[i]=max(b)
    bg_list_times[i]=1.25*max(b)


#bg_list_times为乘以倍数的阈值曲线

print("第四段的阈值是：")
print(bg_list_times)
f_threshold.write("第四段阈值是："+'\n')
f_threshold.write(str(bg_list_times) + '\n')

# print(len(bg_list_aft))
print(len(bg_list_times))



#计算第五段阈值
with open("D:/qdfh/threshold/back5.txt",'r') as f:
    bg_list=[]
    line = f.readline()

    print(len(line.split(',')))

    while line:
        # print(line[1:len(line)-2])
        line = line[1:len(line)-2].split(',')

        line_process = []
        for i in line:
            line_process.append(float(i))
        bg_list.append(line_process)
        line = f.readline()

point_num = len(bg_list[0])


bg_list_aft = [0] * point_num
bg_list_times = [0] * point_num

for i in range(point_num):
    b=[]
    for j in range(len(bg_list)):
        b.append(bg_list[j][i])
    bg_list_aft[i]=max(b)
    bg_list_times[i]=1.25*max(b)



#bg_list_aft为最大值保持的背景迹线list
# print(bg_list_aft)

#bg_list_times为乘以倍数的阈值曲线

print("第五段的阈值是：")
print(bg_list_times)
f_threshold.write("第五段阈值是："+'\n')
f_threshold.write(str(bg_list_times) + '\n')

print(len(bg_list_times))