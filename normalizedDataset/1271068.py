# ARC59 D input
id0=id1(map(id2, input().split()))

id3=id0[0]
id4=id0[1]
id5=id0[2]
id6=id1(id7(id8(id1(map(id2, input().split())))))

# ARC59 D naive
def id9(id10):
    id11=[]
    id12=id6[0]
    id9=1
    for id13, id14 in id15(id6[1:id10]):
        if (id14==id12):
            id9+=1
        else:
            id11.id16(id9)
            id9=1
        
        if(id13==id10-2):
            id11.id16(id9)
        id12=id14
        
    return id11
        
def id17(id10):
    return id18(id6[0:id10])/id10

def id19(id10):
    id20=1
    for id13 in id21(1,id10+1):
        id20*=id13
    return id20

def id22(id23, id24):
    id25=1
    for id13 in id21(id24):
        id25*=(id23-id13)
    return id2(id25/id19(id24))


id26=-1
id27=0
id28=id9(id3)

for id13 in id21(id4, id5+1):
    id24=id13 # u is the number of items to pick
    id29=id17(id13)
    if (id26<=id29):
        for id30 in id28:
            if (id24-id30<=0):
                if (id26!=id29):
                    id27=id22(id30, id24)
                else:
                    id27+=id22(id30, id24)
                break
            else:
                id24-=id30
        id26=id29
print(id26)
print(id27)