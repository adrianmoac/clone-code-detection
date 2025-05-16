import id0
from id1 import id2

class id3:

    def id4(id5, id6):
        id5.id7=id8(id9(id6))
        id5.id10=[0]*id6

    def id11(id5, id12):
        if id12!=id5.id7[id12]:
            id5.id7[id12]=id5.id11(id5.id7[id12])

        return id5.id7[id12]

    def id13(id5, id12, id14):
        return id5.id11(id12)==id5.id11(id14)

    def id15(id5, id12, id14):
        id16=id5.id11(id12)
        id17=id5.id11(id14)

        if id16==id17:
            return

        if id5.id10[id16]<id5.id10[id17]:
            id5.id7[id16]=id17
        else:
            id5.id7[id17]=id16

            if id5.id10[id16]==id5.id10[id17]:
                id5.id10[id16]+=1


id18, id19, id20=map(id21, id0.id22.id23().split())

id24=id3(id18)
id25=id3(id18)

for id26 in id9(id19):
    id7, id27=map(id21, id0.id22.id23().split())
    id7, id27=id7-1, id27-1
    id24.id15(id7, id27)

for id26 in id9(id20):
    id28, id29=map(id21, id0.id22.id23().split())
    id28, id29=id28-1, id29-1
    id25.id15(id28, id29)

id30=id2()

for id26 in id9(id18):
    id16=id24.id11(id26)
    id17=id25.id11(id26)

    id30[(id16, id17)]+=1

id31=[]

for id26 in id9(id18):
    id16=id24.id11(id26)
    id17=id25.id11(id26)

    id31.id32(id30[(id16, id17)])

print(*id31)