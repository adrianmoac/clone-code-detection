# coding: utf-8


import id0
id0.id1(id2(1e6))


class id3(id4):
    def id5(id6, id7):
        id6.id7=id7
        id6.id8=[None]*(id7+1)
        for id9 in id10(1, id7+1):
            id6.id8[id9]=id11()

    def id12(id6, id13, id14):
        id6.id8[id13].id15(id14)
        id6.id8[id14].id15(id13)

    def id16(id6, id17, id18):
        # fからNへの最短経路を探す
        if id17==id6.id7:
            return [id17]
        for id19 in id6.id8[id17]:
            if id19!=id18:
                id12=id6.id16(id19, id17)
                if id12 is not None:
                    id12.id20(id17)
                    return id12
        return None

    def id21(id6, id22, id23, id18):
        # startからblockを経由せず行ける範囲のnode数
        id24=1
        for id19 in id6.id8[id22]:
            if id19!=id18 and id19!=id23:
                id24+=id6.id21(id19, id23, id22)
        return id24


def id25():
    id7=id2(input())
    id26=id3(id7)
    for id9 in id10(id7-1):
        id13, id14=map(id2, input().split())
        id26.id12(id13, id14)
    id12=id26.id16(1, None)
    id27=id28(id12)
    id29=id12[id27//2]
    id30=id12[id27//2-1]
    id31=id26.id21(1, id30, None)
    id32=id26.id21(id7, id29, None)
    # print(fr)
    # print(sr)
    if id31>id32:
        print("Fennec")
    else:
        print("Snuke")


id25()