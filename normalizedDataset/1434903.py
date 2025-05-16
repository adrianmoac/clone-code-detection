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


def id29(id30): return id31(id30)
def id32(): return id29(id26())

class id31():
    def id33(id34, id30):
        id34.id30=id30

    def id35(id34, id19):
        id19=id31.id36(id19)
        return id31((id34.id30+id19)%id16)

    def id37(id34, id19):
        id19=id31.id36(id19)
        return id31((id34.id30-id19)%id16)

    def id38(id34, id19):
        id19=id31.id36(id19)
        return id31((id34.id30*id19)%id16)

    def id39(id34, id19):
        id19=id31.id36(id19)
        return id31(id34.id30*id40(id19, id16-2, id16)%id16)

    @id41
    def id36(id42, id19):
        if id43(id19, id31):
            return id19.id30
        return id19

    def id44(id34):
        return id45(id34.id30)

def id46():
    id30,id47=id17()
    id48=id22()
    id49=[0]*(id47*2)
    id50=[[] for _ in id51(id47*2)]
    id52=0
    for id53 in id51(1,id30):
        id54=id48[id53-1]
        id55=id48[id53]
        if id55<id54:
            id55+=id47
        id49[id54+2]+=1
        id50[id55].id56(id55-id54-1)
        id52+=id55-id54

    id57=[0]*(id47*2)
    id58=0
    id59=0
    for id53 in id51(1,id47*2):
        id58+=id49[id53]
        id59+=id58
        id57[id53]+=id59
        for id60 in id50[id53]:
            id58-=1
            id59-=id60
    for id53 in id51(id47):
        id57[id53]+=id57[id53+id47]

    return id52-id61(id57)

print(id46())


