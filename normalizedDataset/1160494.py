# coding: utf-8

id0=id1(input())
id2=id3(input())


def id4(id5, id6, id7):
    if id5=="S":
        if id6=="S":
            if id7=="o":
                return "S"
            else:
                return "W"
        else:
            if id7=="o":
                return "W"
            else:
                return "S"

    else:
        if id6=="S":
            if id7=="o":
                return "W"
            else:
                return "S"
        else:
            if id7=="o":
                return "S"
            else:
                return "W"


def id8(id9, id10):
    global id11
    id11.id12(id9)
    id13=id4(id10, id9, id2[0])
    id11.id12(id13)
    for id14 in id15(1, (id0-1)):
        id13=id4(id11[id14-1], id11[id14], id2[id14])
        id11.id12(id13)

    if id11[(id0-1)]==id10 and id4(id11[(id0-2)], id11[(id0-1)], id2[(id0-1)])==id11[0]:
        return "ok"
    else:
        return "ng"


id16=0

for id14 in id15(4):
    id11=[]
    if id14==0:
        id17="S"
        id18="S"
        if id8(id17, id18)=="ok":
            print ("".id19([id14 for id14 in id11]))
            break
        else:
            id16+=1

    elif id14==1:
        id17="S"
        id18="W"
        if id8(id17, id18)=="ok":
            print ("".id19([id14 for id14 in id11]))
            break
        else:
            id16+=1

    elif id14==2:
        id17="W"
        id18="S"
        if id8(id17, id18)=="ok":
            print ("".id19([id14 for id14 in id11]))
            break
        else:
            id16+=1

    elif id14==3:
        id17="W"
        id18="W"
        if id8(id17, id18)=="ok":
            print ("".id19([id14 for id14 in id11]))
            break
        else:
            id16+=1

if id16==4:
    print(-1)