#!/usr/bin/env python3

# AtCoder Regular Contest 054 B. ムーアの法則
# 中心差分と二分探索による解答例

id0=200
id1=10e-10
id2=1e3  # 数式処理システムによる
id3=0.0


# 5点近似によりf'(x)を求める
# Based on: http://qiita.com/copycat/items/e61d13c01c1cb947a393
def id4(id5, id6, id7=id1):
    id8=id5(id6+id7)
    id9=id5(id6-id7)
    id10=id5(id6+2*id7)
    id11=id5(id6-2*id7)
    return (id11-8*id9+8*id8-id10)/(12*id7)


# 二分探索（二分法）によりg(x)の[a, b]における零点を求める
def id12(id13, id14, id15, id16=id0):
    for _ in id17(id16):
        id18=(id14+id15)/2
        if id13(id18)*id13(id14)>0:
            id14=id18
        else:
            id15=id18
    else:
        return (id14+id15)/2


def id19(id20):
    # 最小化したい関数
    def id5(id6): return id6+id20*2**(-id6/1.5)

    # その導関数
    def id21(id6): return id4(id5, id6)

    if id21(id3)*id21(id2)>0:
        # f'(MIN_X)とf'(MAX_X)が同符号ならば、
        # 区間[MIN_X, MAX_X]にf'(x)の零点はない
        # （二分探索は機能しない）
        # このときには、x0=0
        id22=0
    else:
        # f'(x)を0にするx、すなわちf(x)を最小化するx
        id22=id12(id21, id3, id2)
    # 答え
    return id5(id22)


def id23():
    print("{:.12f}".id24(id19(id25(input()))))


if id26=="__main__":
    id23()