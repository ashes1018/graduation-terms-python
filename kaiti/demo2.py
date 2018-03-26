import json
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm as CM
from matplotlib import axes


class demo2():
    def __init__(self):
        pass

    def process_jsonfile(self):
        url = 'C:/Users/l.c/Desktop/科研/毕设/开题/工程文件/trace.txt'
        file = open(url,'rb')
        l = list()
        i = 0
        while i < 20:
            data = json.loads(file.readline())
            temp = data['data'].split(']')[0][1:len(data['data'].split(']')[0])-1]
            # print(temp)
            temp2 = [float(x) for x in temp.split(',')]
            # print(max(temp2))
            l.append(temp2)
            i = i + 1
        file.close()
        return l

    def draw_image(self):
        l = demo2().process_jsonfile()
        ll = np.array(l)
        print(l)
        print(ll)
        fig = plt.figure(facecolor='w',figsize=(20,20))
        ax1 = fig.add_subplot(2, 1, 1, position=[0.1, 0.15, 0.9, 0.8])
        # ax1.set_xticklabels(range(1000))
        cmap = CM.get_cmap('spectral',1000)
        map = ax1.imshow(ll, interpolation="nearest", cmap=cmap,aspect='auto', vmin=0, vmax=50)
        cb = plt.colorbar(mappable=map, cax=None, ax=None, shrink=0.5)
        cb.set_label('(%)')
        plt.show()



# demo2().process_jsonfile()
demo2().draw_image()

# array = np.array([
#
# ])
