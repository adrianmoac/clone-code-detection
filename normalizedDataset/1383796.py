import id0
from id1 import id2

# sys.stdin=open('d1.in')


def id3():
    return id4(map(id5, input().split()))


def id6():
    return input().split()


def id7():
    return id5(input())


def id8():
    return input()


id9=10
id10=10**20


def id11():
    id12, id13, id14=id3()
    id15=[id3() for id16 in id17(id12)]
    id18=id2(lambda: id10)
    id18[(0, 0)]=0

    for id16, (id19, id20, id21) in id22(id15):
        for id23 in id17(id9*id16,-1,-1):
            for id24 in id17(id9*id16,-1,-1):
                if (id23, id24) in id18:
                    id25=id18[(id23, id24)]
                    if id25+id21<id18[((id23+id19), (id24+id20))]:
                        id18[((id23+id19), (id24+id20))]=id25+id21

    id26=id10
    for id23 in id17(0, id9*id12+1):
        for id24 in id17(0, id9*id12+1):
            if id23==0 and id24==0:
                continue
            if id23*id14==id24*id13:
                if (id23, id24) in id18:
                    id25=id18[(id23, id24)]
                    if id25<id26:
                        id26=id25
    if id26==id10:
        id26=-1
    return id26


def id27():
    id26=id11()
    print(id26)


id27()