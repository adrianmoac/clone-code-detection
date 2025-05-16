import id0

id1=id0.id1

id2=lambda: id3(id4())
id5=lambda: id6(map(id3, id1.id7().split()))
id4=lambda: id1.id7()

id8,id9,id10=id5()
id11=id5()
for id12 in id13(id10):
    id11[id12]-=1

id14=[[99999999999]*id8 for _ in id13(id8)]
for id12 in id13(id8):
    id14[id12][id12]=0
for id12 in id13(id9):
    id15, id16, id17=id5()
    id15-=1
    id16-=1
    id14[id15][id16]=id14[id16][id15]=id17

from id18 import*def id19(id14, id20):
    id8=id21(id14)
    id22=[1e18]*id8
    id22[id20]=0
    id23=[]
    id24(id23, (0, id20))
    while id21(id23)>0:
        id25, id26=id27(id23)
        if id25!=id22[id26]: continue
        for id28, id29 in id14[id26]:
            if id25+id29<id22[id28]:
                id22[id28]=id25+id29
                id24(id23, (id22[id28], id28))
    return id22

def id30(id14, id20):
    id8=id21(id14)
    id22=[1e18]*id8
    id22[id20]=0

    id31=[0]*id8
    while True:
        id32=1e19
        id33=-1
        for id12 in id13(id8):
            if not id31[id12] and id22[id12]<id32:
                id32=id22[id12]
                id33=id12
        if id33==-1: break
        id31[id33]=1
        for id12 in id13(id8):
            id22[id12]=id34(id22[id12], id32+id14[id33][id12])
    return id22


id35=[None]*id8
for id10 in id11:
    id35[id10]=id30(id14, id10)

from id36 import*id37=9999999999999999999
for id38 in id39(id11):
    id40=0
    for id12 in id13(1, id21(id11)):
        id40+=id35[id38[id12-1]][id38[id12]]
    id37=id34(id37, id40)
print(id37)