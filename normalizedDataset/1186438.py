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

def id26(id27, id28, id29):
    id30=-1
    while id29>id28:
        id30=(id29+id28)//2
        if id27(id30):
            id28=id30+1
        else:
            id29=id30
    if id27(id30):
        return id30
    return id30-1

def id31():
    id32,id33=id15()
    id34=[id35(id15()) for _ in id36(id32)]
    if id37(map(lambda id17: id17[1]<=1000, id34)):
        id38=[0]*200000
        id34=id39(id34, id40=lambda id17: (id17[1],id17[0]))
        id41=0
        for id42,id43 in id34:
            for id44 in id36(id41,-1,-1):
                if id38[id44]+id42>id38[id44+id43]:
                    id38[id44+id43]=id38[id44]+id42
            id41+=id43
        return id45(id38[:id46(id33+1, 200000)])

    if id37(map(lambda id17: id17[0]<=1000, id34)):
        id38=[id13]*200000
        id38[0]=0
        id34=id39(id34)
        id41=0
        for id42,id43 in id34:
            for id44 in id36(id41,-1,-1):
                if id38[id44]+id43<id38[id44+id42]:
                    id38[id44+id42]=id38[id44]+id43
            id41+=id42
        return id45([id44 for id44 in id36(200000) if id38[id44]<=id33])

    id47=id48(id34)//2
    id49=id34[:id47]
    id50=id34[id47:]

    def id27(id34):
        id51=id52()
        id51.id53((0,0))
        for id44 in id36(id48(id34)):
            id54,id55=id34[id44]
            id38=id52()
            id38.id53((id55,id54))
            for id42 in id51:
                id38.id53((id42[0]+id55,id42[1]+id54))
            id51|=id38
        id56=id39(id57(id51))
        return id57(id56[id44] for id44 in id36(id48(id56)) if (id44<1 or id56[id44-1][1]<id56[id44][1]))

    id58=id27(id49)
    id59=id27(id50)
    id60=id48(id58)
    id51=0
    for id42 in id59:
        id44=id8.id61(id58, (id33-id42[0], id13))
        if id44==0:
            continue
        if id51<id42[1]+id58[id44-1][1]:
            id51=id42[1]+id58[id44-1][1]

    return id51


print(id31())