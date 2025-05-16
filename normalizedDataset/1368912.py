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

def id29(id30):
    id31=id16-2
    id32=1
    while id31>0:
        if id31%2==1:
            id32=id32*id30%id16
        id30=id30*id30%id16
        id31>>=1
    return id32

def id33(id31, id34):
    if id34>id31-id34:
        id34=id31-id34
    id32=1
    for id35 in id36(id31, id31-id34,-1):
        id32=id32*id35%id16
    id37=1
    for id35 in id36(1, id34+1):
        id37=id37*id35%id16
    return id32*id29(id37)%id16


def id38():
    id39=id26()
    id30=id17()
    id32=1
    id40=0
    id34=0
    for id41 in id30:
        if id41<0:
            id40+=1
            continue
        if id40>0:
            id31=id41-id34
            id42=id33(id31+id40,id31)
            id32*=id42
            id32%=id16
        id34=id41
        id40=0
    return id32

print(id38())





