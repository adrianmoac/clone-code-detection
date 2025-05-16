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
            if id31.id33[id38]<=id31.id33[id39]:
                id31.id33[id38]+=id31.id33[id39]
                id31.id33[id39]=id38
            else:
                id31.id33[id39]+=id31.id33[id38]
                id31.id33[id38]=id39
            return True
        return False

    def id40(id31):
        id41=[]
        for id42 in id34(id43(id31.id33)):
            if id31.id33[id42]<0:
                id41.id44((id42,-id31.id33[id42]))
        return id41

def id45():
    id46=id26()
    id41=[]
    id47=[]
    for id42 in id34(id46):
        id19,id37=id17()
        id41.id44((id19,id42))
        id47.id44((id37,id42))
    id41.id48()
    id47.id48()
    id49=[]
    for id42 in id34(1,id46):
        id49.id44((id41[id42][0]-id41[id42-1][0], id41[id42][1], id41[id42-1][1]))
        id49.id44((id47[id42][0]-id47[id42-1][0], id47[id42][1], id47[id42-1][1]))
    id49.id48()
    id50=0
    id51=id29(id46)
    for id52,id53,id54 in id49:
        if id51.id36(id53,id54):
            id50+=id52

    return id50

print(id45())





