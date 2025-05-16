import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11

id9.id12(10**7)
id13=10**20
id14=10**9+7

def id15(): return id16(map(id17, input().split()))
def id18(): return id16(map(id19, input().split()))
def id20(): return id17(input())
def id21(): return input().split()
def id22(): return input()


class id23():
    id24=2**20

    def id25(id26, id27, id28):
        id26.id24=id27
        id29=[[id28]*id27]
        for id30 in id31(1, 100):
            if id32(id29[id30-1])==1:
                break
            id33=id29[-1]
            id34=id32(id33)//2
            id35=[id26.id36(id33[id37*2], id33[id37*2+1]) for id37 in id31(id34)]
            id29.id38(id35)
        id26.id29=id29

    def id39(id26, id30, id40):
        id26.id29[0][id30]=id40
        id34=id32(id26.id29)
        for id37 in id31(1, id34):
            id30//=2
            id26.id29[id37][id30]=id26.id36(id26.id29[id37-1][id30*2], id26.id29[id37-1][id30*2+1])

    def id36(id26, id35, id41):
        return (id35[0]*id41[0], id35[1]*id41[0]+id41[1])

    def id42(id26, id40):
        id35=id26.id29[-1][0]
        return id40*id35[0]+id35[1]


def id43():
    id27,id44=id15()
    id29=[id18() for _ in id31(id44)]
    id45=id46(id16(map(lambda id40: id40[0], id29)))
    id47=id16(id45)
    id47.id48()
    id49={}
    for id30 in id31(id32(id47)):
        id49[id47[id30]]=id30

    id50=id23(2**17, (1,0))

    id51=id52=id50.id42(1)
    for id53,id35,id41 in id29:
        id50.id39(id49[id53], (id35, id41))
        id54=id50.id42(1)
        if id51>id54:
            id51=id54
        elif id52<id54:
            id52=id54
    return "\n".id55(id16(map(id56, [id51,id52])))

print(id43())