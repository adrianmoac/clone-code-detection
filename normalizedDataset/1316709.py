# coding: utf-8
def id0():
    return input().split()


def id1():
    return id2(map(id3, id0()))


id4=5


class id5:
    def id6(id7, id8, id9):
        id7.id8=id8
        id7.id9=id9


    def id10(id7, id11):
        id12=id7.id9+id11
        id13=id7.id8+(id12//60)
        return id5(id13, id12%60)

    
    def id14(id7):
        id15=id7.id9%5
        return id5(id7.id8, id7.id9-id15)


    def id16(id7):
        id17=-(id7.id9%(-5))
        return id7.id10(id17)


    def id18(id7, id19):
        if id7.id8>id19.id8:
            return True
        if id7.id8==id19.id8 and id7.id9>id19.id9:
            return True
        return False


    def id20(id7, id19):
        if id7.id8<id19.id8:
            return True
        if id7.id8==id19.id8 and id7.id9<id19.id9:
            return True
        return False


    def id21(id7):
        return id5(id7.id8, id7.id9)


    def id22(id7):
        return ("%02d"%id7.id8)+("%02d"%id7.id9)


    def id23(id7, id19):
        return id7.id8==id19.id8 and id7.id9==id19.id9


    def id24(id7):
        return id7.id8*60+id7.id9


class id25:
    def id6(id7, id26, id27):
        id7.id28=id26.id14()
        id7.id29=id27.id16()


    def id30(id7, id19):
        return (id19.id18(id7.id28) or id19.id23(id7.id28)) and\
        id19.id20(id7.id29)


    def id31(id7, id32):
        if id7.id28.id18(id32.id28):
            return id32.id31(id7)
        return id7.id29.id18(id32.id28) or id7.id29.id23(id32.id28)


    def id22(id7):
        return id7.id28.id22()+"-"+id7.id29.id22()


def id33(id34):
    id35=id3(id34[:2])
    id36=id3(id34[2:4])
    id37=id3(id34[5:7])
    id38=id3(id34[7:9])
    return id25(id5(id35, id36), id5(id37, id38))


def id39(id40, id41):
    if id40.id28.id18(id41.id28):
        return id39(id41, id40)
    id27=id42(id40.id29, id41.id29, id43=lambda id19: id19.id24())
    return id25(id40.id28, id27)


def id44():
    id45=id2()
    id46=id1()[0]

    for _ in id47(id46):
        id45.id48(id33(id0()[0]))
    
    id19=id5(0, 0)
    id49=id5(24, 0)
    id50=id51(id45, id43=lambda id52: id52.id28.id24())
    
    id53=0
    while id53<id54(id50)-1:
        id55=id50[id53]
        id56=id50[id53+1]
        if id55.id31(id56):
            id57=id39(id55, id56)
            id50.id58(id53)
            id50.id58(id53)
            id50.id59(id53, id57)
        else:
            id53+=1

    for id52 in id50:
        print(id52.id22())


id44()