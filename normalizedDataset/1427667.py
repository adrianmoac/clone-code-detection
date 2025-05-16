import id0
id1=id0.id2.id1
from id3 import id4, id5
from id6 import id7

id8=id9(id1())
id10=[[] for _ in [None]*id8]
for _ in [None]*(id8-1):
    id11,id12=map(id9, id1().split())
    id10[id11-1].id13(id12-1)
    id10[id12-1].id13(id11-1)


def id14(id15, id10, id16, id17):
    id18=id19("inf")
    id20=[(id18,None) for _ in [None]*id15]
    id20[id16]=(0, None)
    id21=[(0, id16)]

    while id21:
        id22, id23=id5(id21)
        if id20[id23][0]<id22:
            continue

        for id24 in id10[id23]:
            id25=id22+1
            if id20[id24][0]>id25:
                id20[id24]=(id25, id23)
                if not id24 in id17:
                    id4(id21, (id25, id24))
    return id20

def id26(id16, id17):
    id27=id7()
    id28, id13=id27.id29, id27.id13
    id30=0
    id31=[0]*id8
    id13(id16)
    while id27:
        id32=id28()
        for id23 in id10[id32]:
            if id31[id23]==0 and id23 not in id17:
                id13(id23)
                id31[id23]=1
                id30+=1
    return id30

id33=id14(id8, id10, 0, {id8-1})
id34=[]
id35=id34.id13
id15=id33[id8-1][1]
while id15!=0:
    id35(id15)
    id15=id33[id15][1]

import id36
id37=id36.id38(id39(id34)/2)
id40=id41(id34[-id37:]+[0])
id42=id41(id34[:-id37]+[id8-1])
id43=id26(0, id42)
id44=id26(id8-1, id40)
#print(fen, snuke, path, fen_s, snuke_s)
print("Fennec" if id43>id44 else "Snuke")