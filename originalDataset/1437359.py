import sys
from collections import deque
import copy

from math import *
def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline

class mas_node():
    def __init__(self, now_number, pass_route):
        self.now_number = now_number
        self.pass_route = set(pass_route)
        self.pass_route.add(now_number)

    def set_now_number(self, now_number):
        self.now_number = now_number
        self.pass_route.add(now_number)

def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [N] = [int(input_raw[0])]

    adj_list = {}
    for i in range(N):
        adj_list[i + 1] = []

    for i in range(N - 1):
        input_raw = list(read_func().strip().split())
        adj_list[int(input_raw[0])].append(int(input_raw[1]))
        adj_list[int(input_raw[1])].append(int(input_raw[0]))


    #node_list = [mas_node(1, [])]
    is_already_pass = [False] * N
    is_already_pass[0] = True
    node_list = [1]
    count = 0
    while 1:
        #count += 1
        #print count
        #new_node_list = []
        m_node = node_list[len(node_list) - 1]
        is_already_pass[m_node - 1] = True
        is_leaf_node = True
        if m_node == N:
            break;
        for next_node in adj_list[m_node]:
            if is_already_pass[next_node - 1] == False:
                is_leaf_node = False
                node_list.append(next_node)
        if is_leaf_node == True:
            node_list.pop()
        if len(node_list) == 0:
            break;

    to_N_pass_route = deque([])
    for i in range(len(node_list)):
        if is_already_pass[node_list[i] - 1] == True:
            to_N_pass_route.append(node_list[i])


    to_N_pass_route.popleft()
    to_N_pass_route.pop()
    already_colored_list = [False] * N
    mas_set = {}
    mas_set["b"] = [1]
    mas_set["w"] = [N]
    pass_len = len(to_N_pass_route)

    #print to_N_pass_route
    for i in range(pass_len):
        if len(to_N_pass_route) == 0:
            break;
        b = to_N_pass_route.popleft()
        already_colored_list[b - 1] = True
        mas_set["b"].append(b)
        if len(to_N_pass_route) == 0:
            break;
        w = to_N_pass_route.pop()
        already_colored_list[w - 1] = True
        mas_set["w"].append(w)

    black_mas_node = copy.deepcopy(mas_set["b"])
    white_mas_node = copy.deepcopy(mas_set["w"])
    while 1:
        new_black_mas_node = []
        for b_mas in black_mas_node:
            for next_b_mas in adj_list[b_mas]:
                if already_colored_list[next_b_mas - 1] == False:
                    mas_set['b'].append(next_b_mas)
                    new_black_mas_node.append(next_b_mas)
                    already_colored_list[next_b_mas - 1] = True
        black_mas_node = copy.deepcopy(new_black_mas_node)

        new_white_mas_node = []
        for w_mas in white_mas_node:
            for next_w_mas in adj_list[w_mas]:
                if already_colored_list[next_w_mas - 1] == False:
                    mas_set['w'].append(next_w_mas)
                    new_white_mas_node.append(next_w_mas)
                    already_colored_list[next_w_mas - 1] = True
        white_mas_node = copy.deepcopy(new_white_mas_node)

        if len(white_mas_node) == 0 & len(black_mas_node) == 0:
            break;

    if len(mas_set['b']) > len(mas_set['w']):
        print "Fennec"
    else:
        print "Snuke"



if __name__ == '__main__':
    main()