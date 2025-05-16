from id0 import id1
input=id1.id2
id3,id4=map(id5,input().split())
id6=id7(map(id5,input().split()))
id8=10000000000
id9=[id6[-1]]
id10=[1]

for id11 in id6[-2:-id3-1:-1]:
    if id11==id9[-1]:
        id10.id12(id10[-1]+1)
    else:
        id10.id12(1)
    id9.id12(id13(id9[-1],id11))
id9.id14()
id10.id14()

id15={}
for id16 in id17(id3-1,-1,-1):
    if id9[id16]==id6[id16]:
        id15[id9[id16]]=id16

id18=0
id19=0
id20=0
id21=0
id22=[]
id23=[]
for id24,id11 in id25(id6):
    if id24==id3-1:
        break
    id26=id9[id24+1]
    id27=id26-id11
    #print(jump,bestSellingPrice,biggestJump)
    if id27>id18:
        id18=id27
        #LPcount+=1
        id23=[]
        id22=[]
        
        id23.id12(1)
        id19=id26
        #HPcount=highestCount[indexOfHighest[bestSellingPrice]]
        id22.id12(id10[id15[id26]])
    elif id27==id18:
        if id26!=id19:
            id19=id26
            #HPcount+=highestCount[indexOfHighest[bestSellingPrice]]
            id22.id12(id10[id15[id26]])
            id23.id12(0)
        id23[-1]+=1
id28=0
id29=id4//2
for id30,id31 in id32(id22,id23):
    if id29>id33(id30,id31):
        id28+=id33(id30,id31)
    else:
        id28+=id29
print(id28)