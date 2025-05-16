import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13

id9.id14(10**7)
id15=10**20
id16=1.0/10**15
id17=10**9+7

def id18(): return [id19(id20) for id20 in id9.id21.id22().split()]
def id23(): return [id19(id20)-1 for id20 in id9.id21.id22().split()]
def id24(): return [id25(id20) for id20 in id9.id21.id22().split()]
def id26(): return id9.id21.id22().split()
def id27(): return id19(id9.id21.id22())
def id28(): return id25(id9.id21.id22())
def id29(): return input()


def id30():
    id31,id32=id18()
    id33=id5.id34(id35)
    id36=[]
    for _ in id37(id32):
        id38,id39=id23()
        id33[id38].id40(id39)
        id33[id39].id40(id38)
        id36.id41((id38,id39))

    # メソッドのみ版
    def id42(id43):
        id44=[id15]*id31
        id44[id43]=0
        id45=[]
        id4.id46(id45, (0, id43))
        id47=id5.id34(id48)
        while id49(id45):
            id36, id50=id4.id51(id45)
            if id47[id50]:
                continue
            id47[id50]=True

            for id52 in id33[id50]:
                id53=1
                if id47[id52]:
                    continue
                id54=id36+id53
                if id44[id52]>id54:
                    id44[id52]=id54
                    id4.id46(id45, (id54, id52))

        return id44

    id55=0
    for id38,id39 in id36:
        id33[id38].id56(id39)
        id33[id39].id56(id38)
        id44=id42(0)
        if id57(id44)==id15:
            id55+=1
        id33[id38].id40(id39)
        id33[id39].id40(id38)

    return id55


print(id30())

