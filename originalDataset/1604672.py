def D_takoyaki(N, D, Q, P):
    from itertools import product

    square_memo = [[-1] * N for _ in range(N)]

    def rectangleFromOrigin(x, y):
        # 原点と(x,y)から作れる長方形内でのおいしさの和
        if x < 0 or y < 0:
            return 0
        if square_memo[x][y] == -1:
            # ex.(x,y)=(2,3)
            # 全体     領域1 領域2 領域3 領域4
            # ***--    ++--- ###-- xx--- -----
            # ***--    ++--- ###-- xx--- -----
            # ***-- <= ++--- ###-- xx--- -----
            # ***--    ++--- ----- ----- --o--
            # -----    ----- ----- ----- -----
            # 原点から伸びる*の領域について計算するなら、領域1+2-3+4とすればよい。
            s = 0
            s += rectangleFromOrigin(x - 1, y)  # 領域1
            s += rectangleFromOrigin(x, y - 1)  # 領域2
            s -= rectangleFromOrigin(x - 1, y - 1)  # 領域3
            s += D[x][y]  # 領域4
            square_memo[x][y] = s
        return square_memo[x][y]

    def rectangle(x, y, w, h):
        #(x,y),(w,h)が定める長方形内でのおいしさの和
        s = 0
        # ex.(x,y,w,h)=(1,1,3,3)
        # 全体     領域1 領域2 領域3 領域4
        # -----    ++++- ####- x---- o----
        # -***-    ++++- ----- x---- -----
        # -***- <= ++++- ----- x---- -----
        # -***-    ++++- ----- x---- -----
        # -----    ----- ----- ----- -----
        s += rectangleFromOrigin(w, h)  # 領域1
        s -= rectangleFromOrigin(x - 1, h)  # 領域2
        s -= rectangleFromOrigin(w, y - 1)  # 領域3
        s += rectangleFromOrigin(x - 1, y - 1)  # 領域4
        return s

    ans = [0] * (N**2)
    # いろいろな長方形に対して計算
    for w, h in product(range(N), repeat=2):
        x_max = N - w
        y_max = N - h
        idx = (w + 1) * (h + 1) - 1
        for x, y in product(range(x_max), range(y_max)):
            tmp = rectangle(x, y, x + w, y + h)
            ans[idx] = max(ans[idx], tmp)  # 幅w、高さhの長方形を張ったときのおいしさのうち最大値

    # 「店員が焼ける能力の上限と同じ面積の長方形を張ると逆に点が下がる」場合があるため、
    # 調整を行う(それまでの最大値を上回るときのみ値を更新)
    tmp = 0
    for i in range(N**2):
        if ans[i] > tmp:
            tmp = ans[i]
        else:
            ans[i] = tmp

    for i in P:
        print(ans[i - 1])
    return None

N = int(input())
D = [[int(i) for i in input().split()] for _ in range(N)]
Q = int(input())
P = [int(input()) for i in range(Q)]
D_takoyaki(N, D, Q, P)