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
s=[[] for j in range(n)]
for j in range(n):
    s[j]=map(int,slist())
det=1
for j in range(n-1):
    x=s[j][j]
    if x==0:
        for z in range(j+1,n):
            if s[z][j]!=0:
                for m in range(n):
                    s[j][m],s[z][m]=s[z][m],s[j][m]
                break
        else:
            print "Even"
            sys.exit()
    x=s[j][j]
    det=det*x%2
    for k in range(j+1,n):
        y=s[k][j]
        if y!=0:
            for l in range(n):
                s[k][l]=(s[k][l]*x-s[j][l]*y)%2

ans=det
for j in range(n):
    ans=ans*s[j][j]%2

if ans%2==0:
    print "Even"
else:
    print "Odd"
