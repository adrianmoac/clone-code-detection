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
    id31=id27()
    id32=id18()
    id33=[]
    id34=[]
    for id35 in id36(id31):
        id4.id37(id33, id32[id35])
        id4.id37(id34,-id32[id35+id31*2])
    id38=id39(id33)
    id40=id39(id34)
    id41={}
    id41[id31-1]=id38
    for id35 in id36(id31):
        id42=id4.id43(id33)
        if id32[id31+id35]>id42:
            id38-=id42
            id4.id37(id33, id32[id31+id35])
            id38+=id32[id31+id35]
        else:
            id4.id37(id33, id42)
        id41[id31+id35]=id38

    id44={}
    id44[id31*2-1]=id40
    for id35 in id36(id31-1,-1,-1):
        id42=id4.id43(id34)
        if-id32[id31+id35]>id42:
            id40-=id42
            id4.id37(id34,-id32[id31+id35])
            id40-=id32[id31+id35]
        else:
            id4.id37(id34, id42)
        id44[id31+id35-1]=id40


    id45=-id15
    for id46 in id41.id47():
        id48=id41[id46]+id44[id46]
        if id48>id45:
            id45=id48

    return id45



print(id30())
