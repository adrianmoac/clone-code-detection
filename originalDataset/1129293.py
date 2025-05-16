import sys
from collections import deque, Counter

def debug(x, table):
    for name, val in table.items():
        if x is val:
            print('DEBUG:{} -> {}'.format(name, val), file=sys.stderr)
            return None

def solve():
    N, K, L = map(int, input().split())
    Adj_r = [[] for i in range(N)]
    Adj_t = [[] for i in range(N)]

    for i in range(K):
        p, q = map(int, input().split())
        p, q = p-1, q-1
        Adj_r[p].append(q)
        Adj_r[q].append(p)

    for i in range(L):
        r, s = map(int, input().split())
        r, s = r-1, s-1
        Adj_t[r].append(s)
        Adj_t[s].append(r)

    col = 0
    cols_r = [None] * N
    cols_t = [None] * N

    for u in range(N):
        if cols_r[u] is None:
            bfs_color(N, Adj_r, cols_r, u, col)
            col += 1
        if cols_t[u] is None:
            bfs_color(N, Adj_t, cols_t, u, col)
            col += 1

    # debug(cols_r, locals())
    # debug(cols_t, locals())

    cnt = Counter((cols_r[u], cols_t[u]) for u in range(N))

    ans = [cnt[cols_r[u], cols_t[u]] for u in range(N)]

    print(*ans)


def bfs_color(N, Adj, v_cols, u, col):
    v_cols[u] = col
    nxts = deque([u])

    while nxts:
        v = nxts.popleft()

        for w in Adj[v]:
            if v_cols[w] is None:
                v_cols[w] = col
                nxts.append(w)


if __name__ == '__main__':
    solve()