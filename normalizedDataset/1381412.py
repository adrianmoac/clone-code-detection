import id0
import id1

# sys.stdin=open('d1.in')


def id2():
    return id3(map(id4, input().split()))


def id5():
    return input().split()


def id6():
    return id4(input())


def id7():
    return input()


id8=[]
id9=[]


def id10(id11):
    id8[id11]=id11
    id9[id11]=0


def id12(id11, id13):
    id14(id15(id11), id15(id13))


def id14(id11, id13):
    if id9[id11]>id9[id13]:
        id8[id13]=id11
    else:
        id8[id11]=id13
        if id9[id11]==id9[id13]:
            id9[id11]+=1


def id15(id11):
    if id11!=id8[id11]:
        id8[id11]=id15(id8[id11])
    return id8[id11]


def id16():
    id17=id6()
    id18=[id2() for id19 in id20(id17)]
    global id8, id9
    id8=[0]*id17
    id9=[0]*id17

    for id11 in id20(id17):
        id10(id11)

    def id21(id19, id22):
        return id23(id24(id18[id19][0]-id18[id22][0]), id24(id18[id19][1]-id18[id22][1]))

    id25=[]
    for id22 in id20(2):
        id26=id27(id20(id17), id28=lambda id19: id18[id19][id22])
        for id19 in id20(id17-1):
            id29=id21(id26[id19], id26[id19+1])
            id30=(id29, id26[id19], id26[id19+1])
            id25.id31(id30)
    id25.id32()

    id33=0
    for id30 in id25:
        id34, id35, id36=id30
        if id15(id35)!=id15(id36):
            id33+=id34
            id12(id35, id36)
    return id33


def id37():
    id33=id16()
    print(id33)


id37()