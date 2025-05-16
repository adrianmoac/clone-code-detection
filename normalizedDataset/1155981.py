#  coding:utf-8

def id0(id1, id2):
    id3=["S", "S"]
    for id4 in id2[1:-1]:
        if id4=="o":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("S")
            else:
                id3.id5("W")
        elif id4=="x":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("W")
            else:
                id3.id5("S")
    else:
        if (id2[0], id2[-1])==("o", "o"):
            if (id3[-2], id3[-1])==("S", "S"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("o", "x"):
            if (id3[-2], id3[-1])==("W", "S"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "o"):
            if (id3[-2], id3[-1])==("W", "W"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "x"):
            if (id3[-2], id3[-1])==("S", "W"):
                return "".id6(id3)
        
    id3=["S", "W"]
    for id4 in id2[1:-1]:
        if id4=="o":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("S")
            else:
                id3.id5("W")
        elif id4=="x":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("W")
            else:
                id3.id5("S")
    else:
        if (id2[0], id2[-1])==("o", "o"):
            if (id3[-2], id3[-1])==("W", "W"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("o", "x"):
            if (id3[-2], id3[-1])==("S", "W"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "o"):
            if (id3[-2], id3[-1])==("S", "S"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "x"):
            if (id3[-2], id3[-1])==("W", "S"):
                return "".id6(id3)

    id3=["W", "S"]
    for id4 in id2[1:-1]:
        if id4=="o":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("S")
            else:
                id3.id5("W")
        elif id4=="x":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("W")
            else:
                id3.id5("S")
    else:
        if (id2[0], id2[-1])==("o", "o"):
            if (id3[-2], id3[-1])==("S", "W"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("o", "x"):
            if (id3[-2], id3[-1])==("W", "W"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "o"):
            if (id3[-2], id3[-1])==("S", "S"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "x"):
            if (id3[-2], id3[-1])==("W", "S"):
                return "".id6(id3)

    id3=["W", "W"]
    for id4 in id2[1:-1]:
        if id4=="o":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("S")
            else:
                id3.id5("W")
        elif id4=="x":
            if ((id3[-2]=="S" and id3[-1]=="S") or
                (id3[-2]=="W" and id3[-1]=="W")):
                id3.id5("W")
            else:
                id3.id5("S")
    else:
        if (id2[0], id2[-1])==("o", "o"):
            if (id3[-2], id3[-1])==("W", "S"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("o", "x"):
            if (id3[-2], id3[-1])==("S", "S"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "o"):
            if (id3[-2], id3[-1])==("S", "W"):
                return "".id6(id3)
        elif (id2[0], id2[-1])==("x", "x"):
            if (id3[-2], id3[-1])==("W", "W"):
                return "".id6(id3)

    return-1


if id7=="__main__":
    id1=id8(id9())
    id10=id9()
    print id0(id1, id10)