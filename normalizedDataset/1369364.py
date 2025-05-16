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


def id29(id30, id31, id32):
    id33=-1
    while id32>id31:
        id33=(id32+id31)//2
        if id30(id33):
            id31=id33+1
        else:
            id32=id33
    if id30(id33):
        return id33+1
    return id33


def id34():
    id35=id26()
    id36=id26()
    id37=[id17() for _ in id38(id36)]

    def id30(id39):
        id40=0
        for id41,id42 in id37:
            if id41>id39:
                continue
            id40+=(id39-id41+id42)//id42
        return id40<id35

    id43=id29(id30,0,10**12)
    id39=id43-1
    id40=0
    id44=0
    for id41,id42 in id37:
        if id41>id39:
            continue
        id45=(id39-id41+id42)//id42
        id40+=id45
        id44+=id41*id45
        id46=id45
        id44+=(id46*(id46-1)//2)*id42
    id44+=(id35-id40)*id43


    return id44

print(id34())





