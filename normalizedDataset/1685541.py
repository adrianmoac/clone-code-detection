id0, id1=map(id2, input().split())
id3=[]
id4=[]
for id5 in id6(id0):
    id3.id7(input())
    id4.id7([0 for id8 in id6(id1)])
if id0==1 and id1==1:
    if id3[0][0]=="#":
        id4[0][0]="#"
    else:
        id4[0][0]=0
elif id0==1:
    for id8 in id6(id1):
        if id3[0][id8]=="#":
            id4[0][id8]="#"
        elif id3[0][id8]==".":
            if id8==0:
                if id3[0][id8+1]=="#":
                    id4[0][id8]+=1
            elif id8==id1-1:
                if id3[0][id8-1]=="#":
                    id4[0][id8]+=1
            else:
                if id3[0][id8-1]=="#":
                    id4[0][id8]+=1
                if id3[0][id8+1]=="#":
                    id4[0][id8]+=1
elif id1==1:
    for id5 in id6(id0):
        if id3[id5][0]=="#":
            id4[id5][0]="#"
        elif id3[id5][0]==".":
            if id5==0:
                if id3[id5+1][0]=="#":
                    id4[id5][0]+=1
            elif id5==id0-1:
                if id3[id5-1][0]=="#":
                    id4[id5][0]+=1
            else:
                if id3[id5-1][0]=="#":
                    id4[id5][0]+=1
                if id3[id5+1][0]=="#":
                    id4[id5][0]+=1
else:
    for id5 in id6(id0):
        for id8 in id6(id1):
            if id3[id5][id8]=="#":
                id4[id5][id8]="#"
            elif id3[id5][id8]==".":
                if id5==0 and id8==0:
                    if id3[id5+1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8+1]=="#":
                        id4[id5][id8]+=1
                elif id5==0 and id8==id1-1:
                    if id3[id5+1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8-1]=="#":
                        id4[id5][id8]+=1
                elif id5==id0-1 and id8==0:
                    if id3[id5][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8+1]=="#":
                        id4[id5][id8]+=1
                elif id5==id0-1 and id8==id1-1:
                    if id3[id5-1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8-1]=="#":
                        id4[id5][id8]+=1
                elif id5==0:
                    if id3[id5][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8+1]=="#":
                        id4[id5][id8]+=1
                elif id8==0:
                    if id3[id5-1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8+1]=="#":
                        id4[id5][id8]+=1
                elif id5==id0-1:
                    if id3[id5-1][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8+1]=="#":
                        id4[id5][id8]+=1
                elif id8==id1-1:
                    if id3[id5-1][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8]=="#":
                        id4[id5][id8]+=1
                else:
                    if id3[id5-1][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5-1][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5][id8+1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8-1]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8]=="#":
                        id4[id5][id8]+=1
                    if id3[id5+1][id8+1]=="#":
                        id4[id5][id8]+=1
id9=""
for id5 in id6(id0):
    for id8 in id6(id1):
        id9+=id10(id4[id5][id8])
    print(id9)
    id9=""