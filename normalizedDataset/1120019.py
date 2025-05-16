def id0(id1, id2, id3):
    id4=id1[id3]
    id5=id2[id3-1]
    id6=id2[id3]
    id7=""
    if(id4=="o" and id5=="S" and id6=="S"):
        id7="S"
    elif(id4=="o" and id5=="S" and id6=="W"):
        id7="W"
    elif(id4=="o" and id5=="W" and id6=="S"):
        id7="W"
    elif(id4=="o" and id5=="W" and id6=="W"):
        id7="S"
    elif(id4=="x" and id5=="S" and id6=="S"):
        id7="W"
    elif(id4=="x" and id5=="S" and id6=="W"):
        id7="S"
    elif(id4=="x" and id5=="W" and id6=="S"):
        id7="S"
    elif(id4=="x" and id5=="W" and id6=="W"):
        id7="W"
    return id7

def id8(id1, id2):
    id9=0
    if(id2[-1]=="S"):
        if(id1[-1]=="x" and id2[-2]!=id2[0]):
            id9=1
        elif(id1[-1]=="o" and id2[-2]==id2[0]):
            id9=1
    elif(id2[-1]=="W"):
        if(id1[-1]=="x" and id2[-2]==id2[0]):
            id9=1
        elif(id1[-1]=="o" and id2[-2]!=id2[0]):
            id9=1
            
    id10=0    
    if(id2[0]=="S"):
        if(id1[0]=="x" and id2[1]!=id2[-1]):
            id10=1
        elif(id1[0]=="o" and id2[1]==id2[-1]):
            id10=1
    elif(id2[0]=="W"):
        if(id1[0]=="x" and id2[1]==id2[-1]):
            id10=1
        elif(id1[0]=="o" and id2[1]!=id2[-1]):
            id10=1
    
    return id9*id10

try:
    while True:  
        id11=id12().id13().id14()
        id1=id12().id13().id15()
        id9=-1
        for id16 in ["S", "W"]:
            for id17 in ["S","W"]:
                id2=[0]*id18(id11)
                id2[0]=id16
                id2[1]=id17
                for id19 in id20(2, id18(id11)):
                    id7=id0(id1, id2, id19-1)
                    id2[id19]=id7
                    id21=id8(id1, id2)
                    if(id21==1):
                        id9=""
                        for id22 in id2:
                            id9+=id22
        print id9
                        
except id23:
    pass