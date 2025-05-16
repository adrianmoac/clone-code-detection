import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11

id9.id12(10**7)
id13=10**20
id14=10**9+7

def id15(): return id16(map(id17, input().split()))
def id18(): return id16(map(id19, input().split()))
def id20(): return id17(input())
def id21(): return input().split()
def id22(): return input()


class id23:
    def id24(id25, id26):
        id25.id27=[-1 for _ in id28(id26)]

    def id29(id25, id30):
        if id25.id27[id30]<0:
            return id30
        else:
            id25.id27[id30]=id25.id29(id25.id27[id30])
            return id25.id27[id30]

    def id31(id25, id30, id32):
        id33=id25.id29(id30)
        id34=id25.id29(id32)
        if id33!=id34:
            if id25.id27[id33]<=id25.id27[id34]:
                id25.id27[id33]+=id25.id27[id34]
                id25.id27[id34]=id33
            else:
                id25.id27[id34]+=id25.id27[id33]
                id25.id27[id33]=id34


def id35():
    id36,id37=id15()
    id38=id39([id15() for _ in id28(id37)], id40=lambda id30:-id30[2])
    id41=id20()
    id42=id39([id15()+[_] for _ in id28(id41)], id40=lambda id30:-id30[1])
    id43=id23(id36+1)
    id44=[1]*id41
    id45=id38[0][2]
    id46=0
    for id47,id32,id48 in id42:
        while id45>id32:
            id43.id31(id38[id46][0],id38[id46][1])
            if id46<id37-1:
                id46+=1
                id45=id38[id46][2]
            else:
                id46=-1
                id45=-id13

        id44[id48]=-id43.id27[id43.id29(id47)]

    return "\n".id49(map(id50, id44))

print(id35())