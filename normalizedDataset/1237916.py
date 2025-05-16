import id0
import id1

id2=10**9+7

def id3(id4):
    if(id4==1):
        return 1
    else:
        return(id4*id3(id4-1))

def id5(id6, id7):
    if(id6==id7 or id7==1):
        return 1
    else:
        return id3(id6)/(id3(id6-id7)*id3(id7))

id8=id0.id8
def id9(): return map(id10, id8.id11().split())
def id12(): return id8.id11().id13()
def id14(): return id15(id8.id11().id13())
def id16(): return id10(id8.id11())
def id17(): return id15(map(id10, id8.id11().split()))

id6=id16()
id18=id17()

id19=[]

for id4 in id20(id6):
    id19.id21(id18[id4])


id22=0

id23=0
id24=0

if id18[0]==0:
    id18[0]=1
    id23+=1;

for id4 in id20(0, id6-1):
    id22+=id18[id4]

    id25=id22+id18[id4+1]

    if id25==0:
        if id22>0:
            id18[id4+1]-=1
            id25-=1
            id23+=1

    if(id22*id25>=0):
        id3=id26(id25)+1

        id27=id3-(id26(id22)-1)
        id28=id3-id27

        if id22>0 :
            id18[id4]-=id28
            id22-=id28
            id18[id4+1]-=id27
        else:
            id18[id4]+=id28
            id22+=id28
            id18[id4+1]+=id27

        id23+=id27+id28


id22=0

id18=id19

if id18[0]==0:
    id18[0]=-1
    id24+=1;
else:
    id24=id26(id18[0])+1
    if id18[0]>0:
        id18[0]=-1
    else:
        id18[0]=1

for id4 in id20(0, id6-1):
    id22+=id18[id4]

    id25=id22+id18[id4+1]

    if id25==0:
        if id22>0:
            id18[id4+1]-=1
            id25-=1
            id24+=1

    if(id22*id25>=0):
        id3=id26(id25)+1

        id27=id3-(id26(id22)-1)
        id28=id3-id27

        if id22>0 :
            id18[id4]-=id28
            id22-=id28
            id18[id4+1]-=id27
        else:
            id18[id4]+=id28
            id22+=id28
            id18[id4+1]+=id27

        id24+=id3

print(id29(id23, id24))



