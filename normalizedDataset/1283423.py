import id0

id1=id0.id1


def id2(): return map(id3, id1.id4().split())


def id5(): return id1.id4().id6()

def id7(id8, id9, id10, id11):
    id12=999999999999999999
    id13=[id12]*id9
    id13[id10]=0

    for id14 in id15(id9-1):
        id16=False
        for id17 in id8:
            if not id11[id17[0]]: continue
            if not id11[id17[1]]: continue
            if id13[id17[0]]+id17[2]<id13[id17[1]]:
                id13[id17[1]]=id13[id17[0]]+id17[2]
                id16=True
        if not id16: break
    for id17 in id8:
        if not id11[id17[0]]: continue
        if not id11[id17[1]]: continue
        if id13[id17[0]]+id17[2]<id13[id17[1]]:
            return None
    return id13

def id18(id10, id19, id20):
    id9=id21(id19)
    id11=[False]*id9
    id22=[id10]
    id23=0
    id11[id10]=True
    while(id23<id21(id22)):
        id24=id22[id23]
        for id17 in id19[id24]:
            if not id11[id17[id20]]:
                id11[id17[id20]]=True
                id22.id25(id17[id20])
        id23+=1
    return id11

id9,id26=id2()
id8=[]

for id14 in id15(id26):
    id27,id28,id29=id2()
    id8.id25([id27-1,id28-1,-id29])

id19=[[] for _ in id15(id9)]
for id17 in id8:
    id19[id17[0]].id25(id17)

id30=[[] for _ in id15(id9)]
for id17 in id8:
    id30[id17[1]].id25(id17)


id11=id18(0, id19, 1)
id31=id18(id9-1, id30, 0)

for id14 in id15(id9):
    id11[id14]&=id31[id14]

id32=id7(id8, id9, 0, id11)
if id32:
    print(-id32[id9-1])
else:
    print("inf")