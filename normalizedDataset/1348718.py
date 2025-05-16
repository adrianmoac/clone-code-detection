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


class id29:
    def id30(id31, id32):
        id31.id33=[-1 for _ in id34(id32)]

    def id35(id31, id19):
        if id31.id33[id19]<0:
            return id19
        else:
            id31.id33[id19]=id31.id35(id31.id33[id19])
            return id31.id33[id19]

    def id36(id31, id19, id37):
        id38=id31.id35(id19)
        id39=id31.id35(id37)
        if id38!=id39:
            if id38<id39:
                id31.id33[id38]+=id31.id33[id39]
                id31.id33[id39]=id38
            else:
                id31.id33[id39]+=id31.id33[id38]
                id31.id33[id38]=id39
            return True
        return False

    def id40(id31):
        id41=id5.id42(id43)
        for id44 in id34(id45(id31.id33)):
            id46=id31.id35(id44)
            id41[id46].id47(id44)
        return id41.id48()

def id49():
    id50=id26()
    id38=[id51 for id51 in id28()]
    id39=[id51 for id51 in id28()]
    id52=id29(36)
    id41=id5.id42(id18)
    for id44 in id34(id50):
        id53=id18(id38[id44], 36)
        id54=id18(id39[id44], 36)
        if id41[id53]==0:
            id41[id53]=id44+1
        if id41[id54]==0:
            id41[id54]=id44+1
        id52.id36(id53, id54)

    id55=1
    for id56,id57 in id52.id40():
        id46=id58([id41[id51] for id51 in id57])
        if id56<10:
            continue
        if id46==0:
            continue
        if id46==1:
            id55*=9
        else:
            id55*=10

    return id55


print(id49())