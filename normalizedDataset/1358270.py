import id0


# sys.stdin=open('d1.in')


def id1():
    return id2(map(id3, input().split()))


def id4():
    return input().split()


def id5():
    return id3(input())


def id6():
    return input()


id7={}
id8={}


def id9(id10, id11):
    if (id10, id11) in id7:
        return id7[(id10, id11)]
    for id12 in id13(2, id10+1, 2):
        id14=id12//2
        if not id9(id10-2*id14, id11+id14):
            id15=True
            id7[(id10, id11)]=id15
            id8[id10, id11]=id10-2*id14, id11+id14
            return id15
    for id12 in id13(2, id11+1, 2):
        id14=id12//2
        if not id9(id10+id14, id11-2*id14):
            id15=True
            id7[(id10, id11)]=id15
            id8[id10, id11]=id10+id14, id11-2*id14
            return id15
    id15=False
    id7[(id10, id11)]=id15
    return id15


def id16(id10, id11):
    return id17(id10-id11)>=2


def id18(id19):
    for id10 in id13(id19):
        for id11 in id13(id19):
            if id9(id10, id11):
                print(id10, id11, "     ", id8[id10, id11])


def id20():
    id10, id11=id1()
    id15=id16(id10, id11)
    if id15:
        print("Alice")
    else:
        print("Brown")


# test(10)
id20()