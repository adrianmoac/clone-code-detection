# coding:utf-8


def id0(id1, id2, id3, id4, id5):
    if id4==id5 or id2[id4]==id2[id5]:
        return id3

    id6=0
    if id1[id4]==id2[id5]:
        id6+=1
    if id1[id5]==id2[id4]:
        id6+=1

    if id1[id4]==id2[id4]:
        if id1[id5]==id2[id5]:
            if id3>=2:
                id7=id2[id4]
                id2[id4]=id2[id5]
                id2[id5]=id7
                return id3-2
            else:
                return-1
        else:
            if id3+id6>=1:
                id7=id2[id4]
                id2[id4]=id2[id5]
                id2[id5]=id7
                return id3+id6-1
            else:
                return-1
    else:
        if id1[id5]==id2[id5]:
            if id3+id6>=1:
                id7=id2[id4]
                id2[id4]=id2[id5]
                id2[id5]=id7
                return id3+id6-1
            else:
                return-1
        else:
            id7=id2[id4]
            id2[id4]=id2[id5]
            id2[id5]=id7
            return id3+id6


id8, id3=[id9(id10) for id10 in input().split(" ")]
id1=id11(input())
id2=id1.id12()
for id4 in id13(id8):
    id14=id15(id11(id16(id2[id4:])))
    for id5 in id14:
        id6=id2[id4:].id6(id5)
        id17=id2[id4:].id12()
        id18=-1
        id19=0
        for id20 in id13(id6):
            id21=id2.id12()
            id22=id0(id1, id21, id3, id4, id17.id23(id5)+id20+id4)
            if id22>id18:
                id18=id22
                id19=id17.id23(id5)+id20+id4
            id17.id24(id5)
        if id18>=0:
            id3=id0(id1, id2, id3, id4, id19)
            break
print("".id25(id2))