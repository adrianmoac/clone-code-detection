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

class id29():
    def id30(id31, id32):
        id31.id33=id34=[True]*(id32+1)
        id34[0]=id34[1]=False
        id31.id35=id36=[]
        for id37 in id38(2, id18(id0.id39(id32))+1):
            if not id34[id37]:
                continue
            id36.id40(id37)
            for id41 in id38(id37*id37,id32+1,id37):
                id34[id41]=False

    def id42(id31, id32):
        return id31.id33[id32]

    def id43(id31, id32):
        id44=id5.id45(id18)
        for id46 in id31.id35:
            while id32%id46==0:
                id44[id46]+=1
                id32//=id46
            if id32<2:
                break
        if id32>1:
            id44[id32]+=1
        return id44.id47()

    def id48(id31, id32):
        id49=1
        for id50,id51 in id31.id43(id32):
            id36=1
            for id37 in id38(1,id51+1):
                id36+=id0.id52(id50, id37)
            id49*=id36
        return id49

def id53():
    id32=id26()
    id54=id29(id18(id0.id39(id32))+5)
    id36=id54.id48(id32)-id32
    if id32==id36:
        return "Perfect"
    if id32>id36:
        return "Deficient"

    return "Abundant"


print(id53())