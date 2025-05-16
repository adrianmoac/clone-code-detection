import id0
from id1 import id2

# sys.stdin=open('e1.in')


def id3():
    return id4(map(id5, input().split()))


def id6():
    return id5(input())


def id7():
    return input().split()


def id8():
    return input()


def id9(id10, id11):
    if id11==0:
        return id10
    return id9(id11, id10%id11)


def id12():
    def id13(id14, id15, id16, id17):
        return id14*id17==id16*id15

    def id18(id19, id20, id21):
        return id13(id22[id20]-id22[id19], id23[id20]-id23[id19], id22[id21]-id22[id19], id23[id21]-id23[id19])

    id24=id6()
    id25=998244353
    id26=id27(2, id24, id25)-id24-1
    id22, id23=id28(*[id3() for id19 in id29(id24)])
    id30=id2(id31)
    for id19 in id29(id24):
        for id20 in id29(id19+1, id24):
            id10=id23[id19]-id23[id20]
            id11=id22[id20]-id22[id19]
            id32=id9(id10, id11)
            id10//=id32
            id11//=id32
            if id10<0 or (id10==0 and id11<0):
                id10, id11=-id10,-id11
            id33=-(id10*id22[id19]+id11*id23[id19])
            id30[(id10, id11, id33)].id34(id19)
            id30[(id10, id11, id33)].id34(id20)
    for id21, id35 in id30.id36():
        id37=id38(id35)
        id26-=id27(2, id37, id25)-id37-1
    id26%=id25
    return id26


def id39():
    id26=id12()
    print(id26)


if id40=="__main__":
    id39()