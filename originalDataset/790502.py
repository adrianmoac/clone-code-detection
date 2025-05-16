import itertools


def read_data():
    N, M = map(int, input().split())
    xy = []
    for m in range(M):
        x, y = map(int, input().split())
        xy.append((x - 1, y - 1))
    return N, M, xy

def solve_naive(N, M, xy):
    count = 0
    for seq in itertools.permutations(list(range(N))):
        if is_valid(seq, xy):
            count += 1
    return count

def is_valid(seq, xy):
    pos = [0] * len(seq)
    for i, s in enumerate(seq):
        pos[s] = i
    for x, y in xy:
        if pos[x] > pos[y]:
            return False
    return True


def init_memo(N):
    memo = [[] for i in range(1 << N)]
    for mask in range(1 << N):
        memo_mask = memo[mask]
        for idx in range(N):
            if mask & (1 << idx):
                memo_mask.append(idx)
    return memo

def solve(N, M, xy):
    '''
    faster[x][y]: pos(x) < pos(y) なら 1 pos(x) > pos(y) なら -1, 不明なら0 
    Es[x] = [y1, y2...]: pos(x) < pos(yi) である yi のリスト 
    '''
    memo = init_memo(N)
    faster = [[0] * N for i in range(N)]
    Es = [[] for i in range(N)]
    for x, y in xy:
        faster[x][y] = 1
        faster[y][x] = -1
        Es[x].append(y)
    for x in range(N):
        f = [x]
        visited = [False] * N
        visited[x] = True
        while f:
            new_f = []
            for u in f:
                for v in Es[u]:
                    if visited[v]:
                        continue
                    visited[v] = True
                    new_f.append(v)
                    faster[x][v] = 1
                    faster[v][x] = -1
            f = new_f
    dp = [0] * (1 << N)
    for mask in range(1, 1 << N):
        if len(memo[mask]) == 1:
            dp[mask] = 1
            continue
        members = memo[mask]
        for idx0 in members:
            faster0 = faster[idx0]
            for idx1 in members:
                if faster0[idx1] == -1:
                    break
            else:
                dp[mask] += dp[mask - (1 << idx0)]
    return dp[(1 << N) - 1]

        
N, M, xy = read_data()
print(solve(N, M, xy))