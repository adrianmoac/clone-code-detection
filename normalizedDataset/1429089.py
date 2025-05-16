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
    id28=id2.id29(id18)
    for id21 in id22(id27-1):
        id30, id31=id17()
        id28[id30].id32(id31)
        id28[id31].id32(id30)
    return id27, id28


def id33(id27, id28):
    id34=id35()
    id36=id35()
    id34.id37(1)
    id36.id37(id27)

    id38=1
    id39=True

    id40=[False]*(id27+1)
    id41=[False]*(id27+1)
    id40[0], id40[1]=True, True
    id41[0], id41[id27]=True, True

    while id42(id34)!=0:
        id43=id35()
        for id44 in id34:
            id45=id28[id44]
            for id46 in id45:
                if id39 and id46 in id36:
                    id39=False
                    id40[id46]=True

                if id40[id46]:
                    continue
                else:
                    id43.id37(id46)
                    id40[id46]=True

        id38+=id42(id43)
        id34=id43

        if id39:
            id47=id35()
            for id44 in id36:
                id45=id28[id44]
                for id46 in id45:
                    if id46 in id34:
                        id40[id44]=True
                        id39=False
                        break

                    if id41[id46]:
                        continue
                    else:
                        id47.id37(id46)
                        id41[id46]=True

            id36=id47

    if id38>id27//2:
        id48="Fennec"
    else:
        id48="Snuke"


    return id48


def id49():
    id50=id26()
    print(id33(*id50))


if id51=="__main__":
    id49()