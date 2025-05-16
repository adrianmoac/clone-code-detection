#-*-cofing:utf-8-*-field=[[] for _ in range(19)]
id0=[]
id1=[]
for id2 in id3(19):
    id4=input()
    for id5,id6 in id7(id4):
        id8[id2].id9(id6)
        if id6=="x":
            id1.id9([id2,id5])
        elif id6=="o":
            id0.id9([id2,id5])

id10=[[-1,1],[0,1],[1,1],[1,0]]

def id11(id0,id1,id8):
    def id12(id13,id14,id15,id16=0):
        id17=id14[0]+id15[0]
        id18=id14[1]+id15[1]
        if 0<=id17<=18 and 0<=id18<=18:
            if [id17,id18] in id13:
                id16+=1
                return id12(id13,[id17,id18],id15,id16)
            else:
                return id16
        else:
            return id16

    def id19(id13):
        id20=0
        for id15 in id10:
            id16=0
            for id14 in id13:
                id16=id12(id13,id14,id15)
                if id16>=4:
                    return True
        return False
    id6=False
    id21=(id22(id0)-id22(id1))
    id23=id19(id0)
    id24=id19(id1)
    if not id21 in [0,1]:
        id6=True
    else:
        if id23 and id24:
            id6=True
        elif id23:
            if id21==0:
                id6=True
            else:
                id6=True
                for id14 in id0:
                    id25=[id2 for id2 in id0 if id2 not in [id14]]
                    if not id19(id25):
                        id6=False
                        break
        elif id24:
            if id21==1:
                id6=True
            else:
                id6=True
                for id14 in id1:
                    id25=[id2 for id2 in id1 if id2 not in [id14]]
                    if not id19(id25):
                        id6=False
                        break
    return id6

if id11(id0,id1,id8):
    print("NO")
else:
    print("YES")