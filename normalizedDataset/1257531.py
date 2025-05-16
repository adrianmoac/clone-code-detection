id0=[[0]*3 for id1 in id2(3)]  # 盤面(0:null, 1:dai, 2,ko)
id3=[id4(map(id5, input().split())) for _ in id2(2)]
id6=[id4(map(id5, input().split())) for _ in id2(3)]


def id7():
    return "".id8([id9 for id9 in ["".id8(map(id10, id0[id1])) for id1 in id2(3)]])

id11=id12()

id13=0
for id1 in id2(3):
    for id14 in id2(2):
        id13+=id3[id14][id1]+id6[id1][id14]


def id15():
    id16=0
    for id1 in id2(3):
        for id14 in id2(2):
            if id0[id14][id1]!=id0[id14+1][id1]:
                id16+=id3[id14][id1]
            if id0[id1][id14]!=id0[id1][id14+1]:
                id16+=id6[id1][id14]
    return id13-id16


def id17(id18, id19):
    global id0
    if id19==9:
        return id15()

    if id18 and id18 in id11.id20():
        return id11[id18]

    # turn=position%2
    if id19%2==0:  # dai
        id16=-1e10
        for id1 in id2(3):
            for id14 in id2(3):
                if not id0[id1][id14]:
                    id0[id1][id14]=1

                    id16=id21(id16, id17(id7(), id19+1))
                    id0[id1][id14]=0

    else:  # ko
        id16=1e10
        for id1 in id2(3):
            for id14 in id2(3):
                if not id0[id1][id14]:
                    id0[id1][id14]=2
                    id16=id22(id16, id17(id7(), id19+1))
                    id0[id1][id14]=0

    id11[id7()]=id16
    return id16


id23=id17(None, 0)
print(id23)
print(id13-id23)