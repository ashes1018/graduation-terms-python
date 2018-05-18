#! /usr/bin/env python
# -*- coding:utf-8 -*-
# Author:Cherry Lang
import pywt
import json
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.sandbox.stats.diagnostic import  acorr_ljungbox


def wt(data,wavefunc, level, m, n):
    """
    小波降噪函数
    - level: 分解层数；
    - data: 保存列表类型的字典；
    - keyname: 键名；
    - index_list: 待处理序列；
    - wavefunc: 选取的小波函数；
    - m,n 选择进行阈值处理的小波系数层数
    """
    # 分解
    coeff = pywt.wavedec(data, wavefunc, mode='sym', level=level)
    #print(coeff)
    # 设置 sgn 函数
    sgn = lambda x: 1 if x > 0 else -1 if x < 0 else 0
    # 降噪过程
    for i in range(m, n + 1):  # 选取小波系数层数为 m~n 层
        cD = coeff[i]
        for j in range(len(cD)):
            Tr = np.sqrt(2 * np.log(len(cD)))  # 计算阈值
            if cD[j] >= Tr:
                coeff[i][j] = sgn(cD[j]) - Tr  # 使用 sgn 函数向零收缩
            else:
                coeff[i][j] = 0  # 低于阈值置零
    # 重新构建
    denoised_data_list = pywt.waverec(coeff, wavefunc)
    # 为了避免出现负值的情况，取绝对值
    abs_denoised_list = list(map(lambda x: abs(x), denoised_data_list))
    # 返回降噪结果
    return abs_denoised_list








list_pre=[]
list_aft=[]
with open("C:/Users/l.c/Desktop/tasks/graduation projection/midterm/data/data/test.txt",'r',encoding="utf-8") as f:

    line = f.readline()
    while line:
        #读json数据
        json_data=json.loads(line)
        #json格式的data数据
        data_point=json_data['data']
        #data内为['','','','']格式的字符串，变成list
        point_1=data_point[1:len(data_point) - 1]
        list_point = point_1.split(",")
        #把list里的'12'变成float类型
        for i in range(len(list_point)):
            list_point[i]=float(list_point[i])
        list_pre.append(list_point)
        line = f.readline()


pre_565 = []
aft_565 = []

for i in list_pre:
    pre_565.append(i[565])
    aft_565.append(wt(i, 'db3', 4, 1, 4)[565])

import matplotlib.pyplot as plt
x = np.arange(0,1000)
y1 = pre_565
y2 = aft_565


qljungbox, pval, qboxpierce, pvalbp = acorr_ljungbox(y1, boxpierce=True)
plt.plot(range(0, len(pval)), pval)
plt.plot(range(0, len(pvalbp)), pvalbp)
plt.legend()
plt.show()


plt.plot(x,y1)
plt.plot(x,y2)

plt.show()



