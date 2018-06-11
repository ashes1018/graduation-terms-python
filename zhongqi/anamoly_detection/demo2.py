import socket


HOST = '10.10.41.160'
PORT = 9999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建TCP socket对象
s.bind(('', PORT))  # 绑定地址
s.listen(1)  # 监听TCP，1代表：操作系统可以挂起(未处理请求时等待状态)的最大连接数量。该值至少为1
conn, addr = s.accept()  # 开始被动接受TCP客户端的连接。
print('连接的地址', repr(addr))
count = 0

f = open("E:/data/1.txt",'w')

while 1 and count < 2:

    data = conn.recv(10000)
    print(len(data))
    if not data:
        break
    data = str(data)
    print(data)
    value = data.split('|')[10]

    print(value[1:len(value)-4])
    value = value[1:len(value)-4]
    v = []
    for k in value.split(','):
        v.append(float(k))

    print(v)
    print(len(v))
    # f.write(str(data)+'\n')

    count += 1
