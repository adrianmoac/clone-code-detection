

N,M = map(int, input().split())

from collections import defaultdict
neighbor = defaultdict(list)
Rneighbor = defaultdict(list)
edges = []
for i in range(M):
  a,b,c = map(int, input().split())
  a,b = a-1, b-1
  edges += [(a,b,c)]
  neighbor[a].append(b)
  Rneighbor[b].append(a)

# only vertices that are reachable from 1 or N
v1 = set()
v1.add(0)
stack = [0]
while stack:
  v = stack.pop()
  for u in neighbor[v]:
    if u not in v1:
      v1.add(u)
      stack.append(u)

vn = set()
vn.add(N-1)
stack = [N-1]
while stack:
  v = stack.pop()
  for u in Rneighbor[v]:
    if u not in vn:
      vn.add(u)
      stack.append(u)

V = v1 & vn

edges = [(a,b,c) for a,b,c in edges if a in V and b in V]
score = [float('-inf')]*N
score[0] = 0

updated = True
i = 0

positive_cycle = False

while updated:
  if i == len(V):
    positive_cycle = True
    break

  updated = False
  for a,b,w in edges:
    if score[b] < score[a] + w:
      score[b] = score[a] + w
      updated = True
  i += 1

if positive_cycle:
  print('inf')
else:
  print(score[N-1])