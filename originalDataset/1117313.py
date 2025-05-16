#!/usr/bin/env python
# -*- coding: utf-8 -*-

_ = input()
s = input()
# print(s)

a = [None] * len(s)

def neib(p, q, s):
    if q =="S":
        if s=="o":
            return p
        if s=="x":
            if p=="S":
                return "W"
            else:
                return "S"
    if q=="W":
        if s=="x":  # 両隣同じ
            if p=="S":
                return "S"
            else:
                return "W"
        if s=="o":
            if p=="S":
                return "W"
            else:
                return "S"

# aN, a0, a1
def checkans(p, q, r, s):
    pr = p+r
    if q=="S":
        if pr=="SS" or pr=="WW":
            return s=="o"
        if p != r:
            return s=="x"
    if q=="W":
        if pr=="SS" or pr=="WW":
            return s=="x"
        if p!=r:
            return s=="o"


ans = "-1"
for ini in [("S", "S"), ("S", "W"), ("W", "S"), ("W", "W")]:
    a[0], a[1] = ini
    for i in range(1, len(s)-1):
        a[i+1] = neib(a[i-1], a[i], s[i])
    # print("#", ini)
    # print(a)
    c0 = (checkans(a[-2], a[-1], a[0], s[-1]))
    c1 = (checkans(a[-1], a[0], a[1], s[0]) )

    if c0 and c1:
        ans = "".join(a)
        break
print(ans)


        
    

