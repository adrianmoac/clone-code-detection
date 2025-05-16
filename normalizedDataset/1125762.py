from id0 import id1, id2, id3
id4=id1(id5)
id6=id2()
id6.id7(id3)
id4.id7(id3)
id4.id8(id6)

import id9

def match(id10, id11, id12, id13):
    if id10[id12]=="o":
        if id11[id12]=="S":
            return id11[(id12-1+id13)%id13]==id11[(id12+1+id13)%id13]
        else:
            return id11[(id12-1+id13)%id13]!=id11[(id12+1+id13)%id13]
    else:
        if id11[id12]=="W":
            return id11[(id12-1+id13)%id13]==id11[(id12+1+id13)%id13]
        else:
            return id11[(id12-1+id13)%id13]!=id11[(id12+1+id13)%id13]


id13=id14(input())
id10=input()


  
    

for id15 in id16(4):
    id11=""
    if id15%2==0:
        id11+="S"
    else:
        id11+="W"

    if (id14(id15/2))%2==0:
        id11+="S"
    else:
        id11+="W"
#    logger.debug(sw)


    for id17 in id16(id13-2):
        if (id11[id17+1]=="S" and id10[id17+1]=="o") or (id11[id17+1]=="W" and id10[id17+1]=="x"):
            id11+=id11[id17]
        else:
            if id11[id17]=="S":
                id11+="W"
            else:
                id11+="S"

#        logger.debug(sw)

    if match(id10,id11,0,id13) and match(id10,id11,id13-1,id13):
        print(id11)
        id9.id18()

print(-1)