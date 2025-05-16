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


def id7():
    id8=10
    id9, id10, id11=id1()
    id12=[id1() for id13 in id14(id9)]
    id15={(0, 0, 0): 0}

    for id13 in id14(1, id9+1):
        id16, id17, id18=id12[id13-1]
        for id19 in id14(0, id8*(id13-1)+1):
            for id20 in id14(0, id8*(id13-1)+1):
                if (id13-1, id19, id20) in id15:
                    id21=id15[(id13-1, id19, id20)]
                    id22=id21+id18
                    id23=id19+id16
                    id24=id20+id17
                    if (id13, id23, id24) not in id15:
                        id15[(id13, id23, id24)]=id22
                    if id22<id15[(id13, id23, id24)]:
                        id15[(id13, id23, id24)]=id22
                        
                    id22=id21
                    id23=id19
                    id24=id20
                    if (id13, id23, id24) not in id15:
                        id15[(id13, id23, id24)]=id22
                    if id22<id15[(id13, id23, id24)]:
                        id15[(id13, id23, id24)]=id22

    id25=10**20
    id26=id25
    for id19 in id14(0, id8*id9+1):
        for id20 in id14(0, id8*id9+1):
            if id19==0 and id20==0:
                continue
            if id19*id11==id20*id10:
                if (id9, id19, id20) in id15:
                    id21=id15[(id9, id19, id20)]
                    if id21<id26:
                        id26=id21
    if id26==id25:
        id26=-1
    return id26


def id27():
    id26=id7()
    print(id26)


id27()