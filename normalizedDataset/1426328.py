import id0

id0.id1(10**5+100)

# sys.stdin=open('d1.in')


def id2():
    return id3(map(id4, input().split()))


def id5():
    return id4(input())


def id6():
    return input().split()


def id7():
    return input()


id8=[]
id9=[]
id10=[]


def id11(id12, id13):
    id10[id12]=1
    id9[id12]=id13
    for id14 in id8[id12]:
        if id14!=id13:
            id11(id14, id12)
    id10[id12]=2


def id15(id12):
    id16=1
    for id14 in id8[id12]:
        if id14!=id9[id12]:
            id16+=id15(id14)
    return id16


def id17():
    global id8
    global id9
    global id10
    id18=id5()
    id19=[id2() for id14 in id20(id18-1)]
    id8=[[] for id14 in id20(id18)]
    for id21, id22 in id19:
        id21-=1
        id22-=1
        id8[id21].id23(id22)
        id8[id22].id23(id21)
    id10=[0]*id18
    id9=[-1]*id18
    id11(0,-1)

    id24=id18-1
    id25=[]
    while id24!=0:
        id25.id23(id24)
        id24=id9[id24]
    id25.id23(0)

    id26=id27(id25)
    id28=id26//2

    id29=id15(id25[id28-1])
    if id18-id29>id29:
        return "Fennec"
    return "Snuke"


def id30():
    id16=id17()
    print(id16)


if id31=="__main__":
    id30()