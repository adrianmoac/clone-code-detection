# -*- coding: utf-8 -*-
import numpy as np

LINE_NUM = 9
ANSWER_NUM = 4

inpData = raw_input().split()
x = int(inpData[0])-1
y = int(inpData[1])-1
W = inpData[2]
c = np.zeros((LINE_NUM, LINE_NUM), dtype = int)
answer = np.zeros(ANSWER_NUM, dtype = int)

for i in range(LINE_NUM):
    inpNum = raw_input()

    for j in range(LINE_NUM):
        c[i][j] = int(inpNum[j])

#print c
for i in range(ANSWER_NUM):
    answer[i] = c[y][x]

    if W == "R":
        if x == LINE_NUM-1:
            x = LINE_NUM-2
            W = "L"
        else:
            x += 1

    elif W == "L":
        if x == 0:
            x = 1
            W = "R"
        else:
            x -= 1

    elif W == "U":
        if y == 0:
            y = 1
            W = "D"
        else:
            y -= 1

    elif W == "D":
        if y == LINE_NUM-1:
            y = LINE_NUM-2
            W = "U"
        else:
            y += 1

    elif W == "RU":
        if x == LINE_NUM-1 and y == 0:
            x = LINE_NUM-2
            y = 1
            W = "LD"
        elif x == LINE_NUM-1:
            x = LINE_NUM-2
            y -= 1
            W = "LU"
        elif y == 0:
            x += 1
            y = 1
            W = "RD"
        else:
            x += 1
            y -= 1

    elif W == "RD":
        if x == LINE_NUM-1 and y == LINE_NUM-1:
            x = LINE_NUM-2
            y = LINE_NUM-2
            W = "LU"
        elif x == LINE_NUM-1:
            x = LINE_NUM-2
            y += 1
            W = "LD"
        elif y == LINE_NUM-1:
            x += 1
            y = LINE_NUM-2
            W = "RU"
        else:
            x += 1
            y += 1

    elif W == "LU":
        if x == 0 and y == 0:
            x = 1
            y = 1
            W = "RD"
        elif x == 0:
            x = 1
            y -= 1
            W = "RU"
        elif y == 0:
            x -= 1
            y = 1
            W = "LD"
        else:
            x -= 1
            y -= 1

    elif W == "LD":
        if x == 0 and y == LINE_NUM-1:
            x = 1
            y = LINE_NUM-2
            W = "RU"
        elif x == 0:
            x = 1
            y += 1
            W = "RD"
        elif y == LINE_NUM-1:
            x -= 1
            y = LINE_NUM-2
            W = "LU"
        else:
            x -= 1
            y += 1
print "%d%d%d%d" % (answer[0], answer[1], answer[2], answer[3])
