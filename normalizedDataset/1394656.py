import id0
from id1 import id2

# sys.stdin=open('d1.in')
# sys.stdout=open('out.txt', 'w')

id3=10**9+7


def id4():
    return id5(map(id6, input().split()))


def id7():
    return id6(input())


def id8():
    return input().split()


def id9():
    return input()


def id10():
    id11=id7()
    id12=[0]*(id11+2)
    id12[1]=1
    for id13 in id14(2, id11+2):
        id12[id13]=(id3-id3//id13)*id12[id3%id13]%id3
    id15=id4()
    id16=id2(id15)
    id17=-1
    for id13 in id14(1, id11+1):
        if id16[id13]==2:
            id17=id13
            break
    id18=[id13 for id13 in id14(id11+1) if id15[id13]==id17]
    id19=id18[1]-id18[0]
    id20=[0]*(id11+1)
    id16=1
    id21=1
    for id22 in id14(1, id11+2):
        id16*=id11+1-id22+1
        id16*=id12[id22]
        id16%=id3
        id20[id22-1]=(id16-id21)%id3

        id21*=id11-id19-id22+1
        id21*=id12[id22]
        id21%=id3

    id23="\n".id24(map(id25, id20))
    return id23


def id26():
    id23=id10()
    print(id23)


if id27=="__main__":
    id26()