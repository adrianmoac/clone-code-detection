import numpy as np
import itertools
import heapq
import collections


class treasure(object):

    def __init__(self, n, times):
        self.path = collections.defaultdict(dict)
        self.path_r = collections.defaultdict(dict)
        self.n = n
        self.times = times
        self.earn = None
        self.big_number = float('inf')

    def store_minimum_path(self, path):
        self.path[path[0]][path[1]] = path[2]
        self.path_r[path[1]][path[0]] = path[2]

    def store_money(self, earn):
        self.earn = np.array(earn)

    def dijk(self, start, n, tree):
        cost = [self.big_number] * n
        cost[start] = 0
        stack = [[0, start]]
        while len(stack):
            c, index = heapq.heappop(stack)
            try:
                for key in tree[index]:
                    tmp_cost = c + tree[index][key]
                    if tmp_cost <= cost[key]:
                        cost[key] = tmp_cost
                        heapq.heappush(stack, [tmp_cost, key])
            except KeyError:
                pass
        return np.array(cost)

    def calc_around(self, start, n):
        return self.dijk(0, self.n, self.path) + self.dijk(0, self.n, self.path_r)

    def calc_all(self, start, n):
        distance = self.calc_around(start, n)
        return tre.earn * (tre.times - distance)

    def beam_search(self, start, end, depth=5):
        if start in self.path and end in self.path[start]:
            return self.path[start][end]
        minimum_value = self.big_number
        stack = [[0, start]]
        answer = self.big_number
        while bool(len(stack)):
            tmp_stack = []
            for _ in range(depth):
                if len(stack) == 0:
                    break
                tmp = heapq.heappop(stack)
                if tmp[0] >= minimum_value:
                    break
                if tmp[-1] in self.path:
                    for key in self.path[tmp[-1]]:
                        value = tmp[0] + self.path[tmp[-1]][key]
                        if key == end:
                            if minimum_value >= value:
                                answer = value
                                minimum_value = value
                        else:
                            if minimum_value >= value and key not in tmp[1:]:
                                tmp_stack.append([value] + tmp[1:] + [key])
            for ele in tmp_stack:
                heapq.heappush(stack, ele)
        return answer

    def look_for_minimum_path(self, start, end, depth=5):
        if start in self.path and end in self.path[start]:
            return [start, end, self.path[start][end]]
        answer = []
        answer_value = []
        process = [[start]]
        process_value = [[0]]
        min_value = self.big_number
        for _ in range(depth):
            tmp_process_p = []
            tmp_process_v = []
            for p, v in zip(process, process_value):
                value = v[-1]
                if p[-1] in self.path:
                    for key in self.path[p[-1]].keys():
                        tmp_value = value + self.path[p[-1]][key]
                        if min_value >= tmp_value:
                            tmp_p = p[:] + [key]
                            tmp_v = v[:] + [tmp_value]
                            if key == end:
                                answer = tmp_p
                                answer_value = tmp_v
                                min_value = tmp_value
                            elif len(tmp_p) == len(set(tmp_p)):
                                tmp_process_p.append(tmp_p)
                                tmp_process_v.append(tmp_v)
            process = tmp_process_p[:]
            process_value = tmp_process_v[:]
            if len(process) == 0:
                if len(answer) == 0:
                    return [start, self.big_number]
                else:
                    self.register_path(answer, answer_value)
                    return answer + [answer_value[-1]]
        if len(answer) == 0:
            return [start, self.big_number]
        else:
            self.register_path(answer, answer_value)
            return answer + [answer_value[-1]]

    def register_path(self, answer, answer_value):
        branch = []
        for i, ii in itertools.combinations(range(len(answer)), 2):
            branch.append([answer[i], answer[ii], answer_value[ii] - answer_value[i]])
        self.store_minimum_path(branch)

    def calculate_earn(self, start, end, depth):
        if start == end:
            return self.times * self.earn[end]
        min_go = self.big_number
        min_back = self.big_number
        # go = min(self.look_for_minimum_path(start, end, depth=depth)[-1], min_go)
        go = min(self.beam_search(start, end, depth=depth), min_go)
        if go == self.big_number:
            return -1
        self.store_minimum_path([start, end, go])
        # back = min(self.look_for_minimum_path(end, start, depth=depth)[-1], min_back)
        back = min(self.beam_search(end, start, depth=depth), min_back)
        if back == self.big_number:
            return -1
        self.store_minimum_path([end, start, back])
        residue = self.times - go - back
        return residue * self.earn[end]

N, M, T = map(int, raw_input().split())
tre = treasure(N,T)
tre.store_money(map(int, raw_input().split()))
for _ in range(M):
    a,b,c = map(int, raw_input().split())
    tre.store_minimum_path([a-1,b-1,c])
print(int(np.max(tre.calc_all(0,tre.n))))