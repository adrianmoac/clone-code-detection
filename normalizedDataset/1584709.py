#coding=UTF-8

def id0(id1):
    global id2
    global id3
    global id4
    global id5
    id6=0
    if id7(id1)==id3:
        id8=id1[0]
        for id9 in id10(1,id3,1):
            id11=id1[id9]
            id6+=id5[id8][id4[id11]]
            id8=id11

        if id2==None or id6<id2:
            id2=id6
    else:
        for id12 in id10(0,id3,1):
            if not (id12 in id1):
                id0(id1+[id12])


id13=input()
id14=id13.split(" ")
id15=id16(id14[0])
id17=id16(id14[1])
id3=id16(id14[2])

id13=input()
id14=id13.split(" ")
id4=[(id16(id18)-1 ) for id18 in id14]

id19=[]
for id9 in id10(0,id15,1):
    id19.id20([])

for id9 in id10(0,id17,1):
    id13=input()
    id14=id13.split(" ")
    id21=id16(id14[0])-1
    id22=id16(id14[1])-1
    id23=id16(id14[2])
    id19[id21].id20((id22,id23))
    id19[id22].id20((id21,id23))


id5=[]
for id24 in id10(0,id3,1):
    id25=[None]*id15
    id25[id4[id24]]=0
    id26=[id4[id24]]
    while id26:
        id27=[]
        for id28 in id26:
            id29=id25[id28]
            for (id30,id31) in id19[id28]:
                id32=id29+id31
                if id25[id30]==None or id32<id25[id30]:
                    id25[id30]=id32
                    id27.id20(id30)

        id26=id33(id34(id27))
    id5.id20(id25)

#for ko in rCost:
#    print(ko)

id2=None
id0([])
print(id2)