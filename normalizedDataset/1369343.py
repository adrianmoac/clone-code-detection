import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13

id9.id14(10**7)
id15=10**20
id16=10**9+7

def id17(): return [id18(id19) for id19 in id9.id20.id21().split()]
def id22(): return [id18(id19)-1 for id19 in id9.id20.id21().split()]
def id23(): return [id24(id19) for id19 in id9.id20.id21().split()]
def id25(): return id9.id20.id21().split()
def id26(): return id18(id9.id20.id21())
def id27(): return id24(id9.id20.id21())
def id28(): return input()


def id29():
    id30=id26()
    id31=id5.id32(id33)
    for _ in id34(id30-1):
        id35,id36=id17()
        id31[id35].id37((id36, 1))
        id31[id36].id37((id35, 1))

    def id38(id39):
        id40=id5.id32(lambda: id15)
        id40[id39]=0
        id41=[]
        id4.id42(id41, (0, id39))
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

        return id40

    def id52(id40):
        id53=-1
        id54=0
        for id46,id43 in id40.id55():
            if id53<id43:
                id53=id43
                id54=id46
        return id54

    id56=id38(1)
    id57=id52(id56)
    id58=id52(id38(id57))

    return "{} {}".id59(id57,id58)

print(id29())





