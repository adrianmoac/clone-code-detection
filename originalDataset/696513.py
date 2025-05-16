import heapq
N,A,B=map(int,raw_input().split())
a=map(int,raw_input().split())
m=1000000007

def calc(A,ex,m):
    ret = 1
    mul = A
    while ex!= 0:
        if ex%2 == 1:
            ret*=A
            ret%=m
        A*=A
        A%=m
        ex/=2
    return ret

if A==1:
    a.sort()
    for ans in a:
        print ans
    exit()

MA=max(a)
bi=0
for i in range(N):
    curA=a[i]
    while curA*A < MA:
        curA*=A
        bi+=1

if bi>B:
    heapq.heapify(a)
    for bi in xrange(B):
        n=a[0]
        heapq.heappop(a)
        heapq.heappush(a,n*A)
    for i in range(N):
        print a[0]
        heapq.heappop(a)

else:
    for i in range(N):
        while a[i]*A < MA:
            a[i]*=A
            B-=1
    a.sort()
    ex=B/N
    common=calc(A,ex,m)
    r=B%N
    for i in range(N):
        a[i]*=common
        a[i]%=m
    for i in range(r):
        a[i]*=A
        a[i]%=m
    for i in range(r,N):
        print a[i]
    for i in range(r):
        print a[i]


