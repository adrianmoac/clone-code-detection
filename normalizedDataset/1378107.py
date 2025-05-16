import id0
from id1 import id2

# sys.stdin=open('c1.in')


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
    if id10==id12:
        return id12+id11
    if id11==id13:
        return id12+id13+id12-id10
    if id10==0:
        return id12+id13+id12+id13-id11


id12, id13, id14,=id3()
id15=[0, 0]
id16=[0, 0]
id17=[]
for id18 in id19(id14):
    id15[0], id16[0], id15[1], id16[1]=id3()
    if (id15[0] in [0, id12] or id16[0] in [0, id13]) and (id15[1] in [0, id12] or id16[1] in [0, id13]):
        for id20 in id19(2):
            id17.id21((id9(id15[id20], id16[id20]), id18))
id22=id23(id17)//2
id17.id24()

id25="YES"
id26=id27()
id28=[]
for id29, id18 in id17:
    if id18 not in id26:
        id26.id30(id18)
        id28.id21(id18)
    else:
        if id28[-1]!=id18:
            id25="NO"
            break
        id28.id31()

print(id25)