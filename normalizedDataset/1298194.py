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
    id27, id28=id17()
    return (id27, id28)

def id29(id27, id28):
    id30=id13
    
    if id27%3==0 or id28%3==0:
        return 0
    else:
        id30=id31(id30, id27, id28)

    if id28%2==0:
        for id32 in id22(1, id27):
            id33=id32*id28
            id34=(id27-id32)*id28//2
            id30=id31(id30, id35(id33-id34))
    else:
        for id32 in id22(1, id27):
            id33=id32*id28
            id34=(id27-id32)*(id28//2)
            id36=(id27-id32)*(id28//2+1)
            id37=id38([id33, id34, id36])
            id30=id31(id30, (id37[2]-id37[0]))

    if id27%2==0:
        for id39 in id22(1, id28):
            id33=id39*id27
            id34=(id28-id39)*id27//2
            id30=id31(id30, id35(id33-id34))
    else:
        for id39 in id22(1, id28):
            id33=id39*id27
            id34=(id28-id39)*(id27//2)
            id36=(id28-id39)*(id27//2+1)
            id37=id38([id33, id34, id36])
            id30=id31(id30, (id37[2]-id37[0]))
    
    return id30


def id40():
    id41=id26()
    print(id29(*id41))


if id42=="__main__":
    id40()