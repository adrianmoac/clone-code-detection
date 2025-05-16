import id0
import id1
import id2

# sys.stdin=open('b1.in')


def id3():
    return id4(map(id5, input().split()))


def id6():
    return id5(input())


def id7():
    return input().split()


def id8():
    return input()


def id9(id10, id11):
    if id12[id10]>id12[id11]:
        id13[id11]=id10
    else:
        id13[id10]=id11
        if id12[id10]==id12[id11]:
            id12[id11]=id12[id10]+1


def id14(id10, id11):
    id9(id15(id10), id15(id11))


def id15(id10):
    if id10!=id13[id10]:
        id13[id10]=id15(id13[id10])
    return id13[id10]


def id16(id17, id18):
    return id19(id20(id21[id17][0]-id21[id18][0]), id20(id21[id17][1]-id21[id18][1]))


id22=id6()
id21=[id3() for id23 in id24(id22)]

id13=id4(id24(id22))
id12=[0]*id22

id25=[]

for id26 in id24(2):
    id27=id4(id24(id22))
    id27.id28(id29=lambda id30: id21[id30][id26])
    for id23 in id24(1, id22):
        id17=id27[id23-1]
        id18=id27[id23]
        id31=id16(id17, id18)
        id2.id32(id25, (id31, id17, id18))

id33=0
while id25:
    id34=id2.id35(id25)
    id31, id17, id18=id34
    if id15(id17)!=id15(id18):
        id33+=id31
        id14(id17, id18)

print(id33)