import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11

id9.id12(10**7)
id13=10**20
id14=10**9+7

def id15(): return [id16(id17) for id17 in id9.id18.id19().split()]
def id20(): return [id21(id17) for id17 in id9.id18.id19().split()]
def id22(): return id9.id18.id19().split()
def id23(): return id16(id9.id18.id19())
def id24(): return id21(id9.id18.id19())
def id25(): return input()


def id26():
    id27,id28,id29=id15()
    id30=id15()
    id31=id5.id32(id33)
    id34=id5.id32(id33)
    for _ in id35(id28):
        id36,id37,id38=id15()
        id31[id36-1].id39((id37-1,id38))
        id34[id37-1].id39((id36-1,id38))

    id40=[id13]*id27
    id40[0]=0
    id41=[]
    id4.id42(id41, (0, 0))
    id43=id5.id32(id44)
    while id45(id41):
        id46, id47=id4.id48(id41)
        if id43[id47]:
            continue
        id43[id47]=True

        for id49, id50 in id31[id47]:
            if id43[id49]:
                continue
            id51=id46+id50
            if id40[id49]>id51:
                id40[id49]=id51
                id4.id42(id41, (id51, id49))

    id52=[id13]*id27
    id52[0]=0
    id41=[]
    id4.id42(id41, (0, 0))
    id43=id5.id32(id44)
    while id45(id41):
        id46, id47=id4.id48(id41)
        if id43[id47]:
            continue
        id43[id47]=True

        for id49, id50 in id34[id47]:
            if id43[id49]:
                continue
            id51=id46+id50
            if id52[id49]>id51:
                id52[id49]=id51
                id4.id42(id41, (id51, id49))

    id28=0
    for id53 in id35(id27):
        id54=id29-id40[id53]-id52[id53]
        if id54<1:
            continue
        if id54*id30[id53]>id28:
            id28=id54*id30[id53]

    return id28


print(id26())