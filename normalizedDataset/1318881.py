import id0

def id1(id2,id3):
    id4=id2/2
    if id2%2==0:
        #tateb
        id5=id0.id6(id3/3)
        id7=id8(id2*id5, (id3-id5)*id4)
        id9=id10(id2*id5, (id3-id5)*id4)
        id11=id7-id9
        #tates
        if id3>3:
            id5=id0.id12(id3/3)
            id7=id8(id2*id5, (id3-id5)*id4)
            id9=id10(id2*id5, (id3-id5)*id4)
        id13=id7-id9
    else:
        #tateb
        id5=id0.id6(id3/3)
        id7=id8(id2*id5, (id3-id5)*id0.id6(id4))
        id9=id10(id2*id5, (id3-id5)*id0.id12(id4))
        id11=id7-id9
        #tates
        if id2>3:
            id5=id0.id12(id3/3)
            id7=id8(id2*id5, (id3-id5)*id0.id6(id4))
            id9=id10(id2*id5, (id3-id5)*id0.id12(id4))
        id13=id7-id9
    return id0.id12(id10(id11,id13))

id2,id3=map(id14, input().split())
id15=[100000,100000,100000, 100000]

#tate3
if id2%3==0:
    id15[0]=0
elif id2>3:
    id15[0]=id3
#yoko3
if id3%3==0:
    id15[1]=0
elif id3>3:
    id15[1]=id2

#ト
if id3%3==0:
    if id2%2==0:
        id15[2]=0
    elif id2>2:
        id15[2]=id0.id12(2*id3/3)
else:
    id15[2]=id1(id2,id3)
#T
if id2%3==0:
    if id3%2==0:
        id15[3]=0
    elif id3>2:
        id15[3]=id0.id12(2*id2/3)
else:
    id15[3]=id1(id3,id2)
print(id10(id15))