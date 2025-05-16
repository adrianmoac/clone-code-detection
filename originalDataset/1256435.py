# -*- coding: utf-8 -*-
import numpy as np

LINE_NUM = 9
ANSWER_NUM = 4

inpData = raw_input().split()
x = int(inpData[0])-1
y = int(inpData[1])-1
W = inpData[2]
c = np.zeros((LINE_NUM, LINE_NUM), dtype = int)
xd = 0
yd = 0
answer = np.zeros(ANSWER_NUM, dtype = int)

for i in range(LINE_NUM):
    inpNum = raw_input()

    for j in range(LINE_NUM):
        c[i][j] = int(inpNum[j])

# 方向決め
if W == "R":
    xd = 1
    yd = 0
elif W == "L":
    xd = -1
    yd = 0
elif W == "U":
    xd = 0
    yd = -1
elif W == "D":
    xd = 0
    yd = 1
elif W == "RU":
    xd = 1
    yd = -1
elif W == "RD":
    xd = 1
    yd = 1
elif W == "LU":
    xd = -1
    yd = -1
elif W == "LD":
    xd = -1
    yd = 1

# 矢印方向に動かす
for i in range(ANSWER_NUM):
    answer[i] = c[y][x]

    if x == LINE_NUM-1 and xd == 1:
        xd = -1
    elif x == 0 and xd == -1:
        xd = 1

    if y == LINE_NUM-1 and yd == 1:
        yd = -1
    elif y == 0 and yd == -1:
        yd = 1

    x += xd
    y += yd

print "%d%d%d%d" % (answer[0], answer[1], answer[2], answer[3])
