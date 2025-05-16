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
    id30,id31,id32=id17()
    id33=[]
    def id34(id19,id35):
        if id19==0:
            return (0,id35)
        if id19==id30:
            return (id30,-id35)
        if id35==0:
            return (id30+1,-id19)
        return (1, id19)

    for _ in id36(id32):
        id37,id38,id39,id40=id17()
        if (0<id37<id30 and 0<id38<id31) or (0<id39<id30 and 0<id40<id31):
            continue
        id33.id41((id34(id37,id38),_))
        id33.id41((id34(id39,id40),_))
    id33.id42()
    id43=[id33[id44][1] for id44 in id36(id45(id33))]
    id46=[None]*(id45(id43))
    id47=-1
    for id48 in id43:
        if id47<-1:
            id47+=1
            id46[0]=id48
            continue
        if id46[id47]==id48:
            id47-=1
        else:
            id47+=1
            id46[id47]=id48

    if id47>1:
        return "NO"
    return "YES"

print(id29())





