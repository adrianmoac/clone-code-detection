id0=input()
if id0[0]=="0":
    id0="1"+id0

id1=id2(id0)
id3=id1
for id4 in id5(1, id1):
    if id0[id4]!="0":
        id3=id4
        break

id6=[]
id6.id7(id8(id0[0:id3]))
id0=id0[id3:id1]
id1=id2(id0)
if id1==0:
    print(id6[0], 1)
    id9()

if id6[0]>=id8(id0):
    id10=id8(id0)
    id11=id12(id6[0])
    id13=id2(id11)
    id14=id2(id0)
    if id13>id14 and id11[0:id14]==id0[0:id14]:
        print(id6[0], 1)
        id9()

    while id6[0]>=id10:
        id10*=10

    print(id6[0], id10-id6[0])
    id9()

def id15(id0, id16):
    if id0[0]=="0" or id16[0]=="0":
        return False

    id17=id2(id0)
    id18=id2(id16)
    id1=id19(id17, id18)
    if id0[0:id1]==id16[0:id1]:
        return True
    else:
        return False

for id4 in id5(1, id1):
    id10=[id6[0]]
    id10.id7(id8(id0[0:id4]))
    id20=id10[1]-id10[0]
    if id20<=0:
        continue

    id16=id0[id4:id1]
    while True:
        id10.id7(id10[-1]+id20)
        id21=id12(id10[-1])
        if not id15(id16, id21):
            break

        id18=id2(id16)
        id22=id2(id21)
        if id18<=id22:
            print(id10[0], id20)
            id9()

        id16=id16[id22:id18]

print(id6[0], id8(id0)-id6[0])