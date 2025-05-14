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
        id31.id33=id34=id18(id0.id35(id32))+10
        id31.id36=id37=[True]*id34
        id37[0]=id37[1]=False
        id31.id38=id39=[]
        for id40 in id41(2, id18(id0.id35(id34))+1):
            if not id37[id40]:
                continue
            id39.id42(id40)
            for id43 in id41(id40*id40,id34,id40):
                id37[id43]=False

    def id44(id31, id32):
        return id31.id36[id32]

    def id45(id31, id32):
        id46=id5.id47(id18)
        for id48 in id31.id38:
            while id32%id48==0:
                id46[id48]+=1
                id32//=id48
            if id32<2:
                break
        if id32>1:
            id46[id32]+=1
        return id46.id49()

    def id50(id31, id32):
        id51=1
        for id52,id53 in id31.id45(id32):
            id39=1
            for id40 in id41(1,id53+1):
                id39+=id0.id54(id52, id40)
            id51*=id39
        return id51

def id55():
    id32=id26()
    id56=id29(id32)
    id39=id56.id50(id32)-id32
    if id32==id39:
        return "Perfect"
    if id32>id39:
        return "Deficient"

    return "Abundant"


print(id55())