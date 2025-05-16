import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12

id9.id13(10**7)
id14=10**20
id15=10**9+7

def id16(): return [id17(id18) for id18 in id9.id19.id20().split()]
def id21(): return [id17(id18)-1 for id18 in id9.id19.id20().split()]
def id22(): return [id23(id18) for id18 in id9.id19.id20().split()]
def id24(): return id9.id19.id20().split()
def id25(): return id17(id9.id19.id20())
def id26(): return id23(id9.id19.id20())
def id27(): return input()

class id28():
    def id29(id30):
        id30.id31=id5.id32(id33)

    def id34(id30, id35, id36, id37):
        id30.id31[id35].id38([id36,id37])
        id30.id31[id36].id38([id35,id37])

    def id39(id30, id35, id36):
        id30.id31[id35]=[_ for _ in id30.id31[id35] if _[0]!=id36]
        id30.id31[id36]=[_ for _ in id30.id31[id36] if _[0]!=id35]

    def id40(id30, id41):
        id37=id5.id32(lambda: id14)
        id37[id41]=0
        id42=[]
        id4.id43(id42, (0, id41))
        id36=id5.id32(id44)
        while id45(id42):
            id46, id35=id4.id47(id42)
            if id36[id35]:
                continue
            id36[id35]=True

            for id48, id49 in id30.id31[id35]:
                if id36[id48]:
                    continue
                id50=id46+id49
                if id37[id48]>id50:
                    id37[id48]=id50
                    id4.id43(id42, (id50, id48))

        return id51(id37.id52())

def id53():
    id54,id55=id16()
    id56=id28()
    for _ in id57(id55):
        id58,id59,id60=id16()
        id56.id34(id58,id59,id60)

    id61=[id56.id40(id62) for id62 in id57(1,id54+1)]

    return id63(id61)

print(id53())