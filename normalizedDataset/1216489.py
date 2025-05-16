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


def id28():
    id29=id25()
    id30=[[] for _ in id31(id29)]
    for _ in id31(id29-1):
        id18,id32=id21()
        id30[id18].id33(id32)
        id30[id32].id33(id18)

    id34=[[] for _ in id31(id29)]
    id35=[-1]*id29
    id36=[]
    id37=[2**id38 for id38 in id31(20)]

    def id39(id38):
        id40=id41(id36)
        id35[id38]=id40
        id42=0
        while id37[id42]<=id40:
            id34[id38].id33(id36[id40-id37[id42]])
            id42+=1
        id36.id33(id38)
        for id43 in id30[id38]:
            if id35[id43]>=0:
                continue
            id39(id43)
        del id36[-1]

    id39(0)

    id44=id25()
    id45=[]
    for _ in id31(id44):
        id46,id47=id21()
        if id35[id46]>id35[id47]:
            id46,id47=id47,id46
        id48=id35[id46]+id35[id47]
        id49=id35[id47]-id35[id46]
        while id49>0:
            id38=1
            while id37[id38]<id49:
                id38+=1
            id38-=1
            id47=id34[id47][id38]
            id49-=id37[id38]
        while id46!=id47:
            id38=1
            id50=id41(id34[id46])
            while id50>id38 and id34[id46][id38]!=id34[id47][id38]:
                id38+=1
            id38-=1
            id46=id34[id46][id38]
            id47=id34[id47][id38]
        id45.id33(id51(id48-id35[id46]*2+1))

    return "\n".id52(id45)

print(id28())