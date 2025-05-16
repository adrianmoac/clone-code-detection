import id0

# sys.stdin=open('f1.in')


def id1():
    return id2(map(id3, input().split()))


def id4():
    return id3(input())


def id5():
    return input().split()


def id6():
    return input()


def id7():
    id8=id4()
    id9=id4()
    id10=id1()
    id11=id4()
    id12=0
    id13=-1
    id14=0
    id15=id8
    id16=0
    id17=0
    id18=[0]*id11
    for id19 in id20(id11):
        id21, id22=id1()
        while id12<id9 and id10[id12]<id21:
            id23=id10[id12]-id17
            id16+=id23*id13
            if id16<0:
                id14+=id24(id16)
                if id14>id15:
                    id14=id15
                id16=0
            if id16+id15-id14>id8:
                id25=(id16+id15-id14)-id8
                id15-=id25
                if id15<id14:
                    id15=id14
            if id16>id8:
                id16=id8
            id17=id10[id12]
            id12+=1
            id13*=-1
        id23=id21-id17
        if id22<=id14:
            id26=id16
        elif id22<=id15:
            id26=id16+id22-id14
        else:
            id26=id16+id15-id14
        id26+=id23*id13
        if id26<0:
            id26=0
        if id26>id8:
            id26=id8
        id18[id19]=id26
    return id18


def id27():
    id26=id7()
    print(*id26, id28="\n")


if id29=="__main__":
    id27()