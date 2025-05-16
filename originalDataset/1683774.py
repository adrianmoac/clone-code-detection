#! -*- coding:utf-8 -*-
import sys
h,w = map(int,input().split())
S = []
for i in range(h):
    S.append(str(input()))
arr = [[]*w]*h

for i in range(h):
    arr[i] = list(S[i])

if h == 1 and w == 1:
    if arr[0][0] == '#':
        print('#')
    else:
        print(0)
    sys.exit()
elif h == 1:
    for i in range(w):
        c = 0
        if arr[0][i] == '#':
            print('#',sep ='',end = '')
        elif i == 0:
            if arr[0][1] == '#':
                c += 1
            print(c,sep = '', end = '')
        elif i == w-1:
            if arr[0][-2] == '#':
                c += 1
            print(c,sep = '', end = '')
        else:
            if arr[0][i-1] == '#':
                c += 1
            if arr[0][i+1] == '#':
                c += 1
            print(c,sep = '',end = '')
    print('')
    sys.exit()
elif w == 1:
    for i in range(h):
        c = 0
        if arr[i][0] == '#':
            print('#')
        elif i == 0:
            if arr[1][0] == '#':
                c += 1
            print(c)
        elif i == h-1:
            if arr[-2][0] == '#':
                c += 1
            print(c)
        else:
            if arr[i-1][0] == '#':
                c += 1
            if arr[i+1][0] == '#':
                c += 1
            print(c)
    sys.exit()
    
for i in range(h):
    for j in range(w):
        if arr[i][j] == '#':
            print('#',sep = '', end = '')
        else:
            if i == 0 and j == 0:
                c = 0
                if arr[0][1] == '#':
                    c += 1
                if arr[1][0] == '#':
                    c += 1
                if arr[1][1] == '#':
                    c += 1
                print(c,sep = '', end = '')
            elif i == 0 and j == w-1:
                c = 0
                if arr[0][-2] == '#':
                    c += 1
                if arr[1][-1] == '#':
                    c += 1
                if arr[1][-2] == '#':
                    c += 1
                print(c,sep = '', end = '')
            elif i == 0:
                c = 0
                if arr[i][j-1] == '#':
                    c+= 1
                if arr[i][j+1] == '#':
                    c +=1
                if arr[i+1][j-1] == '#':
                    c += 1
                if arr[i+1][j] == '#':
                    c += 1
                if arr[i+1][j+1] == '#':
                    c += 1
                print(c,sep = '', end = '')
            elif i == h-1 and j == 0:
                c = 0
                if arr[-1][1] == '#':
                    c += 1
                if arr[-2][0] == '#':
                    c += 1
                if arr[-2][1] == '#':
                    c += 1
                print(c,sep = '', end = '')
            elif i == h-1 and j == w-1:
                c = 0
                if arr[-1][-2] == '#':
                    c += 1
                if arr[-2][-1] == '#':
                    c += 1
                if arr[-2][-2] == '#':
                    c += 1
                print(c,sep = '', end = '')
            elif i == h-1:
                c = 0
                if arr[i][j-1] == '#':
                    c+= 1
                if arr[i][j+1] == '#':
                    c +=1
                if arr[i-1][j-1] == '#':
                    c += 1
                if arr[i-1][j] == '#':
                    c += 1
                if arr[i-1][j+1] == '#':
                    c += 1
                print(c,sep = '', end = '')
            elif j == 0:
                c = 0
                if arr[i-1][j] == '#':
                    c += 1
                if arr[i+1][j] == '#':
                    c += 1
                if arr[i][j+1] == '#':
                    c += 1
                if arr[i-1][j+1] == '#':
                    c += 1
                if arr[i+1][j+1] == '#':
                    c += 1
                print(c,sep = '', end = '')
            elif j == w-1:
                c = 0
                if arr[i-1][j] == '#':
                    c += 1
                if arr[i+1][j] == '#':
                    c += 1
                if arr[i][j-1] == '#':
                    c += 1
                if arr[i-1][j-1] == '#':
                    c += 1
                if arr[i+1][j-1] == '#':
                    c += 1
                print(c,sep = '', end = '')
            else:
                c = 0
                if arr[i-1][j-1] == '#':
                    c += 1
                if arr[i-1][j] == '#':
                    c += 1
                if arr[i-1][j+1] == '#':
                    c += 1
                if arr[i][j-1] == '#':
                    c += 1
                if arr[i][j+1] == '#':
                    c += 1
                if arr[i+1][j-1] == '#':
                    c += 1
                if arr[i+1][j] == '#':
                    c += 1
                if arr[i+1][j+1] == '#':
                    c += 1
                print(c,sep = '', end = '')
    print('')
