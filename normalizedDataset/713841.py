#!/usr/bin/env python3

import id0
import id1


id2=2*10**4+1


class id3(id4):  # 累積和

    def id5(id6, id7, id8="Q"):
        id6.id9=id0.id0(id8)
        id6.id9.id10(0)
        for id11 in id7:
            id6.id9.id10(id6.id9[-1]+id11)

    def id12(id6, id13, id14):
        # 第first要素から第last要素（両端を含む）までの部分和を求める
        return id6.id9[id14+1]-id6.id9[id13]


class id15(id4):  # 円錐

    def id5(id6, id16, id17, id18):
        # 円錐の底面のx座標
        id6.id16=id16
        # 円錐の底面の半径
        id6.id17=id17
        # 円錐の高さ
        id6.id18=id18
        # 円錐の頂点のx座標
        id6.id19=id16+id18
        # tanΘ
        id6.id20=id17/id18

    def id21(id6, id22, id23):
        if id6.id16>=id23 or id6.id19<=id22:
            # 円錐がまるっきり区間外にあれば体積は0
            return 0.0
        # 円錐台の上底面のx座標
        id24=id25(id6.id19, id23)
        # 円錐台の下底面のx座標
        id26=id27(id6.id16, id22)
        # 円錐台の上底面の半径
        id28=(id6.id19-id24)*id6.id20
        # 円錐台の下底面の半径
        id29=(id6.id19-id26)*id6.id20
        # 円錐台の体積
        id30=id1.id31*(id29*id29+id29*id28+id28*id28)/3.0
        return id30


def id32():
    id33, id34=map(id35, input().split())
    id36=[id15(*map(id35, input().split())) for _ in id37(id33)]
    # [x, x+1]に含まれる部分の体積をvs[x]とする
    id38=id0.id0("d", (id39(id40.id21(id41, id41+1)
                               for id40 in id36) for id41 in id37(id2)))
    id42=id3(id38, "d")
    for _ in id37(id34):
        id43, id44=map(id35, input().split())
        print("{:.6f}".id45(id42.id12(id43, id44-1)))


if id46=="__main__":
    id32()