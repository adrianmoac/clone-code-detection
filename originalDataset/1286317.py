N,M = map(int, input().split())

from collections import defaultdict
E = []

for i in range(M):
  a,b,c = map(int, input().split())
  a,b = a-1, b-1
  E += [(a,b,c)]

def reachable_vertices(neighbor, s):
  V = set()
  V.add(s)
  stack=[s]
  while stack:
    v = stack.pop()
    for u in neighbor[v]:
      if u not in V:
        V.add(u)
        stack.append(u)
  return V

def neighbor_dict(E):
  neighbor = defaultdict(list)
  for a,b,c in E:
    neighbor[a].append(b)
  return neighbor

def rev_neighbor_dict(E):
  neighbor = defaultdict(list)
  for a,b,c in E:
    neighbor[b].append(a)
  return neighbor

def degenerate_graph(V, E):
  d = {v:i for i,v in enumerate(sorted(V))}
  return len(V), [(d[a],d[b],c) for a,b,c in E if a in V and b in V]

# only vertices that are reachable from 1 or N
N,E = degenerate_graph(reachable_vertices(neighbor_dict(E), 0), E)
N,E = degenerate_graph(reachable_vertices(rev_neighbor_dict(E), N-1), E)
score = [float('-inf')]*N
score[0] = 0


i = 0
updated=True
while updated:
  if i == N:
    print('inf')
    break

  updated = False
  for a,b,w in E:
    if score[b] < score[a] + w:
      score[b] = score[a] + w
      updated = True
  i += 1
else:
  print(score[N-1])