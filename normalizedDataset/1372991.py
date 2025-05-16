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


def id7(id8, id9):
    for id10 in id11(2):
        for id12 in id11(2):
            id13=[id10, id12]+[-1]*(id8-2)
            for id14 in id11(2, id8):
                if id9[id14-1]=="o":
                    id15=id13[id14-2]
                else:
                    id15=1-id13[id14-2]
                if id13[id14-1]==1:
                    id15=1-id15
                id13[id14]=id15

            id16=True
            for id14 in id11(-1, id8-1):
                if id13[id14-1]!=id13[id14+1]:
                    id17=1
                else:
                    id17=0
                if id13[id14]==1:
                    id17=1-id17
                if id17==1:
                    id18="x"
                else:
                    id18="o"
                id16&=id9[id14]==id18
            if id16:
                id19=map(lambda id20: "SW"[id20], id13)
                id21="".id22(id19)
                return id21
    return-1


def id23():
    id8=id5()
    id9=id6()
    id21=id7(id8, id9)
    print(id21)


id23()