from collections import deque
EMPTY = 0
BLACK = 1
WHITE = 2
N = input()
G = {i: [] for i in range(1, N+1)}
for i in range(N-1):
    a, b = map(int, raw_input().split())
    G[a].append(b)
    G[b].append(a)

parent = {}
dist = [N] * (N+1)
dist[1] = 0
que = deque([1])
while len(que) > 0:
    s = que.popleft()
    for t in G[s]:
        if dist[t] > dist[s]+1:
            dist[t] = dist[s]+1
            parent[t] = s
            que.append(t)

s = N
path = [s]
while s in parent:
    path.append(parent[s])
    s = parent[s]
path = path[::-1]

colors = [EMPTY] * (N+1)
n = len(path)
que_black, que_white = deque(), deque()
for i in range(n):
    if i % 2 == 0:
        v = path[i/2]
        colors[v] = BLACK
        que_black.append(v)
    else:
        v = path[n-i/2-1]
        colors[v] = WHITE
        que_white.append(v)

def paint(que, c):
    while len(que) > 0:
        s = que.popleft()
        for t in G[s]:
            if colors[t] == EMPTY:        
                colors[t] = c
                que.append(t)
paint(que_black, BLACK)
paint(que_white, WHITE)
score = 0
for c in colors:
    if c == BLACK:
        score += 1
    elif c == WHITE:
        score -= 1
print "Fennec" if score > 0 else "Snuke"
