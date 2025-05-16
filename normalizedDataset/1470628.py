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


def id7(id8, id9):
    return (id8+id9-1)//id9


def id10():
    id11=id4()
    id8=id1()
    id12=id13(id8)
    id14=0
    id15=id12-id11*id11
    if id15>0:
        id14+=id15
        for id16 in id17(id11):
            id8[id16]+=id15
        id18=0
        id19=10**20
        while id19-id18>1:
            id20=(id18+id19)//2
            id21=0
            for id16 in id17(id11):
                if id8[id16]>=id20:
                    id21+=id7(id8[id16]-id20, id11+1)
            id22=id21<=id15
            if id22:
                id19=id20
            else:
                id18=id20
        id23=0
        for id16 in id17(id11):
            if id8[id16]>=id19:
                id24=id7(id8[id16]-id19, id11+1)
                id8[id16]-=id24*(id11+1)
                id23+=id24
        for _ in id17(id15-id23):
            id25=0
            for id16 in id17(id11):
                if id8[id16]>id8[id25]:
                    id25=id16
            id8[id25]-=id11+1
    while id26(id8)>=id11:
        for id16 in id17(id11):
            id8[id16]+=1
        id25=0
        for id16 in id17(id11):
            if id8[id16]>id8[id25]:
                id25=id16
        id8[id25]-=id11+1
        id14+=1
    return id14


def id27():
    id14=id10()
    print(id14)


if id28=="__main__":
    id27()