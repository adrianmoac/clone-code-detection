import numpy as np
import sys
import itertools

def read_data():
    try:
        LOCAL_FLAG
        import codecs
        import os

        lines = []
        file_path = os.path.join(os.path.dirname(__file__), 'data073.dat')
        with codecs.open(file_path, 'r', 'utf-8') as f:
            lines.append(f.readline().rstrip("\r\n"))
            N, M, R = list(map(int, lines[0].split()))
            for i in range(M+1):
                lines.append(f.readline().rstrip("\r\n"))


    except NameError:
        lines = []
        lines.append(input())
        N, M, R = list(map(int, lines[0].split()))
        for i in range(M+1):
            lines.append(input())

    return lines

def dis(D, town_list):
    total = 0
    for i in range(len(town_list)-1):
        total += D[town_list[i]][town_list[i+1]]
    return total


def Travel():

    raw_data = read_data()
    N, M, R = list(map(int, raw_data[0].split()))
    town_list = list(map(int, raw_data[1].split()))
    road_set = set([])

    MAX = 200000
    # D = np.zeros((N+1, N+1), dtype='int32')
    # D += MAX
    D = [[float('inf')]*(N+1) for _ in range(N+1)]


    for i in range(2, M+2):
        a, b, c = list(map(int, raw_data[i].split()))
        D[a][b] = c
        D[b][a] = c

    # for i in range(1, N+1):
    #     for j in range(1, N+1):
    #         dis_two_node = np.min(D[i] + D[j])
    #         if dis_two_node < D[i,j]:
    #             D[i,j] = dis_two_node
    #             D[j,i] = dis_two_node

    # for i in range(N+1):
    #     D[i][i] = 0

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                dis_two_node = D[i][k] + D[k][j]
                if dis_two_node < D[i][j]:
                    D[i][j] = dis_two_node
                    D[j][i] = dis_two_node

   
    min_dis = float('inf')
    for each in itertools.permutations(town_list):
        min_dis = min(dis(D, each), min_dis)

    print(min_dis)




Travel()
