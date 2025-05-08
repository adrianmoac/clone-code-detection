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

###########

def q(t):
    if max([x[i]-t/c[i] for i in range(n)])>min([x[i]+t/c[i] for i in range(n)]) or max([y[i]-t/c[i] for i in range(n)])>min([y[i]+t/c[i] for i in range(n)]):
        return False
    return True
        
n=i()
x,y,c = [0]*n,[0]*n,[0]*n
for i in range(n):
    x[i],y[i],c[i] = ii()
t1=0.00
t2=max([max(x)-min(x),max(y)-min(y)])*max(c)
for cnt in range(256):
    if q((t1+t2)/2):
        t1,t2=t1,(t1+t2)/2
    else:
        t1,t2=(t1+t2)/2,t2
print (t1+t2)/2
