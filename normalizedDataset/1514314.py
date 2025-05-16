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


def id30():
    id31,id32,id33=id18()
    id34=id15

    def id35(id36, id37):
        id38={}
        for id39 in id40(-600, 601):
            id41=id42(id39)
            if id39<=0:
                id38[id39+id37]=(id41+id41+id36-1)*id36//2
                continue
            id43=id36-id41
            id44=id45(id36,id41)
            id38[id39+id37]=(id41+id41-id44+1)*id44//2
            if id43>0:
                id38[id39+id37]+=(id43-1)*id43//2
        return id38

    id38=id35(id31,-100)
    id46=id35(id32,0)
    id47=id35(id33,100)

    id48=id15
    for id41,id49 in id50(id38.id51()):
        if id49>id48:
            id38[id41]=id48
        else:
            id48=id49

    id48=id15
    for id41,id49 in id50(id47.id51(), id52=True):
        if id49>id48:
            id47[id41]=id48
        else:
            id48=id49

    for id41 in id40(-250,251):
        id53=id46[id41]
        id53+=id38[id41-id32]
        id53+=id47[id41+id33]
        if id53<id34:
            id34=id53

    return id34



print(id30())
