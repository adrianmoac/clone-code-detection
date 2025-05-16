import bisect
import sys
import math
import itertools
sys.setrecursionlimit(10000)

INF = float('inf')

# input macro
def i():
    return int(raw_input())
def ii():
    return map(int,raw_input().split(" "))
def s():
    return raw_input()
def ss():
    return raw_input().split(" ")
def slist():
    return list(raw_input())
def join(s):
    return ''.join(s)

#memoize macro
def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[(args)] = f(*args)
        return cache[args]
    return helper

nh=zip([1,0,-1,0],[0,1,0,-1])
mod=1000000007

###########

n=i()
x=[]
y=[]
for j in range(n):
    a,b=ii()
    if a<b:
        x.append([a,b])
    else:
        y.append([b,a])
x.sort()
y.sort()
y.reverse()

cur=0
mx=0
for a,b in x:
    cur+=a
    mx=max(mx,cur)
    cur-=b
for b,a in y:
    cur+=a
    mx=max(mx,cur)
    cur-=b

print mx
