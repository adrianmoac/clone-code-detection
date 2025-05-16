#coding=UTF-8

id0=[]
def id1(id2,id3,id4):
    global id0
    global id5

    if id3==id5:
        id6=0
        if id7(id2):
            id6=id8(id2)
        return id9(id6,id4)
    else:
        id10=0
        if id7(id2+[1]):
            id10=id1(id2+[1],id3+1,id9(id4,id8(id2)+1))

        id10=id9(id1(id2+[0],id3+1,id4),id10)
        return id10

def id7(id11):
    id12=[]
    for id13 in id14(0,id15(id11),1):
        if id11[id13]==1:
            id12.id16(id13)

    return id17(id12)

def id17(id18):
    if id15(id18)<=1:
        return True
    else:
        id19=id18[0]
        id20=id18[1:id15(id18)]
        id10=True
        for id11 in id20:
            if id0[id11][id19]==False:
                return False
        return id17(id20)

id21=input()
id22=id21.split(" ")

id5=id23(id22[0])
id24=id23(id22[1])

id25=[]
for id13 in id14(0,id24,1):
    id21=input()
    id22=id21.split(" ")
    id25.id16((id23(id22[0])-1,id23(id22[1])-1))


for id13 in id14(0,id5,1):
    id0.id16([False]*id5)

for id26 in id25:
    id0[id26[0]][id26[1]]=True
    id0[id26[1]][id26[0]]=True

id27=id1([],0,0)
print(id27)