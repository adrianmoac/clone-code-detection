# coding: utf-8
import id0, id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11
id10.id12(10**7)
id13=10**20
id14=10**9+7


def id15(): return id16(input())
def id17(): return id18(map(id16, input().split()))
def id19(id20): return [id17() for id21 in id22(id20)]
def id23(): return {id24: id25 for id24, id25 in id17()}


def id26(id27, id28):
    id29=1
    if id27-id28<id28:
        id28=id27-id28
    for id30 in id22(id27, id27-id28,-1):
        id29=id29*id30%id14
    id31=[1]*(id28+1)
    for id30 in id22(1, id28+1):
        id31[id30]=id31[id30-1]*id30%id14
    return id29%id14*id32(id31[id28], id14-2, id14)%id14


def id33():
    id34=id15()
    id35=id17()
    return id34, id35


def id36(id34, id35):
    id37=id35[0]
    id38=0
    id39=1

    for id40, id41 in id42(id35):
        if id41==-1:
            id38+=1
            continue
        else:
            if id38==0:
                id37=id41
                continue
            else:
                id43=id41-id37
                id44=id43+id38
                id45=id38
                id39*=id26(id44, id45)
                id37=id41
                id38=0

    return (id39%id14)


def id46():
    id47=id33()
    print(id36(*id47))


if id48=="__main__":
    id46()