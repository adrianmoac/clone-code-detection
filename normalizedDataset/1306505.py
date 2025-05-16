import id0
id1,id2=map(id3,input().split())
id4=[]
id5,id6=(0,0),(0,0)
for id7 in id8(id1):
    id9=id10(input())
    if "s" in id9:
        id5=(id7,id9.id11("s"))
    if "g" in id9:
        id6=(id7,id9.id11("g"))
    id4.id12(id9)
id13=[[3 for id14 in id8(id2)] for id15 in id8(id1)]
id16=id0.id17()
id16.id12((id5[0], id5[1], 0))


id18=False
while id19(id16)>0:
    id20,id21,id22=id16.id23()
    id24=False
    if id13[id20][id21]<=id22:
        continue

    id13[id20][id21]=id22

    if id20>0:
        id15=id4[id20-1][id21]
        if id15=="g":
            id18=True
            break
        elif id15=="#":
            if id22<2:
                id16.id12((id20-1,id21,id22+1))
        else:
            id16.id12((id20-1,id21,id22))
    if id20<id1-1:
        id15=id4[id20+1][id21]
        if id15=="g":
            id18=True
            break
        elif id15=="#":
            if id22<2:
                id16.id12((id20+1,id21,id22+1))
        else:
            id16.id12((id20+1,id21,id22))
    if id21>0:
        id15=id4[id20][id21-1]
        if id15=="g":
            id18=True
            break
        elif id15=="#":
            if id22<2:
                id16.id12((id20,id21-1,id22+1))
        else:
            id16.id12((id20,id21-1,id22))
    if id21<id2-1:
        id15=id4[id20][id21+1]
        if id15=="g":
            id18=True
            break
        elif id15=="#":
            if id22<2:
                id16.id12((id20,id21+1,id22+1))
        else:
            id16.id12((id20,id21+1,id22))

if id18:
    print("YES")
else:
    print("NO")