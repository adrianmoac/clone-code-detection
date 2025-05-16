import id0


class id1(id2):
    @id3
    def id4():
        return input()

    @id3
    def id5():
        id6=id1.id7()
        return id1.id8(id6)

    @id3
    def id9():
        return id1.id4().id10()

    @id3
    def id7():
        return id11(id1.id4().id10())

    @id3
    def id8(id6):
        return id12(map(
            id11,
            id0.split("\s+", id1.id4().id10())))[: id6]


def id13():
    id14=id1.id5()
    print(id15(id14))


def id15(id14):
    """>>>min_cost_from_left_to_right([100, 150, 130, 120])
    40>>>min_cost_from_left_to_right([100, 125, 80, 110])
    40>>>a=[314, 159, 265, 358, 979, 323, 846, 264, 338]>>>min_cost_from_left_to_right(a)
    310
    """
    id16=id17(id14)
    id18(id14, id16)
    return id16[-1]


def id18(id14, id19):
    id19[0]=0
    for id20 in id21(1, id22(id14)):
        for id23 in [1, 2]:
            id24=id20-id23
            if id24<0:
                continue
            id25=id19[id24]+id26(id14[id24]-id14[id20])
            id19[id20]=id27(id19[id20], id25)


def id17(id14):
    id28=10000
    id29=100000
    id30=id28*id29
    id16=[id30]*id22(id14)
    return id16

if id31=="__main__":
    # import doctest
    # doctest.testmod()
    id13()