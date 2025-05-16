id0=1000000007

id1=id2(input())
id3=id4(input())

id5="S"
id6="W"
id7=0
id8=0
id9=0

for id10 in [id5, id6]:
    if(id7==1): break
    for id11 in [id5, id6]:
        if (id7==1): break
        id12=id4()
        id12.id13(id10)
        id12.id13(id11)

        for id14 in id15(1, id1-1):
            if(id3[id14]=="o"):
               if(id12[id14]==id5):
                   id12.id13(id12[id14-1])
               else:
                    if(id12[id14-1]==id5): id12.id13(id6)
                    else: id12.id13(id5)

            else:
                if (id12[id14]==id6):
                    id12.id13(id12[id14-1])
                else:
                    if (id12[id14-1]==id5):
                        id12.id13(id6)
                    else:
                        id12.id13(id5)

        id8=0
        if(id12[0]==id5):
            if(id3[0]=="o"):
                if(id12[1]==id12[id1-1]):
                    id8=1
            else:
                if (id12[1]!=id12[id1-1]):
                    id8=1
        else:
            if (id3[0]=="x"):
                if (id12[1]==id12[id1-1]):
                    id8=1
            else:
                if (id12[1]!=id12[id1-1]):
                    id8=1
        id9=0
        if (id12[id1-1]==id5):
            if (id3[id1-1]=="o"):
                if (id12[0]==id12[id1-2]):
                    id9=1
            else:
                if (id12[0]!=id12[id1-2]):
                    id9=1
        else:
            if (id3[id1-1]=="x"):
                if (id12[0]==id12[id1-2]):
                    id9=1
            else:
                if (id12[0]!=id12[id1-2]):
                    id9=1
        if(id8==1&id9==1): id7=1

if(id7==1):
    print("".id16(id12))
else:
    print("-1")