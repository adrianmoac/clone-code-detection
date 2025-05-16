import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13

id9.id14(10**7)
id15=10**20
id16=1.0/10**10
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
    id34=id18()
    id35=id5.id36(id37)
    for _ in id38(id32):
        id39,id40,id41=id18()
        id35[id39].id42((id40,id41))
        id35[id40].id42((id39,id41))

    # メソッドのみ版
    def id43(id44):
        id45=id5.id36(lambda: id15)
        id45[id44]=0
        id46=[]
        id4.id47(id46, (0, id44))
        id48=id5.id36(id49)
        while id50(id46):
            id51, id52=id4.id53(id46)
            if id48[id52]:
                continue
            id48[id52]=True

            for id54, id55 in id35[id52]:
                if id48[id54]:
                    continue
                id56=id51+id55
                if id45[id54]>id56:
                    id45[id54]=id56
                    id4.id47(id46, (id56, id54))

        return id45
    id57={}
    for id58 in id34:
        id57[id58]=id43(id58)

    id59=id15
    for id60 in id2.id61(id34):
        id62=0
        for id58 in id38(1,id33):
            id62+=id57[id60[id58-1]][id60[id58]]
        if id62<id59:
            id59=id62

    return id59

print(id30())


