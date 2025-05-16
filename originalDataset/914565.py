import bisect
import sys
import math
import itertools
import heapq
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
#

def join(s):
    return ''.join(s)

#iterate macro
def piter(n,m):
    return itertools.permutations(n,m)
def citer(n,m):
    return itertools.combinations(n,m)

#modulo macro
def modc(a,b,m):
    c = 1
    for i in xrange(b):
        c = c * (a - i) % m
        c = c * modinv(i + 1,m) % m
    return c
 
def gcd(a, b):
    (x, lastx) = (0, 1)
    (y, lasty) = (1, 0)
    while b != 0:
        q = a // b
        (a, b) = (b, a % b)
        (x, lastx) = (lastx - q * x, x)
        (y, lasty) = (lasty - q * y, y)
    return (lastx, lasty, a)
 
def modinv(a, m):
    (inv, q, gcd_val) = gcd(a, m)
    return inv % m

#bisect macro
def index(a, x):
    #Locate the leftmost value exactly equal to x
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    return -1

#memoize macro
def memoize(f):
    cache = {}
    def helper(*args):
        if args not in cache:
            cache[(args)] = f(*args)
        return cache[args]
    return helper

@memoize
def nck(a,b,m):
    b = min([a-b,b])
    if (b>a or b<0 or a<0):
        return 0
    elif a == 0:
        return 1
    return (nck(a-1,b-1,m)+nck(a-1,b,m)) % m

nh=zip([1,0,-1,0],[0,1,0,-1])

###########

n,m,t = ii()
money = ii()

path = [[] for j in range(n)]
cost = [(INF,j) for j in range(n)]
cost[0] = (0,0)
time = [INF]*n
end = [False]*n

pathinv = [[] for j in range(n)]
costinv = [(INF,j) for j in range(n)]
costinv[0] = (0,0)
timeinv = [INF]*n
endinv = [False]*n

heapq.heapify(cost)
heapq.heapify(costinv)

#input
for j in range(m):
    a,b,c = ii()
    path[a-1].append((b-1,c))
    pathinv[b-1].append((a-1,c))


while(len(cost)!=0):
    dist,cur=heapq.heappop(cost)
    if not end[cur]:
        end[cur]=True
        time[cur]=dist
        for b,c in path[cur]:
            if not end[b]:
                heapq.heappush(cost,(dist+c,b))

while(len(costinv)!=0):
    dist,cur=heapq.heappop(costinv)
    if not endinv[cur]:
        endinv[cur]=True
        timeinv[cur]=dist
        for b,c in pathinv[cur]:
            if not endinv[b]:
                heapq.heappush(costinv,(dist+c,b))

ans=0
for j in range(n):
    earn=(t-time[j]-timeinv[j])*money[j]
    if ans<earn:
        ans=earn

print ans
