# coding: utf-8
import id0, id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11

id10.id12(10**7)
id13=10**20
id14=10**9+7


def id15(): return id16(input())
def id17(): return id18(map(id16, input().split()))
def id19(id20): return [id17() for id21 in id22(id20)]
def id23(): return {id24: id25 for id24, id25 in id17()}


def id26():
    id27=id15()
    id28, id29=[], []
    for id30 in id22(id27):
        id31, id32=id17()
        id28.id33((id30, id31))
        id29.id33((id30, id32))
    return id27, id28, id29


class id34(id35):
    def id36(id37, id38):  # 初期化
        id37.id39=id0.id0("L", id22(id38))
        id37.id40=id0.id0("L", (0 for id30 in id22(id38)))

    def id41(id37, id42):  # 根を求める
        if id37.id39[id42]==id42:
            return id42
        else:
            id43=id37.id41(id37.id39[id42])
            id37.id39[id42]=id43  # 経路圧縮
            return id43

    def id44(id37, id45, id46):  # 同じ集合に属するか
        return id37.id41(id45)==id37.id41(id46)

    def id47(id37, id45, id46):  # 属する集合を併合
        id28=id37.id41(id45)
        id29=id37.id41(id46)
        if id28==id29:
            pass
        elif id37.id40[id28]<id37.id40[id29]:
            id37.id39[id28]=id29
        else:
            id37.id39[id29]=id28
            if id37.id40[id28]==id37.id40[id29]:
                id37.id40[id28]+=1


def id48(id27, id28, id29):
    id49=[]
    id28.id50(id24=lambda id28: id28[1])
    id29.id50(id24=lambda id28: id28[1])
    for id30 in id22(id27-1):
        id51, id52=id28[id30], id28[id30+1]
        id53, id54=id29[id30], id29[id30+1]
        id49.id33((id51[0], id52[0], id52[1]-id51[1]))
        id49.id33((id53[0], id54[0], id54[1]-id53[1]))

    id49.id50(id24=lambda id28: id28[2])
    id55=id34(id27)
    id56=0
    for id57 in id49:
        if not id55.id44(id57[0], id57[1]):
            id55.id47(id57[0], id57[1])
            id56+=id57[2]

    return id56


def id58():
    id59=id26()
    print(id48(*id59))


if id60=="__main__":
    id58()