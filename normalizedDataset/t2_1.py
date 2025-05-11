import id0
id1=id0.id2.id1
id3=id0.id4.id3
id5=id0.id4.id5
def id6(id7):
    id3("?%d\n"%id7)
    id5()
    return id1().id8()=="Y"
def id9(id7):
    id3("!%d\n"%id7)
    id5()
id10=None
for id11 in id12(10):
    if not id6(10**id11):
        id10=id11
        break
else:
    for id11 in id12(10):
        if id6(10**id11+1):
            id9(10**id11)
            break
    id13(0)
id14=10**(id10-1); id15=10**id10
while id14+1<id15:
    id16=(id14+id15)/2
    if id6(id16*10):
        id15=id16
    else:
        id14=id16
id9(id15)