#!/usr/bin/env python3

# AtCoder Regular Contest 054 B. ムーアの法則
# 中心差分と二分探索による解答例

DEFAULT_NUM_ITER = 200
EPS = 10e-10
MAX_X = 1e3  # 数式処理システムによる
MIN_X = 0.0


# 5点近似によりf'(x)を求める
# Based on: http://qiita.com/copycat/items/e61d13c01c1cb947a393
def cent_diff(f, x, h=EPS):
    y1 = f(x + h)
    y2 = f(x - h)
    y3 = f(x + 2 * h)
    y4 = f(x - 2 * h)
    return (y4 - 8 * y2 + 8 * y1 - y3) / (12 * h)


# 二分探索（二分法）によりg(x)の[a, b]における零点を求める
def calc_min_bisection(g, a, b, num_iter=DEFAULT_NUM_ITER):
    for _ in range(num_iter):
        c = (a + b) / 2
        if g(c) * g(a) > 0:
            a = c
        else:
            b = c
    else:
        return (a + b) / 2


def compute_min_time(p):
    # 最小化したい関数
    def f(x): return x + p * 2 ** (-x / 1.5)

    # その導関数
    def fd(x): return cent_diff(f, x)

    if fd(MIN_X) * fd(MAX_X) > 0:
        # f'(MIN_X)とf'(MAX_X)が同符号ならば、
        # 区間[MIN_X, MAX_X]にf'(x)の零点はない
        # （二分探索は機能しない）
        # このときには、x0 = 0
        x0 = 0
    else:
        # f'(x)を0にするx、すなわちf(x)を最小化するx
        x0 = calc_min_bisection(fd, MIN_X, MAX_X)
    # 答え
    return f(x0)


def main():
    print("{:.12f}".format(compute_min_time(float(input()))))


if __name__ == '__main__':
    main()
