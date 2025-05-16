from id0 import id1
id2=0
id3=1
id4=2
id5=input()
id6={id7: [] for id7 in id8(1, id5+1)}
for id7 in id8(id5-1):
    id9, id10=map(id11, id12().split())
    id6[id9].id13(id10)
    id6[id10].id13(id9)

id14={}
id15=[id5]*(id5+1)
id15[1]=0
id16=id1([1])
while id17(id16)>0:
    id18=id16.id19()
    for id20 in id6[id18]:
        if id15[id20]>id15[id18]+1:
            id15[id20]=id15[id18]+1
            id14[id20]=id18
            id16.id13(id20)

id18=id5
id21=[id18]
while id18 in id14:
    id21.id13(id14[id18])
    id18=id14[id18]
id21=id21[::-1]

id22=[id2]*(id5+1)
id23=id17(id21)
id24, id25=id1(), id1()
for id7 in id8(id23):
    if id7%2==0:
        id26=id21[id7/2]
        id22[id26]=id3
        id24.id13(id26)
    else:
        id26=id21[id23-id7/2-1]
        id22[id26]=id4
        id25.id13(id26)

def id27(id16, id28):
    while id17(id16)>0:
        id18=id16.id19()
        for id20 in id6[id18]:
            if id22[id20]==id2:        
                id22[id20]=id28
                id16.id13(id20)
id27(id24, id3)
id27(id25, id4)
id29=0
for id28 in id22:
    if id28==id3:
        id29+=1
    elif id28==id4:
        id29-=1
print "Fennec" if id29>0 else "Snuke"