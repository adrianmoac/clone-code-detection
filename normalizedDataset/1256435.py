#-*-coding: utf-8-*-import numpy as np

id0=9
id1=4

id2=id3().split()
id4=id5(id2[0])-1
id6=id5(id2[1])-1
id7=id2[2]
id8=id9.id10((id0, id0), id11=id5)
id12=0
id13=0
id14=id9.id10(id1, id11=id5)

for id15 in id16(id0):
    id17=id3()

    for id18 in id16(id0):
        id8[id15][id18]=id5(id17[id18])

# 方向決め
if id7=="R":
    id12=1
    id13=0
elif id7=="L":
    id12=-1
    id13=0
elif id7=="U":
    id12=0
    id13=-1
elif id7=="D":
    id12=0
    id13=1
elif id7=="RU":
    id12=1
    id13=-1
elif id7=="RD":
    id12=1
    id13=1
elif id7=="LU":
    id12=-1
    id13=-1
elif id7=="LD":
    id12=-1
    id13=1

# 矢印方向に動かす
for id15 in id16(id1):
    id14[id15]=id8[id6][id4]

    if id4==id0-1 and id12==1:
        id12=-1
    elif id4==0 and id12==-1:
        id12=1

    if id6==id0-1 and id13==1:
        id13=-1
    elif id6==0 and id13==-1:
        id13=1

    id4+=id12
    id6+=id13

print "%d%d%d%d"%(id14[0], id14[1], id14[2], id14[3])