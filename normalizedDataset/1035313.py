import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11

id9.id12(10**7)
id13=10**10
id14=10**9+7


class id15:
    def id16(id17, id18):
        id17.id19=[-1 for _ in id20(id18)]

    def id21(id17, id22):
        if id17.id19[id22]<0:
            return id22
        else:
            id17.id19[id22]=id17.id21(id17.id19[id22])
            return id17.id19[id22]

    def id23(id17, id22, id24):
        id25=id17.id21(id22)
        id26=id17.id21(id24)
        if id25!=id26:
            if id17.id19[id25]<=id17.id19[id26]:
                id17.id19[id25]+=id17.id19[id26]
                id17.id19[id26]=id25
            else:
                id17.id19[id26]+=id17.id19[id25]
                id17.id19[id25]=id26
            return True
        return False

    def id27(id17):
        id28=[]
        for id29 in id20(id30(id17.id19)):
            if id17.id19[id29]<0:
                id28.id31((id29,-id17.id19[id29]))
        return id28

def id32():
    id33,id34,id35=id36(map(id37, input().split()))
    id38=id15(id33)
    id39=id15(id33)
    for _ in id20(id34):
        id40,id41=id36(map(id37, input().split()))
        id38.id23(id40-1,id41-1)
    for _ in id20(id35):
        id40,id41=id36(map(id37, input().split()))
        id39.id23(id40-1,id41-1)

    id42=id5.id43(id44)
    id45=id5.id43(id44)
    id46={}

    for id29 in id20(id33):
        id42[id38.id21(id29)].id47(id29)
        id45[id39.id21(id29)].id47(id29)
    id48=[]
    for id29 in id20(id33):
        if id29 in id46:
            id48.id31(id46[id29])
            continue
        id49=id42[id38.id21(id29)]&id45[id39.id21(id29)]
        id50=id30(id49)
        for id51 in id49:
            id46[id51]=id50
        id48.id31(id46[id29])

    return " ".id52(map(id53, id48))



print(id32())