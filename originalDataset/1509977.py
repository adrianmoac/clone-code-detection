
import sys
from collections import deque
import copy

from math import *
def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline

#class edge:
#    def __init__(x, y, cost):

class point_node:
    def __init__(self, point, cost):
        self.point = point
        self.cost = cost

def  BFS(con_list, start_point):
    cost_list = {}
    cost_list[start_point] = 0

    node_list = deque([point_node(start_point, 0)])
    while 1:
        #new_node_list = []
        #for i in range(len(node_list)):
        now_node = node_list.popleft()
        connects = con_list[now_node.point]
        for c in connects:
            if c[0] not in cost_list:
                cost_list[c[0]] = c[1] + now_node.cost
                node_list.append(point_node(c[0], c[1] + now_node.cost))
        if len(node_list) == 0:
            break
        #node_list = copy.deepcopy(new_node_list)

    return cost_list


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [N] = [int(input_raw[0])]
    pass_dict = {}
    for i in range(N - 1):
        input_raw = read_func().strip().split()
        [a, b, c] = [int(input_raw[0]), int(input_raw[1]), int(input_raw[2])]
        if a not in pass_dict:
            pass_dict[a] = []
        pass_dict[a].append((b, c))
        if b not in pass_dict:
            pass_dict[b] = []
        pass_dict[b].append((a, c))

    input_raw = read_func().strip().split()
    [Q, K] = [int(input_raw[0]), int(input_raw[1])]

    cost_list = BFS(pass_dict, K)

    for i in range(Q):
        input_raw = read_func().strip().split()
        [x, y] = [int(input_raw[0]), int(input_raw[1])]
        print cost_list[x] + cost_list[y]


if __name__ == '__main__':
    main()
