from id0 import id1
from id2 import id3
from id4 import id5
import id6

id7, id8=None, None


def id9(id10):
    id11=0
    for id12 in id13(3):
        for id14 in id13(3):
            if id12+1<3 and id10[id12][id14]==id10[id12+1][id14]:
                id11+=id7[id12][id14]
            if id14+1<3 and id10[id12][id14]==id10[id12][id14+1]:
                id11+=id8[id12][id14]
    return id11

id15={}


def id16(id17):
    return id18(id17[0]), id18(id17[1]), id18(id17[2])


def id19(id20, id10):
    if id20>=9:
        return id9(id10)

    if id16(id10) in id15:
        return id15[id16(id10)]

    id21=id20%2
    id22=0 if id21==0 else 10**10
    for id12 in id13(3):
        for id14 in id13(3):
            if id10[id12][id14] is None:
                id10[id12][id14]=id21
                id11=id19(id20+1, id10)
                id10[id12][id14]=None

                if id21==0 and id11>id22:
                    id22=id11
                if id21==1 and id11<id22:
                    id22=id11

    id15[id16(id10)]=id22
    return id22


def id23():
    global id7, id8
    id24=id25(map(id26, input().split()))
    id27=id25(map(id26, input().split()))
    id7=[id24, id27]
    id28=id25(map(id26, input().split()))
    id29=id25(map(id26, input().split()))
    id30=id25(map(id26, input().split()))
    id8=[id28+[0], id29+[0], id30+[0]]

    id10=[[None]*3 for _ in id13(3)]
    id11=id19(0, id10)
    id31=id32([id32(id14) for id14 in id7+id8])
    print(*[id11, id31-id11], id33="\n")


if id34=="__main__":
    id23()