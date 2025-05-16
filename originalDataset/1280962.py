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


n,m = na()
es = []

for i in range(m):
    a,b,c = na()
    es.append([a-1,b-1,-c])

ig = [[] for _ in range(n)]
for e in es:
    ig[e[1]].append(e)

ved = [False] * n
q = [n-1]
j = 0
ved[n-1] = True
while(j < len(q)):
    cur = q[j]
    for e in ig[cur]:
        if not ved[e[0]]:
            ved[e[0]] = True
            q.append(e[0])
    j += 1

res = bf(es, n, 0, ved)
if res:
    print(-res[n-1])
else:
    print("inf")