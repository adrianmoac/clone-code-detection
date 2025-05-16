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


id7=[]
id8=[]


def id9(id10):
    id7[id10]=id10
    id8[id10]=0


def id11(id10, id12):
    id13(id14(id10), id14(id12))


def id13(id10, id12):
    if id8[id10]>id8[id12]:
        id7[id12]=id10
    else:
        id7[id10]=id12
        if id8[id10]==id8[id12]:
            id8[id10]+=1


def id14(id10):
    if id10!=id7[id10]:
        id7[id10]=id14(id7[id10])
    return id7[id10]


def id15():
    id16=id5()
    id17=[id1() for id18 in id19(id16)]
    global id7, id8
    id7=[0]*id16
    id8=[0]*id16

    for id10 in id19(id16):
        id9(id10)

    def id20(id18, id21):
        return id22(id23(id17[id18][0]-id17[id21][0]), id23(id17[id18][1]-id17[id21][1]))

    id24=[]
    for id21 in id19(2):
        id25=id26(id19(id16), id27=lambda id18: id17[id18][id21])
        for id18 in id19(id16-1):
            id28=id20(id25[id18], id25[id18+1])
            id29=(id28, id25[id18], id25[id18+1])
            id24.id30(id29)
    id24.id31()

    id32=0
    id33=0
    for id29 in id24:
        id34, id35, id36=id29
        if id14(id35)!=id14(id36):
            id32+=id34
            id33+=1
            id11(id35, id36)
        if id33==id16-1:
            break
    return id32


def id37():
    id32=id15()
    print(id32)


id37()