#-*-coding: utf-8-*-import numpy as np

id0=9
id1=4

id2=id3().split()
id4=id5(id2[0])-1
id6=id5(id2[1])-1
id7=id2[2]
id8=id9.id10((id0, id0), id11=id5)
id12=id9.id10(id1, id11=id5)

for id13 in id14(id0):
    id15=id3()

    for id16 in id14(id0):
        id8[id13][id16]=id5(id15[id16])

#print c
for id13 in id14(id1):
    id12[id13]=id8[id6][id4]

    if id7=="R":
        if id4==id0-1:
            id4=id0-2
            id7="L"
        else:
            id4+=1

    elif id7=="L":
        if id4==0:
            id4=1
            id7="R"
        else:
            id4-=1

    elif id7=="U":
        if id6==0:
            id6=1
            id7="D"
        else:
            id6-=1

    elif id7=="D":
        if id6==id0-1:
            id6=id0-2
            id7="U"
        else:
            id6+=1

    elif id7=="RU":
        if id4==id0-1 and id6==0:
            id4=id0-2
            id6=1
            id7="LD"
        elif id4==id0-1:
            id4=id0-2
            id6-=1
            id7="LU"
        elif id6==0:
            id4+=1
            id6=1
            id7="RD"
        else:
            id4+=1
            id6-=1

    elif id7=="RD":
        if id4==id0-1 and id6==id0-1:
            id4=id0-2
            id6=id0-2
            id7="LU"
        elif id4==id0-1:
            id4=id0-2
            id6+=1
            id7="LD"
        elif id6==id0-1:
            id4+=1
            id6=id0-2
            id7="RU"
        else:
            id4+=1
            id6+=1

    elif id7=="LU":
        if id4==0 and id6==0:
            id4=1
            id6=1
            id7="RD"
        elif id4==0:
            id4=1
            id6-=1
            id7="RU"
        elif id6==0:
            id4-=1
            id6=1
            id7="LD"
        else:
            id4-=1
            id6-=1

    elif id7=="LD":
        if id4==0 and id6==id0-1:
            id4=1
            id6=id0-2
            id7="RU"
        elif id4==0:
            id4=1
            id6+=1
            id7="RD"
        elif id6==id0-1:
            id4-=1
            id6=id0-2
            id7="LU"
        else:
            id4-=1
            id6+=1
print "%d%d%d%d"%(id12[0], id12[1], id12[2], id12[3])