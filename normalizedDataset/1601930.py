import id0

# sys.stdin=open('c1.in')


def id1():
    return id2(map(id3, input().split()))


def id4():
    return input().split()


def id5():
    return id3(input())


def id6():
    return input()


def id7():
    id8, id9, id10, id11, id12, id13=id1()
    id14=100*id8
    id15=0
    id16=0
    while 100*id16*id8<=id13:
        id17=0
        while 100*id16*id8+100*id17*id9<=id13:

            id18=100*id16*id8+100*id17*id9
            id19=0
            while id18+id19*id10<=id13 and id19*id10<=id12*(id16*id8+id17*id9):

                id20=id3((id13-id18-id19*id10)/id11)
                id21=id3((id12*(id16*id8+id17*id9)-id19*id10)/id11)
                id22=id23(id20, id21)
                if (id16, id17, id19, id22)!=(0, 0, 0, 0):
                    if True:
                        # rapide
                        id24=id19*id10+id22*id11
                        id25=id18+id24
                        id26=id24/id25
                        id27=id15+id14
                        id28=id15/id27
                        if id26>id28:
                            id15=id24
                            id14=id18
                    else:
                        # trop lent
                        id22=0
                        while id18+id19*id10+id22*id11<=id13 and id19*id10+id22*id11<=id12*(id16*id8+id17*id9):
                            if (id16, id17, id19, id22)==(0, 0, 0, 0):
                                continue
                            id24=id19*id10+id22*id11
                            id25=id18+id24
                            id26=id24/id25
                            id27=id15+id14
                            id28=id15/id27
                            if id26>id28:
                                id15=id24
                                id14=id18
                            id22+=1
                id19+=1
            id17+=1
        id16+=1

    print(id14+id15, id15)


id7()