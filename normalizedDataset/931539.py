#!/usr/bin/env python3
#-*-coding: utf-8-*-from itertools import*import random

id0=input()
def id1(id2):
    id3=0
    id4=0
    id5=[]
    for id6 in id2:
        id7=""
        if id3==0:
            id7="g"
            id3+=1
        else:
            id7="p"
            id3-=1

        id5.id8(id7)
        if id7=="g" and id6=="p":
            id4-=1
        elif id7=="p" and id6=="g":
            id4+=1
    # print("myans:",debug)
    return id9(id4,0)

# def bf(S):
#     leng=len(S)
#     ret=0
#     best=""
#     for comb in product("gp", repeat=leng):
#         g_num=0
#         valid=True
#         for ch in comb:
#             if ch=='g':
#                 g_num+=1
#             else:
#                 g_num-=1
#             if g_num<0:
#                 valid=False
#                 break
#         if not valid:
#             continue


#         score=0
#         for ch,my in zip(S,comb):
#             if my=='g' and ch=='p':
#                 score-=1
#             elif my=='p' and ch=='g':
#                 score+=1
#         if score>ret:
#             ret=score
#             best=comb

#     # print("bf:",best)
#     return ret

# def main():

#     while True:
#         # q="gggggp"

#         q=[]
#         g_num=0
#         for i in range(6):
#             if g_num==0:
#                 q.append('g')
#                 g_num+=1
#             else:
#                 tmp=random.choice("gp")
#                 q.append(tmp)
#                 if tmp=='g':
#                     g_num+=1
#                 else:
#                     g_num-=1

#         ans1=greedy(q)
#         ans2=bf(q)
#         if ans1!=ans2:
#             print("q:", q)
#             print("ans1:",ans1)
#             print("ans2:",ans2)
        
# main()

print(id1(id0))
