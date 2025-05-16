def id0(id1):
    if id1=="S":
        return "W"
    else:
        return "S"

def id2():
    id3=False
    id4=-1
    for id5 in id6(id7):
        #print r
        if id8[id5]=="S":
            if id9[id5]=="o":
                if id5==0:
                    id8[id5-1]=id8[id5+1]
                elif id5==id7-1:
                    if id8[0]==id8[id5-1]:
                        id3=True
                elif id5==id7-2:
                    if id8[id5+1]!=id8[id5-1]:
                        break;                    
                else:
                    id8[id5+1]=id8[id5-1]
            else:
                if id5==0:
                    id8[id5-1]=id0(id8[id5+1])
                elif id5==id7-2:
                    if id8[id5+1]!=id0(id8[id5-1]):
                        break;                    
                elif id5==id7-1:
                    if id8[0]==id0(id8[id5-1]):
                        id3=True
                else:
                    id8[id5+1]=id0(id8[id5-1])
        else: # W
            if id9[id5]=="x":
                if id5==0:
                    id8[id5-1]=id8[id5+1]
                elif id5==id7-1:
                    if id8[0]==id8[id5-1]:
                        id3=True
                elif id5==id7-2:
                    if id8[id5+1]!=id8[id5-1]:
                        break;                    
                else:
                    id8[id5+1]=id8[id5-1]
            else:
                if id5==0:
                    id8[id5-1]=id0(id8[id5+1])
                elif id5==id7-1:
                    if id8[0]==id0(id8[id5-1]):
                        id3=True
                elif id5==id7-2:
                    if id8[id5+1]!=id0(id8[id5-1]):
                        break;                    
                else:
                    id8[id5+1]=id0(id8[id5-1])
                
        if id3:
            id4="".id10(id8)

    return id4
    
id7=input()
id9=id11(id12())


id13=[["S","S"],["S","W"],["W","S"],["W","W"]]

id4=None
for id14 in id13:
    id8=[None]*id7
    id8[0]=id14[0]
    id8[1]=id14[1]
    id4=id2()
    if id4!=-1:
        break
print id4
