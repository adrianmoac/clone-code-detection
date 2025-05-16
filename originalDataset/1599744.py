import sys
from collections import deque
import copy

from math import *

def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline

class water_node():
    def is_meltable(self):
        if self.sugar <= self.water * self.meltable/100:
            return True
        return False
    def __init__(self, water, sugar, meltable):
        self.water = water
        self.sugar = sugar
        self.mass = water + sugar
        self.meltable = meltable
        self.is_all_melt = self.is_meltable()
        if self.sugar + self.water > 0:
            self.concentration = self.sugar * 100.0 /float(self.sugar + self.water)
        else:
            self.concentration = -1.0


    def __eq__(self,other):
        return (self.water  == other.water) and (self.sugar  == other.sugar)

    def __hash__(self):

        return hash (self.water + self.sugar* 10000)


def BFS(A, B, C, D, E, F):
    n = water_node(0, 0, E)
    done_set = set([n])
    node_list = deque([n])
    max_concentration_node = n
    while len(node_list) > 0:
        n = node_list.popleft()
        #ope1
        new_node_list = []
        new_node_list.append(water_node(n.water + A * 100, n.sugar, E))
        new_node_list.append(water_node(n.water + B * 100, n.sugar, E))
        new_node_list.append(water_node(n.water, n.sugar + C, E))
        new_node_list.append(water_node(n.water, n.sugar + D, E))
        for new_node in new_node_list:
            if new_node.mass <= F:
                if new_node not in done_set:
                    done_set.add(new_node)
                    node_list.append(new_node)
                    if new_node.is_all_melt == True and new_node.concentration > max_concentration_node.concentration:
                        max_concentration_node = new_node
    return max_concentration_node


def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [A, B, C, D, E, F] = [int(input_raw[0]), int(input_raw[1]), int(input_raw[2]), int(input_raw[3]), int(input_raw[4]), int(input_raw[5])]
    max_c = BFS(A, B, C, D, E, F)
    print int(max_c.mass), int(max_c.sugar)

if __name__ == '__main__':
    main()
