import id0


# sys.stdin=open('e1.in')


def id1():
    return id2(map(id3, input().split()))


def id4():
    return id3(input())


def id5():
    return input().split()


def id6():
    return input()


id7=False
id8=5600070
if id7:
    print()
    print("N:", id8)
    print()


def id9(id10):
    if id7:
        id11=(id10<=id8 and id12(id10)<=id12(id8)) or (id10>=id8 and id12(id10)>=id12(id8))
        print("?", id10, "\t", id11)
        return id11
    print("?", id10, id13=True)
    return input() in ["y", "Y"]


def id14():
    if id9(10**9):
        # N is a power of 10
        for id15 in id16(10):
            if id9(2*10**id15):
                return 10**id15

    # Find the number of digits of N
    id17=1
    while id9(10**id17):
        id17+=1

    id18=[9]*id17
    for id19 in id16(id17):

        id20=0
        if id19==0:
            id20=1
        id21=9

        id18[id19]=id20
        id10=id3("".id22(map(id12, id18)))
        if id9(10*id10):
            continue

        while id21-id20>1:
            id23=(id20+id21)//2
            id18[id19]=id23
            id10=id3("".id22(map(id12, id18)))
            if id9(10*id10):
                id21=id23
            else:
                id20=id23
        id18[id19]=id21
    id10=id3("".id22(map(id12, id18)))
    return id10


def id24():
    id11=id14()
    print("!", id11, id13=True)


if id25=="__main__":
    id24()