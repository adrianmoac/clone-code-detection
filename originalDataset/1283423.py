import sys

stdin = sys.stdin


def na(): return map(int, stdin.readline().split())


def ns(): return stdin.readline().strip()

def bf(es, n, start, ved):
    I = 999999999999999999
    d = [I] * n
    d[start] = 0

    for i in range(n-1):
        updated = False
        for e in es:
            if not ved[e[0]]: continue
            if not ved[e[1]]: continue
            if d[e[0]] + e[2] < d[e[1]]:
                d[e[1]] = d[e[0]] + e[2]
                updated = True
        if not updated: break
    for e in es:
        if not ved[e[0]]: continue
        if not ved[e[1]]: continue
        if d[e[0]] + e[2] < d[e[1]]:
            return None
    return d

def go(start, g, ind):
    n = len(g)
    ved = [False] * n
    q = [start]
    j = 0
    ved[start] = True
    while(j < len(q)):
        cur = q[j]
        for e in g[cur]:
            if not ved[e[ind]]:
                ved[e[ind]] = True
                q.append(e[ind])
        j += 1
    return ved

n,m = na()
es = []

for i in range(m):
    a,b,c = na()
    es.append([a-1,b-1,-c])

g = [[] for _ in range(n)]
for e in es:
    g[e[0]].append(e)

ig = [[] for _ in range(n)]
for e in es:
    ig[e[1]].append(e)


ved = go(0, g, 1)
ived = go(n-1, ig, 0)

for i in range(n):
    ved[i] &= ived[i]

res = bf(es, n, 0, ved)
if res:
    print(-res[n-1])
else:
    print("inf")