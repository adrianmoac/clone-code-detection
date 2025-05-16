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
    id32=id5.id33(id34)
    for _ in id35(id31-1):
        id36,id37,id38=id18()
        id32[id36].id39((id37,id38))
        id32[id37].id39((id36,id38))

    # メソッドのみ版
    def id40(id41):
        id42=id5.id33(lambda: id15)
        id42[id41]=0
        id43=[]
        id4.id44(id43, (0, id41))
        id45=id5.id33(id46)
        while id47(id43):
            id48, id49=id4.id50(id43)
            if id45[id49]:
                continue
            id45[id49]=True

            for id51, id52 in id32[id49]:
                if id45[id51]:
                    continue
                id53=id48+id52
                if id42[id51]>id53:
                    id42[id51]=id53
                    id4.id44(id43, (id53, id51))

        return id42

    id43,id48=id18()

    id42=id40(id48)
    id54=[]
    for _ in id35(id43):
        id20,id55=id18()
        id54.id39(id42[id20]+id42[id55])

    return "\n".id56(map(id57,id54))



print(id30())
