import sys
from collections import deque
import copy
import numpy as np

from math import *
def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline

def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [H, W] = [int(input_raw[0]), int(input_raw[1])]
    input_raw = read_func().strip().split()
    [N] = [int(input_raw[0])]
    input_raw = list(read_func().strip().split())
    #color_num_list = []
    #color_num_list = {}
    color_num_list = np.zeros((N))
    for i in range(N):
        color_num_list[i] = (int(input_raw[i]))

    index_list = np.argsort(color_num_list)[::-1]
    sorted_color_num = np.sort(color_num_list)[::-1]

    mat = np.zeros((H, W),'int')
    now_i = 0
    now_j = 0
    rev_flag = False
    #tmp_color_num_list = copy.deepcopy(color_num_list)
    #while len(color_num_list) > 0:
        #color_num = max(color_num_list.values())
        #color = color_num_list.keys()[color_num_list.values().index(color_num)]
        #color_num_list.pop(color)
        #tmp_color_num_list.remove(color_num)
    for i in range(N):
        color_num = sorted_color_num[i]
        color = index_list[i] + 1
        while color_num > 0:
            mat[now_i][now_j] = color
            if (now_j < W - 1 and rev_flag == False)  or  (now_j >= 1 and rev_flag == True):
                s = -1 if rev_flag == True else 1
                now_j += s
            else:
                now_i += 1
                rev_flag = not(rev_flag)
            color_num -= 1

    for i in range(H):
        for j in range(W):
            print mat[i][j],
        print


if __name__ == '__main__':
    main()
