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
    id28=id15()
    id29=[]
    id30=[]
    for id21 in id22(id28):
        id31, id32=id17()
        id29.id33(id31)
        id30.id33(id32)
    return (id27, id28, id29, id30)


# 適当なVを与えられたとき、全部で何回増築できるか
def id34(id35, id28, id29, id30):
    id36=0
    for id37 in id22(id28):
        if id35<id29[id37]:
            continue
        else:
            id36+=((id35-id29[id37])//id30[id37]+1)

    return id36


def id38(id27, id28, id29, id30):
    id39=id40(id29)
    id41=id40(id30)

    id42=1
    id43=id39+id41*id27
    
    # ぎりぎりcountがKに満たないvalueを探索
    while True:
        id44=(id42+id43)//2
        id45=id34(id44, id28, id29, id30)

        if id45>=id27:
            id43=id44
        elif id45<id27:
            id42=id44

        if id43-id42<=1:
            break

    id46=id42
    id47=id34(id46, id28, id29, id30)

    id48=0
    for id37 in id22(id28):
        if id46>=id29[id37]:
            id49=(id46-id29[id37])//id30[id37]
            id48+=(id29[id37]*2+id49*id30[id37])*(id49+1)//2
    
    id48+=(id42+1)*(id27-id47)

    return id48


def id50():
    id51=id26()
    print(id38(*id51))


if id52=="__main__":
    id50()