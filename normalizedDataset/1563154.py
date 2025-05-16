# F
# input
from id0 import id0
id1=id2(input())
id3=id2(input())
id4=[0]+id5(map(id2, input().split()))

id6=id2(input())
id7=[id5(map(id2, input().split())) for _ in id8(id6)]


id9=[]

# M:max, m:min, R:min_a(M), L:max_a(m)
id10=id1
id11=0
id12=id1
id13=0

id9.id14([id10, id11, id12, id13])

for id15 in id8(id3):
    id16=id10
    id17=id11
    id18=id12
    id19=id13
    id20=id4[id15+1]-id4[id15]
    # update
    if id15%2==0:
        if id16-id20<0:
            id10=0
            id12=0
        else:
            id10=id16-id20
            id12=id18
        if id17-id20<0:
            id11=0
            id13=id19+id20-id17
        else:
            id11=id17-id20
            id13=id19
    else:
        if id16+id20>id1:
            id10=id1
            id12=id18-(id16+id20-id1)
        else:
            id10=id16+id20
            id12=id18
        if id17+id20>id1:
            id11=id1
            id13=id1
        else:
            id11=id17+id20
            id13=id19
    id9.id14([id10, id11, id12, id13])
        

# print(MmRL_list)
for id21 in id8(id6):
    id22, id23=id7[id21]
    id24=id0(id4, id22)-1
    # find status then
    id10, id11, id12, id13=id9[id24]
    if id23<=id13:
        id25=id11
    elif id23>=id12:
        id25=id10
    else:
        id25=id11+(id23-id13)
    id26=id22-id4[id24]
    if id24%2==0:
        id27=id28(id25-id26, 0)
    else:
        id27=id29(id25+id26, id1)
    print(id27)