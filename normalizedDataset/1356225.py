
id0=10**20


def id1(id2, id3, id4):
    id5=[-id0]*id2
    id5[0]=0
    id6=[-1]*id2

    for id7 in id8(id2):
        for id9, id10 in id4.id11():
            id12, id13=id9
            if id5[id13]<id5[id12]+id10:
                id5[id13]=id5[id12]+id10
                id6[id13]=id12

    id13=id2-1
    while id13!=0:
        id12=id6[id13]
        id10=id4[(id12, id13)]
        if id5[id13]<id5[id12]+id10:
            return "inf"
        id13=id12
    return id5[id2-1]


def id14(id2, id3, id4):
    id5=[-id0]*id2
    id5[0]=0
    id6=[-1]*id2

    for id7 in id8(id2):
        for id9, id10 in id4.id11():
            id12, id13=id9
            if id5[id13]<id5[id12]+id10:
                id5[id13]=id5[id12]+id10
                id6[id13]=id12

    id15=id5[id2-1]

    for id7 in id8(id2):
        for id9, id10 in id4.id11():
            id12, id13=id9
            if id5[id13]<id5[id12]+id10:
                id5[id13]=id5[id12]+id10
                id6[id13]=id12

    if id15<id5[id2-1]:
        return "inf"
    return id15


def id16():
    id2, id3=map(id17, input().split())
    id4={}
    for _ in id8(id3):
        id12, id13, id10=map(id17, input().split())
        id12-=1
        id13-=1
        id4[(id12, id13)]=id10

    id15=id14(id2, id3, id4)
    print(id15)

if id18=="__main__":
    id16()