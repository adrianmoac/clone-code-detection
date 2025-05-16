import id0

id0.id1(id2(2E5))

id3=True
id4=False


def id5(id6):
    print("".id7(["S" if id8 else "W" for id8 in id6]))


def id9(id6, id10):
    if id11[id10]:
        if id6[id10]==id3:
            return id6[id10-1]
        else:
            return not id6[id10-1]
    else:
        if id6[id10]==id3:
            return not id6[id10-1]
        else:
            return id6[id10-1]


def id12(id6, id10):
    if id11[id10]:
        if id6[id10]==id3:
            return id6[id10+1]
        else:
            return not id6[id10+1]
    else:
        if id6[id10]==id3:
            return not id6[id10+1]
        else:
            return id6[id10+1]


def id13(id6, id10, id14):
    id6[id10+1]=id9(id6, id10)
    id10+=1
    if id10==id14-1:
        return id6[0]==id9(id6, id10) and id6[id10]==id12(id6, 0)
    else:
        return id13(id6, id10, id14)


if id15=="__main__":
    id14=id2(input())
    id11=[True if id16=="o" else False for id16 in input().id17()]
    id18=[[id4, id4]
        , [id4, id3]
        , [id3, id3]
        , [id3, id4]]
    id19=[0]*id2(2E5)
    for id20 in id18:
        id19[:2]=id20
        if id13(id19, 1, id14):
            id5(id19[:id14])
            break
    else:
        print(-1)