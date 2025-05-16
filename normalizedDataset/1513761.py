import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13

id9.id14(10**7)
id15=10**20
id16=1.0/10**9
id17=10**9+7

def id18(): return [id19(id20) for id20 in id9.id21.id22().split()]
def id23(): return [id19(id20)-1 for id20 in id9.id21.id22().split()]
def id24(): return [id25(id20) for id20 in id9.id21.id22().split()]
def id26(): return id9.id21.id22().split()
def id27(): return id19(id9.id21.id22())
def id28(): return id25(id9.id21.id22())
def id29(): return input()


class id30():
    def id31(id32, id33):
        id32.id34=id35=id36(id33)
        id32.id37=id38=id36(id33[0])
        id32.id39=id40=id33
        for id41 in id42(id35):
            for id43 in id42(1,id38):
                id40[id41][id43]+=id40[id41][id43-1]

        for id41 in id42(1,id35):
            for id43 in id42(id38):
                id40[id41][id43]+=id40[id41-1][id43]

    def id44(id32, id45, id46, id47, id48):
        if id45>id47 or id46>id48:
            return 0

        id40=id32.id39
        id49=id40[id48][id47]
        if id45>0 and id46>0:
            return id49-id40[id46-1][id47]-id40[id48][id45-1]+id40[id46-1][id45-1]
        if id45>0:
            id49-=id40[id48][id45-1]
        if id46>0:
            id49-=id40[id46-1][id47]

        return id49


def id50():
    id51=id27()
    id52=[id18() for _ in id42(id51)]
    id53=id30(id52)
    id54=[0]*(id51*id51+1)
    for id41 in id42(id51):
        for id43 in id42(id41,id51):
            for id55 in id42(id51):
                for id56 in id42(id55,id51):
                    id57=(id43-id41+1)*(id56-id55+1)
                    id58=id53.id44(id41,id55,id43,id56)
                    if id54[id57]<id58:
                        id54[id57]=id58
    id59=id54[0]
    for id41 in id42(1,id51*id51+1):
        if id54[id41]<id59:
            id54[id41]=id59
        else:
            id59=id54[id41]
    id40=[]
    id60=id27()
    for _ in id42(id60):
        id61=id27()
        id40.id62(id54[id61])

    return "\n".id63(map(id64,id40))


print(id50())
