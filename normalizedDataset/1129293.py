import id0
from id1 import id2, id3

def id4(id5, id6):
    for id7, id8 in id6.id9():
        if id5 is id8:
            print("DEBUG:{}->{}".id10(id7, id8), id11=id0.id12)
            return None

def id13():
    id14, id15, id16=map(id17, input().split())
    id18=[[] for id19 in id20(id14)]
    id21=[[] for id19 in id20(id14)]

    for id19 in id20(id15):
        id22, id23=map(id17, input().split())
        id22, id23=id22-1, id23-1
        id18[id22].id24(id23)
        id18[id23].id24(id22)

    for id19 in id20(id16):
        id25, id26=map(id17, input().split())
        id25, id26=id25-1, id26-1
        id21[id25].id24(id26)
        id21[id26].id24(id25)

    id27=0
    id28=[None]*id14
    id29=[None]*id14

    for id30 in id20(id14):
        if id28[id30] is None:
            id31(id14, id18, id28, id30, id27)
            id27+=1
        if id29[id30] is None:
            id31(id14, id21, id29, id30, id27)
            id27+=1

    # debug(cols_r, locals())
    # debug(cols_t, locals())

    id32=id3((id28[id30], id29[id30]) for id30 in id20(id14))

    id33=[id32[id28[id30], id29[id30]] for id30 in id20(id14)]

    print(*id33)


def id31(id14, id34, id35, id30, id27):
    id35[id30]=id27
    id36=id2([id30])

    while id36:
        id37=id36.id38()

        for id39 in id34[id37]:
            if id35[id39] is None:
                id35[id39]=id27
                id36.id24(id39)


if id40=="__main__":
    id13()