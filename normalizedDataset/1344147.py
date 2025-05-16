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
    id28=id17()
    return (id27, id28)


def id29(id27, id28):
    id30=[0]*9
    for id31 in id28:
        if 1<=id31<=399:
            id30[0]=1
        elif 400<=id31<=799:
            id30[1]=1
        elif 800<=id31<=1199:
            id30[2]=1
        elif 1200<=id31<=1599:
            id30[3]=1
        elif 1600<=id31<=1999:
            id30[4]=1
        elif 2000<=id31<=2399:
            id30[5]=1
        elif 2400<=id31<=2799:
            id30[6]=1
        elif 2800<=id31<=3199:
            id30[7]=1
        elif id31>=3200:
            id30[8]+=1

    id32=id33(id30[0: 8])
    id34=id33(id30)
    if id32==0:
        id35=1
    else:
        id35=id32
    
    id36=(id35, id34)
    return id36


def id37():
    id38=id26()
    id36=id29(*id38)
    print("{} {}".id39(id36[0], id36[1]))


if id40=="__main__":
    id37()