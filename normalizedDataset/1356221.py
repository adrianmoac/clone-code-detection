import id0

# sys.stdin=open('d1.in')

id1=10**20


def id2(id3, id4, id5):
    id6=[-id1]*id3
    id6[0]=0
    id7=[-1]*id3

    for id8 in id9(id3):
        for id10, id11 in id5.id12():
            id13, id14=id10
            if id6[id14]<id6[id13]+id11:
                id6[id14]=id6[id13]+id11
                id7[id14]=id13

    id14=id3-1
    while id14!=0:
        id13=id7[id14]
        id11=id5[(id13, id14)]
        if id6[id14]<id6[id13]+id11:
            return "inf"
        id14=id13
    return id6[id3-1]


def id15(id3, id4, id5):
    id6=[-id1]*id3
    id6[0]=0
    id7=[-1]*id3

    for id8 in id9(id3):
        for id10, id11 in id5.id12():
            id13, id14=id10
            if id6[id14]<id6[id13]+id11:
                id6[id14]=id6[id13]+id11
                id7[id14]=id13

    id16=id6[id3-1]

    for id8 in id9(id3):
        for id10, id11 in id5.id12():
            id13, id14=id10
            if id6[id14]<id6[id13]+id11:
                id6[id14]=id6[id13]+id11
                id7[id14]=id13

    if id16<id6[id3-1]:
        return "inf"
    return id16


def id17():
    id3, id4=map(id18, input().split())
    id5={}
    for _ in id9(id4):
        id13, id14, id11=map(id18, input().split())
        id13-=1
        id14-=1
        id5[(id13, id14)]=id11

    id16=id2(id3, id4, id5)
    print(id16)

if id19=="__main__":
    id17()