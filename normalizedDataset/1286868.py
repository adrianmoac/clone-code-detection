import id0
id0.id1(100000)

def id2(id3, id4, id5):
    if id3 in id4:
        for id6 in id4[id3]:
            if id5[id6-1]==0:
                id5[id6-1]=1
                id2(id6, id4, id5)


id7, id8=map(id9, input().split())
id10=id11("-inf")
id12=-id10

id4={}
id13={}
for id14 in id15(id8):
    id16, id17, id18=map(id9, input().split())
    if id16 in id13:
        id13[id16].id19((id17, id18))
    else:
        id13[id16]=[(id17, id18)]

    if id17 in id4:
        id4[id17].id19(id16)
    else:
        id4[id17]=[id16]


# path cut
id5=[0 for id14 in id15(id7)]
id5[id7-1]=1
id2(id7, id4, id5)

for id16, id20 in id13.id21():
    if not id5[id16-1]:
        id13[id16]=[]
    else:
        id22=[]
        for id17, id18 in id20:
            if id5[id17-1]:
                id22.id19((id17, id18))
        id13[id16]=id22


id23=[id10 for id14 in id15(id7)]
id23[0]=0

id24=False
for id25 in id15(id7):
    for id16 in id13.id26():
        for id17, id18 in id13[id16]:
            id23[id17-1]=id27(id23[id17-1], id23[id16-1]+id18)

# loop check
if not id24:
    id28=id23[id7-1]
    for id16 in id13.id26():
        for id17, id18 in id13[id16]:
            id23[id17-1]=id27(id23[id17-1], id23[id16-1]+id18)
    if id28!=id23[id7-1]:
        id24=True


if id24:
    print("inf")
else:
    print(id23[id7-1])