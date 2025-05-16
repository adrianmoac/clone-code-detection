
id0=id1(map(id2, input().split()))
id3=[id1(map(id4, input())) for id5 in id6(id0[0])]

def id7(id5,id8,id3):
    if id3[id5][id8]=="#":
        return "#"
    id9=0
    if id10(id3)==1:
        if id10(id3[0])==1:
            if id3[0][0]=="#":
                return "#"
            return 0
        if id10(id3[0])!=1:
            if id8==0:
                if id3[0][1]=="#":
                    id9+=1
                return id9
            if id8==id10(id3[0])-1:
                if id3[0][id10(id3[0])-2]=="#":
                    id9+=1
                return id9
            for id11 in id6(-1,2):
                if id11==0:
                    continue
                if id3[0][id8+id11]=="#":
                    id9+=1
            return id9

    if id10(id3[0])==1:
        if id5==0:
            if id3[1][0]=="#":
                id9+=1
            return id9
        if id5==id10(id3)-1:
            if id3[id10(id3)-2][0]=="#":
                id9+=1
            return id9
        for id12 in id6(-1,2):
            if id12==0:
                continue
            if id3[id5+id12][0]=="#":
                id9+=1
        return id9           


    if id5==0 and id8==0:
        for id12 in id6(0,2):
            for id11 in id6(0,2):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1
        return id9
    if id5==0 and id8==id10(id3[0])-1:
        for id12 in id6(0,2):
            for id11 in id6(-1,1):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1
        return id9    

    if id5==id10(id3)-1 and id8==0:
        for id12 in id6(-1,1):
            for id11 in id6(0,2):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1
        return id9 
    if id5==id10(id3)-1 and id8==id10(id3[0])-1:
        for id12 in id6(-1,1):
            for id11 in id6(-1,1):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1
        return id9
    if id5==0:
        for id12 in id6(0,2):
            for id11 in id6(-1,2):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1
        return id9

    if id5==id10(id3)-1:
        for id12 in id6(-1,1):
            for id11 in id6(-1,2):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1
        return id9

    if id8==0:
        for id12 in id6(-1,2):
            for id11 in id6(0,2):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1 
        return id9

    if id8==id10(id3[0])-1:
        for id12 in id6(-1,2):
            for id11 in id6(-1,1):
                if id12==0 and id11==0:
                    continue
                if id3[id5+id12][id8+id11]=="#":
                    id9+=1
        return id9
       
    for id12 in id6(-1,2):
        for id11 in id6(-1,2):
            if id12==0 and id11==0:
                continue
            if id3[id5+id12][id8+id11]=="#":
                id9+=1
    return id9

id13=[]
for id14 in id6(id10(id3)):
    for id15 in id6(id10(id3[0])):
        id13.id16(id7(id14,id15,id3))  

for id5 in id6(id0[0]):
    id17=0+id0[1]*id5
    id18=id0[1]+id0[1]*id5
    while id17<id18:
        print(id13[id17],id19="")
        id17+=1
    print("")
id20()

