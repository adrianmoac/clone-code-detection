id0=id1(input())
id2=id3(input())
id4=0
id5=[id3("SS"),id3("SW"),id3("WS"),id3("WW")]
for id6 in id5:
    for id7 in id8(id9(id2)-2):
        if id2[id7+1]=="o":
            if id6[id7]=="S" and id6[id7+1]=="S":
                id6.id10("S")
            elif id6[id7]=="S" and id6[id7+1]=="W":
                id6.id10("W")
            elif id6[id7]=="W" and id6[id7+1]=="S":
                id6.id10("W")
            elif id6[id7]=="W" and id6[id7+1]=="W":
                id6.id10("S")
        elif id2[id7+1]=="x":
            if id6[id7]=="S" and id6[id7+1]=="S":
                id6.id10("W")
            elif id6[id7]=="S" and id6[id7+1]=="W":
                id6.id10("S")
            elif id6[id7]=="W" and id6[id7+1]=="S":
                id6.id10("S")
            elif id6[id7]=="W" and id6[id7+1]=="W":
                id6.id10("W")
    
    id11=0
    if id2[0]=="o":
        if id6[0]=="S":
            if id6[-1]==id6[1]:
                id11=1 
        if id6[0]=="W":
            if id6[-1]!=id6[1]:
                id11=1
    if id2[0]=="x":
        if id6[0]=="S":
            if id6[-1]!=id6[1]:
                id11=1
        if id6[0]=="W":
            if id6[-1]==id6[1]:
                id11=1
                
    if id11==1:
        if id2[-1]=="o":
            if id6[-1]=="S":
                if id6[0]==id6[-2]:
                    print ("".id12(id6))
                    id4=1
                    break
            if id6[-1]=="W":
                if id6[0]!=id6[-2]:
                    print ("".id12(id6))
                    id4=1
                    break
        if id2[-1]=="x":
            if id6[-1]=="S":
                if id6[0]!=id6[-2]:
                    print ("".id12(id6))
                    id4=1
                    break
            if id6[-1]=="W":
                if id6[0]==id6[-2]:
                    print ("".id12(id6))
                    id4=1
                    break
if id4==0:
    print(-1)
        