from itertools import permutations


def main():
    """
    とおり方
    2 <= N <= 200
    2 <= R <= min(8, N)
    より、
    最大でも 2 <= R <= 8
    8! = 40320

    道路
    1 <= M <= N * (N-1) / 2
    より、
    最大でも 100 * 199 = 19900

    調べ方
    rに現れない町を経由する可能性がある
    ある町Aからある町Bまでの最短距離を求める
    ABCの町を訪れるならば、
    A→B→C、
    B→C→A
    C→A→B
    の３パターン（組合せ）がある
    もちろん他の町を経由するかもしれない
        A→(D)→B→(E)→C
    """
    N, M, R = map(int, input().split())
    r = map(int, input().split())

    inf = float("inf")
    d = [[inf] * (N + 1) for _ in range(N + 1)]
    for n in range(1, N + 1):
        d[n][n] = 0

    for _ in range(M):
        a, b, c = map(int, input().split())
        d[a][b] = c
        d[b][a] = c

    for k in range(1, N + 1):
        for i in range(1, N + 1):
            for j in range(1, N + 1):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]

    min_cost = inf
    for p in permutations(r):
        cost = 0
        for i in range(len(p) - 1):
            src, dst = p[i:i + 2]
            cost += d[src][dst]
        min_cost = min(min_cost, cost)

    print(min_cost)

if __name__ == '__main__':
    main()
