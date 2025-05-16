# -*- coding: utf-8 -*-
N = int(input())
a = [int(n) for n in input().split()]

count_a = 0 #+start
count_b = 0 #-start

nowsum = a[0]
if nowsum != 0:
    for n in range(1, N):
        if nowsum * (nowsum + a[n]) >= 0:
            count_a += abs(nowsum + a[n]) + 1
            if nowsum < 0:
                nowsum = 1
            else:
                nowsum = -1
        else:
            nowsum += a[n]

    count_b += abs(a[0]) + 1
    nowsum = int(a[0] / abs(a[0]) * -1)

    for n in range(1, N):
        if nowsum * (nowsum + a[n]) >= 0:
            count_b += abs(nowsum + a[n]) + 1
            if nowsum < 0:
                nowsum = 1
            else:
                nowsum = -1
        else:
            nowsum += a[n] 

    print(min(count_a, count_b))

else:
    a[0] = 1
    count_a += 1
    nowsum = 1
    for n in range(1, N):
        if nowsum * (nowsum + a[n]) >= 0:
            count_a += abs(nowsum + a[n]) + 1
            if nowsum < 0:
                nowsum = 1
            else:
                nowsum = -1
        else:
            nowsum += a[n]
    
    a[0] = -1
    count_b += 1
    nowsum = -1
    for n in range(1, N):
        if nowsum * (nowsum + a[n]) >= 0:
            count_b += abs(nowsum + a[n]) + 1
            if nowsum < 0:
                nowsum = 1
            else:
                nowsum = -1
        else:
            nowsum += a[n]   
    print(min(count_a, count_b))
            

