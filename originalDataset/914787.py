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
    a,b=max(a,b),min(a,b)
    if a%b==0:
        return b
    else:
        return gcd(b,a%b)
 
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

a,b,m=ii()
c=gcd(a,b)
mod=m

@memoize
def tens(x):
    if x==1:
        return 10%mod
    elif x%2==0:
        return tens(x/2)**2%mod
    else:
        return tens(x/2)**2*10%mod

@memoize
def ones(x):
    if x==1:
        return 1
    elif x%2==0:
        return (tens(x/2)*ones(x/2)+ones(x/2))%mod
    else:
        return (tens(x/2+1)*ones(x/2)+ones(x/2+1))%mod

@memoize
def zones(x):
    if x==1:
        return 1
    elif x%2==0:
        return (zones(x/2)*tens(x*c/2)+zones(x/2))%mod
    else:
        return (zones(x/2)*tens((x+1)*c/2)+zones((x+1)/2))%mod

print zones(a/c)*ones(b)%mod
