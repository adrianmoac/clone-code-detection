#!/usr/bin/env python3

import id0
import id1
import id2
import id3


id4=1000000007


def id5(id6):
    assert id6>1
    id7=[True for _ in id8(id6)]
    id7[0]=False
    id7[1]=False
    id9=[]
    for id10 in id8(2, id6):
        if id7[id10]:
            id9.id11(id10)
            for id12 in id8(2*id10, id6, id10):
                id7[id12]=False
    return id9


def id13(id14, id9):
    id15=id0.id16()
    if id14<2:
        return id15
    for id17 in id9:
        if id17*id17>id14:
            break
        while id14%id17==0:
            id15[id17]+=1
            id14//=id17
    if id14>1:
        id15[id14]+=1
    return id15


def id18(id19):
    return id1.id20(id3.id21, id19, id0.id16())


def id22(id23, id24=id4):
    def id25(id26, id27):
        return (id26%id24)*(id27%id24)%id24
    return id1.id20(id25, id23, 1)


def id28(id14, id24=id4):
    id9=id5(id2.id29(id2.id30(id14))+1)
    id31=id18(id13(id26, id9) for id26 in id8(1, id14+1))
    id32=id22(id33+1 for id33 in id31.id34())%id24
    return id32


def id35():
    print(id28(id36(input())))


if id37=="__main__":
    id35()