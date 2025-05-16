id0=id1(input())
id2=input()
id3=["SSS", "SSW", "SWW", "WWW", "WWS", "WSS", "SWS", "WSW"]
id4=[]
for id5 in id6(4):
    id4=[]
    if id7(id2)==3:
        print(-1)
        id8()
    elif id2[1]=="o" and id5==0:
        id4.id9("S")
        id4.id9("S")
    elif id2[1]=="x" and id5==0:
        id4.id9("W")
        id4.id9("S")
    elif id2[1]=="o" and id5==1:
        id4.id9("S")
        id4.id9("W")
    elif id2[1]=="x" and id5==1:
        id4.id9("S")
        id4.id9("W")
    elif id2[1]=="o" and id5==2:
        id4.id9("W")
        id4.id9("S")
    elif id2[1]=="x" and id5==2:
        id4.id9("W")
        id4.id9("W")
    elif id2[1]=="o" and id5==3:
        id4.id9("W")
        id4.id9("W")
    elif id2[1]=="x" and id5==3:
        id4.id9("S")
        id4.id9("S")

    for id10 in id6(1, id0):
        if id4[id10-1]=="S":
            if id4[id10]=="S":
                if id2[id10]=="o":
                    id4.id9("S")
                else:
                    id4.id9("W")
            else:
                if id2[id10]=="o":
                    id4.id9("W")
                else:
                    id4.id9("S")
        else:
            if id4[id10]=="S":
                if id2[id10]=="o":
                    id4.id9("W")
                else:
                    id4.id9("S")
            else:
                if id2[id10]=="o":
                    id4.id9("S")
                else:
                    id4.id9("W")
    if id4[id0-1]=="S" and id4[id0]==id4[0]:
        if id4[0]=="S":
            if id2[0]=="o" and id4[1]=="S":
                break
            elif id2[0]=="x" and id4[1]=="W":
                break
        else:
            if id2[0]=="o" and id4[1]=="W":
                break
            elif id2[0]=="x" and id4[1]=="S":
                break
    elif id4[id0-1]=="W" and id4[id0]==id4[0]:
        if id4[0]=="S":
            if id2[0]=="o" and id4[1]=="W":
                break
            elif id2[0]=="x" and id4[1]=="S":
                break
        else:
            if id2[0]=="o" and id4[1]=="S":
                break
            elif id2[0]=="x" and id4[1]=="W":
                break
    if id5==3:
        print(-1)
        id8()
id4.id11()
id4="".id12(id4)
print(id4)