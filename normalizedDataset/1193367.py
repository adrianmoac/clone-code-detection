from id0 import id1
from id2 import id3

def id4():
    id5, id6=map(id7, id1.id8().split())
    id9=[[id7(id10) for id10 in id1.id8().split()] for id11 in id12(id6)]
    id13=id7(id1.id8())
    id14=[[id7(id10) for id10 in id1.id8().split()]+[id11] for id11 in id12(id13)]

    id9.id15(id16=id3(2), id17=True)
    id14.id15(id16=id3(1), id17=True)

    id18=0
    id19=id20(id5)
    id21=[0]*id13

    for id22, id23, id11 in id14:
        for id10 in id12(id18, id6):
            id24, id25, id26=id9[id10]

            if id26<=id23:
                id18=id10
                break

            id19.id27(id24-1, id25-1)
        else:
            id18=id6

        id21[id11]=id19.id28(id22-1)

    print(*id21, id29="\n")

class id20:
    def id30(id31, id5):
        id31.id32=id33(id12(id5))
        id31.id34=[0]*id5
        id31.id35=[1]*id5

    def id36(id31, id37):
        if id31.id32[id37]!=id37:
            id31.id32[id37]=id31.id36(id31.id32[id37])

        return id31.id32[id37]

    def id38(id31, id37, id26):
        return id31.id36(id37)==id31.id36(id26)

    def id27(id31, id37, id26):
        id39=id31.id36(id37)
        id22=id31.id36(id26)

        if id39==id22: return

        if id31.id34[id39]<id31.id34[id22]:
            id31.id32[id39]=id22
            id31.id35[id22]+=id31.id35[id39]
            id31.id35[id39]=0
        else:
            id31.id32[id22]=id39
            id31.id35[id39]+=id31.id35[id22]
            id31.id35[id22]=0

            if id31.id34[id39]==id31.id34[id22]:
                id31.id34[id39]+=1

    def id28(id31, id37):
        return id31.id35[id31.id36(id37)]

if id40=="__main__":
    id4()