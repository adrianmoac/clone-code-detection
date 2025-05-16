import id0
import id1
 
id2=id3(map(id4, input().split()))
id5=id2[0]*id2[1]
 
if ((id2[0]%3==0) or (id2[1]%3==0)):
    print(0)
    id1.id6()
 
id7=1000000000000
for id8 in id9(1, id0.id10(id2[0]/2)+1):
    id11=id8*id2[1]
    id12=id0.id13(id2[1]/2)*(id2[0]-id8)
    id14=id5-(id11+id12)
    if (id12==id14):
        id7=id15(id7, id16(id11-id12))
    else:
        if (id11>id14):
            id7=id15(id7, id16(id11-id12))
        elif(id14>=id11 and id11>=id12):
            id7=id15(id7, id16(id14-id12))
        else:
            id7=id15(id7, id16(id14-id11))
    id11=id8*id2[1]
    id12=id0.id13((id2[0]-id8)/2)*id2[1]
    id14=id5-(id11+id12)
    if (id12==id14):
        id7=id15(id7, id16(id11-id12))
    else:
        if (id11>id14):
            id7=id15(id7, id16(id11-id12))
        elif(id14>=id11 and id11>=id12):
            id7=id15(id7, id16(id14-id12))
        else:
            id7=id15(id7, id16(id14-id11))
 
for id8 in id9(1, id0.id10(id2[1]/2)+1):
    id11=id8*id2[0]
    id12=id0.id13(id2[0]/2)*(id2[1]-id8)
    id14=id5-(id11+id12)
    if (id12==id14):
        id7=id15(id7, id16(id11-id12))
    else:
        if (id11>id14):
            id7=id15(id7, id16(id11-id12))
        elif(id14>=id11 and id11>=id12):
            id7=id15(id7, id16(id14-id12))
        else:
            id7=id15(id7, id16(id14-id11))
    id11=id8*id2[0]
    id12=id0.id13((id2[1]-id8)/2)*id2[0]
    id14=id5-(id11+id12)
    if (id12==id14):
        id7=id15(id7, id16(id11-id12))
    else:
        if (id11>id14):
            id7=id15(id7, id16(id11-id12))
        elif(id14>=id11 and id11>=id12):
            id7=id15(id7, id16(id14-id12))
        else:
            id7=id15(id7, id16(id14-id11))
 
print(id7)