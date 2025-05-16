from id0 import id1
from id2 import id3
from id4 import id5
from id0 import id6
id7=10**15


id8=[0,-1, 0, 1]
id9=[1, 0,-1, 0]


def id10(id11: id12, id13: id12, id14: id12, id15: id12)->id16:
    return 0<=id11<id14 and 0<=id13<id15


def id17(id18: id12, id19: id12, id20: id12, id21: id12, id22: id23, id13: id12):
    id24=id6()
    id24.id25((id18, id19, 0))

    id26=[[id7]*id27(id22[0]) for _ in id28(id27(id22))]

    while id27(id24)!=0:
        id29, id30, id31=id24.id32()

        # 近傍に遷移
        for id33 in id28(id27(id8)):
            id34, id35=id29+id8[id33], id30+id9[id33]

            if id10(id34, id35, id27(id22), id27(id22[0])) and id22[id34][id35] in (".", "#", "G"):
                id36=id31+(id13 if id22[id34][id35]=="#" else 1)

                if id36<id26[id34][id35]:
                    id26[id34][id35]=id36
                    id24.id25((id34, id35, id36))

    return id26[id20][id21]


def id37():
    id14, id15, id38=map(id12, input().split())
    id22=[]
    id18, id19=None, None
    id20, id21=None, None
    for id11 in id28(id14):
        id39=input()
        id22.id25(id39)
        if "S" in id39:
            id18, id19=id11, id39.id40("S")
        if "G" in id39:
            id20, id21=id11, id39.id40("G")

    # [low, high)
    id41, id42, id43=-1, 10**10,-1
    while id42-id41>1:
        id44=(id41+id42)//2
        if id17(id18, id19, id20, id21, id22, id44)<=id38:
            id43=id44
            id41=id44
        else:
            id42=id44

    print(id43)


if id45=="__main__":
    id37()