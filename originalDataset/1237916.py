import sys
import math

INF = 10**9+7

def k(i):
    if(i == 1):
        return 1
    else:
        return(i * k(i-1))

def comb(n, r):
    if(n == r or r == 1):
        return 1
    else:
        return k(n) / (k(n-r) * k(r))

stdin = sys.stdin
def na(): return map(int, stdin.readline().split())
def ns(): return stdin.readline().strip()
def nsl(): return list(stdin.readline().strip())
def ni(): return int(stdin.readline())
def nil(): return list(map(int, stdin.readline().split()))

n = ni()
a = nil()

b = []

for i in range(n):
    b.append(a[i])


sum = 0

c1 = 0
c2 = 0

if a[0] == 0:
    a[0] = 1
    c1 += 1;

for i in range(0, n-1):
    sum += a[i]

    sum2 = sum + a[i+1]

    if sum2 == 0:
        if sum >0:
            a[i+1] -= 1
            sum2 -= 1
            c1 +=1

    if(sum * sum2 >= 0):
        k = abs(sum2) + 1

        h = k - (abs(sum) - 1)
        l = k - h

        if sum > 0 :
            a[i] -= l
            sum -= l
            a[i + 1] -= h
        else:
            a[i] += l
            sum += l
            a[i + 1] += h

        c1 += h+l


sum = 0

a = b

if a[0] == 0:
    a[0] = -1
    c2 += 1;
else:
    c2 = abs(a[0]) + 1
    if a[0] > 0:
        a[0] = -1
    else:
        a[0] = 1

for i in range(0, n-1):
    sum += a[i]

    sum2 = sum + a[i+1]

    if sum2 == 0:
        if sum >0:
            a[i+1] -= 1
            sum2 -= 1
            c2 +=1

    if(sum * sum2 >= 0):
        k = abs(sum2) + 1

        h = k - (abs(sum) - 1)
        l = k - h

        if sum > 0 :
            a[i] -= l
            sum -= l
            a[i + 1] -= h
        else:
            a[i] += l
            sum += l
            a[i + 1] += h

        c2 += k

print(min(c1, c2))




