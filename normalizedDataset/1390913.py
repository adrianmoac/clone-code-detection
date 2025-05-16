class id0:
    def id1(id2, id3):
        id2.id4=[-1 for _ in id5(id3)]
 
    def id6(id2, id7):
        if id2.id4[id7]<0:
            return id7
        else:
            id2.id4[id7]=id2.id6(id2.id4[id7])
            return id2.id4[id7]
 
    def id8(id2, id7, id9):
        id10=id2.id6(id7)
        id11=id2.id6(id9)
        if id10!=id11:
            if id2.id4[id10]<=id2.id4[id11]:
                id2.id4[id10]+=id2.id4[id11]
                id2.id4[id11]=id10
            else:
                id2.id4[id11]+=id2.id4[id10]
                id2.id4[id10]=id11
            return True
        return False
 
def id12(id13,id14):
    id15=id16(id14)
    for id17 in id5(id15-1):
        id18=id19(id14[id17+1][0]-id14[id17][0])
        try:
            id20=id13[id18]
            id20.id21([id14[id17+1][1],id14[id17][1]])
            id13[id18]=id20
        except:
            id13[id18]=[[id14[id17+1][1],id14[id17][1]]]
    return id13
id15=id22(input())
id7=[[0,0] for _ in id5(id15)]
id9=[[0,0] for _ in id5(id15)]
for id17 in id5(id15):
    id7[id17][0],id9[id17][0]=id23(map(id22,input().split()))
    id7[id17][1],id9[id17][1]=id17,id17
id7=id24(id7,id25=lambda id20: id20[0])
id9=id24(id9,id25=lambda id20: id20[0])
id26=id12(id12({},id7),id9)
id27=id0(id15)
id28=0
id29=0
id30=0
while True:
    if(id30==id15-1):
        print(id29)
        break
    try:
        id20=id26[id28]
        for id31 in id20:
            if(id27.id8(id31[0],id31[1])):
                id29+=id28
                id30+=1
            
        id28+=1
    except:
        id28+=1
        continue