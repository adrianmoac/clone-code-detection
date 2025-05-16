#!/usr/bin/python
#-*-coding: utf-8-*-import sys
import id0
import id1
import id2
import id3 as id4
from id5 import id6, id7
from id8 import id9, id10, id11, id12
id13.id14(10000)


class id15(id16):
    pass


def id17(id18):
    for id19 in id18:
        print(id19)


def id20(id18):
    for id19 in id18:
        print("".id21(id19))


def id22(id18):
    id23=id24(map(id24, id25(*id18)))
    return id23


def id26():
    id27, id28=id24(map(id29, input().split(" ")))
    id30=[[0]*id27 for _ in id31(id27)]
    for _ in id31(id28):
        id32, id33=id24(map(id29, input().split(" ")))
        id30[id32-1][id33-1], id30[id33-1][id32-1]=1, 1

    id34=[False for _ in id31(id27)]
    id35=0
    def id36(id37, id38):
        id34[id37]=True
        for id39 in id31(id27):
            if id38[id37][id39]==1 and id34[id39]!=True:
                id36(id39, id38)

    id40=[[False]*id27 for _ in id31(id27)]
    for id41 in id31(id27):
        for id42 in id31(id27):
            if id40[id41][id42]==True:
                pass
            elif id30[id41][id42]==1 and id40[id41][id42]==False:
                id30[id41][id42], id30[id42][id41]=0, 0
                id36(0, id30)
                if id34.id43(False)==0:
                    pass
                else:
                    id35+=1
                id30[id41][id42], id30[id42][id41]=1, 1
                id34=[False for _ in id31(id27)]
                id40[id41][id42], id40[id42][id41]=True, True

    print(id35)
    

id26()