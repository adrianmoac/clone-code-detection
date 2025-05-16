#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from itertools import *
import random

S_input = input()
def greedy(S):
    stack = 0
    score = 0
    debug = []
    for ch in S:
        my = ''
        if stack == 0:
            my = 'g'
            stack += 1
        else:
            my = 'p'
            stack -= 1

        debug.append(my)
        if my == 'g' and ch == 'p':
            score -= 1
        elif my == 'p' and ch == 'g':
            score += 1
    # print("myans:",debug)
    return max(score,0)

# def bf(S):
#     leng = len(S)
#     ret = 0
#     best = ""
#     for comb in product("gp", repeat=leng):
#         g_num = 0
#         valid = True
#         for ch in comb:
#             if ch == 'g':
#                 g_num += 1
#             else:
#                 g_num -= 1
#             if g_num < 0:
#                 valid = False
#                 break
#         if not valid:
#             continue


#         score = 0
#         for ch,my in zip(S,comb):
#             if my == 'g' and ch == 'p':
#                 score -= 1
#             elif my == 'p' and ch == 'g':
#                 score += 1
#         if score > ret:
#             ret = score
#             best = comb

#     # print("bf:",best)
#     return ret

# def main():

#     while True:
#         # q = "gggggp"

#         q = []
#         g_num = 0
#         for i in range(6):
#             if g_num == 0:
#                 q.append('g')
#                 g_num += 1
#             else:
#                 tmp = random.choice("gp")
#                 q.append(tmp)
#                 if tmp == 'g':
#                     g_num += 1
#                 else:
#                     g_num -= 1

#         ans1 = greedy(q)
#         ans2 = bf(q)
#         if ans1 != ans2:
#             print("q:", q)
#             print("ans1:",ans1)
#             print("ans2:",ans2)
        
# main()

print(greedy(S_input))

