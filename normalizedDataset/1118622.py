id0=id1(id2())
id3=id2()
assert(3<=id0<=1e5)
assert(id4(id3)==id0)

id5=[]
id6="S"
id7="W"
id8=[id9 for id9 in id3]
id10="o"
id11="x"
id12=False
id13=[id6, id6]
id14=[id6, id7]
id15=[id7, id6]
id16=[id7, id7]
id17=[id13, id14, id15, id16]
for id5 in id17:
    id18=False
    id19=False
    for id20 in id21(1, id4(id8)-1):
        id9=id8[id20]
        if id5[id20]==id6:
            if id9==id10:
                id5.id22(id5[id20-1])
            else:
                if id5[id20-1]==id6:
                    id5.id22(id7)
                else:
                    id5.id22(id6)
        else:# wolf
            if id9==id10:
                if id5[id20-1]==id6:
                    id5.id22(id7)
                else:
                    id5.id22(id6)
            else:
                id5.id22(id5[id20-1])
    if (id5[0]==id6):
        if (id8[0]==id10) and (id5[-1]==id5[1]):
            id18=True
        elif (id8[0]==id11) and (not (id5[-1]==id5[1])):
            id18=True
    else:
        if (id8[0]==id10) and (not (id5[-1]==id5[1])):
            id18=True
        elif (id8[0]==id11) and (id5[-1]==id5[1]):
            id18=True

    if (id5[-1]==id6):
        if (id8[-1]==id10) and (id5[-2]==id5[0]):
            id19=True
        elif (id8[-1]==id11) and (not (id5[-2]==id5[0])):
            id19=True
    else:
        if (id8[-1]==id10) and (not (id5[-2]==id5[0])):
            id19=True
        elif (id8[-1]==id11) and (id5[-2]==id5[0]):
            id19=True
    if id18 and id19:
        id12=True
        break

if id12:
    print "".id23(id5)
else:
    print-1