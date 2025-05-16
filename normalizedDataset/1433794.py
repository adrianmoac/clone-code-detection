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
        id31[id35].id37(id36)
        id31[id36].id37(id35)

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

            for id49 in id31[id47]:
                id50=1
                if id43[id49]:
                    continue
                id51=id46+id50
                if id40[id49]>id51:
                    id40[id49]=id51
                    id4.id42(id41, (id51, id49))

        return id40

    id52=id38(1)
    id53=id38(id30)
    id54=-1
    for id55 in id34(2,id30):
        if id52[id55]<=id53[id55]:
            id54+=1
        else:
            id54-=1

    if id54>=0:
        return "Fennec"

    return "Snuke"


print(id29())


