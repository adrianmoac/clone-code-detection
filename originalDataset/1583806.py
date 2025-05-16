import copy
import sys
import numpy as np
import heapq

from math import *
def get_read_func(fileobject):
    if fileobject == None :
        return raw_input
    else:
        return fileobject.readline

class node_cost:
    def __init__(self, point, cost):
        self.point = point
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

class Dijkstra:
    def __init__(self):
        self.table = {}

    def execute(self, adj_list, start):
        confirm_set = set()
        cost_dict = {}
        cost_dict[start] = 0
        #heapq.heapify

        n = node_cost(start, 0)
        node_list = [n]
        while len(node_list) > 0:
            n = heapq.heappop(node_list)
            if n.point in confirm_set:
                continue;
            confirm_set.add(n.point)
            self.table[(start, n.point)] = n.cost
            #self.table[(n.point, start)] = n.cost
            for v in adj_list[n.point]:
                if v[0] not in confirm_set:
                    if v[0] not in cost_dict:
                        cost_dict[v[0]] = n.cost + v[1]
                        heapq.heappush(node_list, node_cost(v[0], cost_dict[v[0]]))
                    else:
                        if n.cost + v[1] < cost_dict[v[0]]:
                            cost_dict[v[0]] = n.cost + v[1]
                            heapq.heappush(node_list, node_cost(v[0], cost_dict[v[0]]))

class DFS:
    def __init__(self, visitable_list, cost_table):
        self.visitable_list = visitable_list
        self.cost_table = cost_table
        self.done_list = set([])
        self.min_cost = sys.maxint

    def execute(self, now_cost, now_v):
        if len(self.done_list) == len(self.visitable_list):
            if now_cost < self.min_cost:
                self.min_cost = now_cost
            return

        for v in self.visitable_list:
            if v not in self.done_list:
                self.done_list.add(v)
                if now_v == 0:
                    self.execute(0, v)
                else:
                    self.execute(now_cost + self.cost_table[(now_v, v)], v)
                self.done_list.remove(v)




def main():
    if len(sys.argv) > 1:
        f = open(sys.argv[1])
    else:
        f = None
    read_func = get_read_func(f);
    input_raw = read_func().strip().split()
    [N, M, R] = [int(input_raw[0]), int(input_raw[1]), int(input_raw[2])]
    input_raw = read_func()
    input_str = input_raw.strip().split()
    visit_list = []
    for i in range(R):
        visit_list.append(int(input_str[i]))

    adj_list = {}
    for i in range(M):
        input_raw = read_func().strip().split()
        [A, B, C] = [int(input_raw[0]), int(input_raw[1]), int(input_raw[2])]
        if A not in adj_list:
            adj_list[A] = []
        if B not in adj_list:
            adj_list[B] = []
        adj_list[A].append((B, C))
        adj_list[B].append((A, C))


    D = Dijkstra()
    for v in visit_list:
        D.execute(adj_list, v)
    #print D.table

    dfs = DFS(visit_list, D.table)
    dfs.execute(0, 0)
    print dfs.min_cost

if __name__ == '__main__':
    main()