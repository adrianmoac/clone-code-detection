#! /usr/bin/python
# -*- coding:utf-8 -*-

N = int(raw_input())
s = raw_input()

res = -1
maru = 0
batsu = 0

for i in range(N):
    if s[i] == 'o':
        maru += 1
    else:
        batsu += 1
#print maru, batsu

revers = {'S':'W', 'W':'S'}
res = ''
patterns = ['SS', 'SW', 'WS', 'WW']

for pattern in patterns:
    res = ''
    flg = 0
    flg2 = 0
    res += pattern
    for i in range(2, N,1):
        if res[i-1] == 'S':
            if s[i-1] == 'o':
                res += res[i-2]
            else:
                res += revers[res[i-2]]
        else:
            if s[i-1] == 'o':
                res += revers[res[i-2]]
            else:
                res += res[i-2]
    if res[0] == 'S':
        if s[0] == 'o':
            if res[-1] == res[1]:
                flg = 1
        else:
            if res[-1] != res[1]:
                flg = 1
    else:
        if s[0] == 'o':
            if res[-1] != res[1]:
                flg = 1
        else:
            if res[-1] == res[1]:
                flg = 1

    if res[-1] == 'S':
        if s[-1] == 'o':
            if res[-2] == res[0]:
                flg2 = 1
        else:
            if res[-2] != res[0]:
                flg2 = 1
    else:
        if s[-1] == 'o':
            if res[-2] != res[0]:
                flg2 = 1
        else:
            if res[-2] == res[0]:
                flg2 = 1

    if flg == 1 and flg2 == 1:
        break

if flg == 0 or flg2 ==0:
    print -1
else:
    print res