id0=input()
id1=input()
id2=id3(input())

id4=[]
id5=[]
id6=0
id7=0
for id8 in id0:
    if id8=="A":
        id6+=1
    else:
        id7+=1
    id4.id9(id6)
    id5.id9(id7)

id10=[]
id11=[]
id6=0
id7=0
for id12 in id1:
    if id12=="A":
        id6+=1
    else:
        id7+=1
    id10.id9(id6)
    id11.id9(id7)


def id13(id14, id15, id16, id17):
    id18=id4[id15-1]
    id19=id5[id15-1]
    if id14>=2:
        id18-=id4[id14-2]
        id19-=id5[id14-2]
    id20=id10[id17-1]
    id21=id11[id17-1]
    if id16>=2:
        id20-=id10[id16-2]
        id21-=id11[id16-2]
    """
    print(sa, sb)
    print(ta, tb)
    """

    id19+=2*id18
    id19%=3

    id21+=2*id20
    id21%=3

    return id19==id21


for id22 in id23(id2):
    id14, id15, id16, id17=map(id3, input().split())
    if id13(id14, id15, id16, id17):
        print("YES")
    else:
        print("NO")