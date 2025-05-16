#-*-coding: utf-8-*-import heapq
import id0

def id1(id2, id3=None):
    # permutations('ABCD', 2)-->AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3))-->012 021 102 120 201 210
    id4=id5(id2)
    id6=id7(id4)
    id3=id6 if id3 is None else id3
    if id3>id6:
        return
    id8=id9(id10(id6))
    id11=id9(id10(id6, id6-id3,-1))
    yield id5(id4[id12] for id12 in id8[:id3])
    while id6:
        for id12 in id13(id10(id3)):
            id11[id12]-=1
            if id11[id12]==0:
                id8[id12:]=id8[id12+1:]+id8[id12:id12+1]
                id11[id12]=id6-id12
            else:
                id14=id11[id12]
                id8[id12], id8[-id14]=id8[-id14], id8[id12]
                yield id5(id4[id12] for id12 in id8[:id3])
                break
        else:
            return

id15=input()
id16, id17, id18=[id19(id20) for id20 in id15.split()]
id15=input()
id21=[id19(id20) for id20 in id15.split()]
id22=[]
for id12 in id10(id17):
    id15=input()
    id22.id23([id19(id20) for id20 in id15.split()])

id24={}
for id20, id25, id26 in id22:
    id24[(id20, id25)], id24[(id25, id20)]=id26, id26

id27={}
for id12 in id10(1, id16+1):
    id27[(id12, id12)]=0
for id28 in id21:
    id29={}
    id30=[False for id12 in id10(id16+1)]
    id30[id28]=True
    id31=1
    id32=id28
    while id31<id16:
        id33=[None, None]
        for id12 in id10(1, id16+1):
            if id30[id12]:
                continue
            if (id32, id12) not in id24:
                id34=100000*200+1
            else:
                id34=id27[(id28, id32)]+id24[(id32, id12)]
            if (id28, id12) not in id29 or id29[(id28, id12)]>id34:
                id29[(id28, id12)]=id34
                id29[(id12, id28)]=id34
            if id33[0] is None or id33[1]>id29[(id28, id12)]:
                id33=id12, id29[(id28, id12)]
        id27[(id28, id33[0])], id27[(id33[0], id28)]=id33[1], id33[1]
        id32=id33[0]
        id30[id32]=True
        id31+=1

id35=None
for id36 in id1(id10(id7(id21))):
    id36=id9(id36)
    id37=0
    id38=None
    for id39, id40 in id41(id36, id36[1:]+[id36[0]]):
        id42, id43=id21[id39], id21[id40]
        id44=id27[(id42, id43)]
        if id38 is None or id38<id44:
            id38=id44
        id37+=id44
    id37-=id44
    if id35 is None or id35>id37:
        id35=id37
print(id35)