import id0
id1,id2,id3=map(id4,id5().split())
id6=map(id4,id5().split())
id7=1000000007

def id8(id2,id9,id7):
    id10=1
    id11=id2
    while id9!=0:
        if id9%2==1:
            id10*=id2
            id10%=id7
        id2*=id2
        id2%=id7
        id9/=2
    return id10

if id2==1:
    id6.id12()
    for id13 in id6:
        print id13
    id14()

id15=id16(id6)
id17=0
for id18 in id19(id1):
    id20=id6[id18]
    while id20*id2<id15:
        id20*=id2
        id17+=1

if id17>id3:
    id0.id21(id6)
    for id17 in id22(id3):
        id23=id6[0]
        id0.id24(id6)
        id0.id25(id6,id23*id2)
    for id18 in id19(id1):
        print id6[0]
        id0.id24(id6)

else:
    for id18 in id19(id1):
        while id6[id18]*id2<id15:
            id6[id18]*=id2
            id3-=1
    id6.id12()
    id9=id3/id1
    id26=id8(id2,id9,id7)
    id27=id3%id1
    for id18 in id19(id1):
        id6[id18]*=id26
        id6[id18]%=id7
    for id18 in id19(id27):
        id6[id18]*=id2
        id6[id18]%=id7
    for id18 in id19(id27,id1):
        print id6[id18]
    for id18 in id19(id27):
        print id6[id18]

