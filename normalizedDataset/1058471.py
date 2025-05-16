import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11

id9.id12(10**7)
id13=10**20
id14=10**9+7

def id15(): return id16(map(id17, input().split()))
def id18(): return id17(input())
def id19(): return input().split()
def id20(): return input()

class id21():
    def id22(id23):
        id23.id24=id5.id25(id16)

    def id26(id23, id27, id28, id29):
        id23.id24[id27].id30([id28,id29])
        id23.id24[id28].id30([id27,id29])

    def id31(id23, id27, id28):
        id23.id24[id27]=[_ for _ in id23.id24[id27] if _[0]!=id28]
        id23.id24[id28]=[_ for _ in id23.id24[id28] if _[0]!=id27]

    def id32(id23, id33, id34):
        id29=id5.id25(lambda: id13)
        id29[id33]=0
        id35=[]
        id4.id36(id35, (0, id33))
        id28=id5.id25(id37)
        while id38(id35):
            id39, id27=id4.id40(id35)
            if id28[id27]:
                continue
            if id27==id34:
                return id29[id34]
            id28[id27]=True

            for id41, id42 in id23.id24[id27]:
                if id28[id41]:
                    continue
                id43=id39+id42
                if id29[id41]>id43:
                    id29[id41]=id43
                    id4.id36(id35, (id43, id41))

        return None


def id44():
    id45,id46=id15()
    id47=id21()
    id34=[]
    id48=0
    for _ in id49(id46):
        id50,id51,id52=id15()
        id47.id26(id50,id51,id52)
        id34.id30([id50,id51,id52])
    for id50,id51,id52 in id34:
        id29=id47.id32(id50,id51)
        if id29<id52:
            id48+=1
    return id48


print(id44())