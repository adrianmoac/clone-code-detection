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
    id30,id31=id25()
    id32=id26()
    if id30==id31:
        return "\n".id33(["0", id30, id31])
    id34=[id28() for _ in id35(id32)]
    id36=[id30,id31]
    id37=id38(id36)
    for id39 in id34:
        if id39 in id37:
            continue
        id36.id40(id39)
        id37.id41(id39)

    id42=id5.id43(id44)
    id45=id46(id36)
    id47=id46(id30)
    def id48(id49,id50):
        id51=0
        for id52 in id35(id47):
            if id49[id52]!=id50[id52]:
                id51+=1
                if id51>1:
                    return False
        return True

    for id52 in id35(id45):
        id49=id36[id52]
        for id53 in id35(id52+1,id45):
            if id48(id49, id36[id53]):
                id42[id52].id40((id53,1))
                id42[id53].id40((id52,1))

    def id54(id39):
        id55=id5.id43(lambda: [id15,-1])
        id55[id39]=[0,-1]
        id56=[]
        id4.id57(id56, (0, id39))
        id58=id5.id43(id59)
        while id46(id56):
            id60, id61=id4.id62(id56)
            if id58[id61]:
                continue
            id58[id61]=True

            for id63, id64 in id42[id61]:
                if id58[id63]:
                    continue
                id65=id60+id64
                if id55[id63][0]>id65:
                    id55[id63]=[id65,id61]
                    id4.id57(id56, (id65, id63))

        return id55

    id55=id54(0)
    if id55[1][0]==id15:
        return-1
    id66=[]
    id67=1
    while id55[id67][1]>=0:
        id66.id40(id36[id67])
        id67=id55[id67][1]
    id66.id40(id30)
    id66.id40(id68(id55[1][0]-1))
    id66.id69()

    return "\n".id33(id66)



print(id29())


