id0=id1(input())
id2=id1(input())
id3=[id1(id4) for id4 in id5(input().split())]
for id6 in id7(0,id2-1): id3[id6]-=id3[id6+1]
id8=id1(input())

id9=id0
id10=id0
id11=0
id12=0
id13=0
id14=-1
id15=id3.id16()

def id17(id18):
    global id9,id10,id11,id12
    if id14==1:
        if id12+id18>id0:
            id12=id0
            id10=id0
            id9=id11
        elif id10+id18>id0:
            id12+=id18
            id10=id0
            id9=id11+id10-id12
        else:
            id12+=id18
            id10+=id18
    else:
        if id10-id18<0:
            id12=0
            id10=0
            id11=id9
        elif id12-id18<0:
            id12=0
            id10-=id18
            id11=id9+id12-id10
        else:
            id12-=id18
            id10-=id18

for id6 in id7(id8):
    id19,id20=[id1(id4) for id4 in input().split()]
    id19-=id13
    id13+=id19
    
    while id19>=id15:
        id17(id15)
        id19-=id15
        if id3:
            id15=id3.id16()
        else:
            id15=id21("inf")
        id14*=-1
    
    id17(id19)
    id15-=id19
    
    if id20<id11:
        print(id12)
    elif id20>id9:
        print(id10)
    else:
        print(id12+id20-id11)