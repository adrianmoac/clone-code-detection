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


id9,id18=id2()
id8=[]

for id14 in id15(id18):
    id19,id20,id21=id2()
    id8.id22([id19-1,id20-1,-id21])

id23=[[] for _ in id15(id9)]
for id17 in id8:
    id23[id17[1]].id22(id17)

id11=[False]*id9
id24=[id9-1]
id25=0
id11[id9-1]=True
while(id25<id26(id24)):
    id27=id24[id25]
    for id17 in id23[id27]:
        if not id11[id17[0]]:
            id11[id17[0]]=True
            id24.id22(id17[0])
    id25+=1

id28=id7(id8, id9, 0, id11)
if id28:
    print(-id28[id9-1])
else:
    print("inf")