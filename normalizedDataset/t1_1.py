from id0 import id1
id2, id3, id4=map(id5, input().split())
class id6(id7):
    def id8(id9, id10):
        id9.id10=id10
        id9.id11=id12(id13(id10))
        id9.id14=[1]*id10
    def id15(id9, id16, id17):
        return id9.id18(id16)==id9.id18(id17)
    def id18(id9, id19):
        if id9.id11[id19]==id19:
            return id19
        id9.id11[id19]=id9.id18(id9.id11[id19])
        return id9.id11[id19]
    def id20(id9, id19, id21):
        id19=id9.id18(id19)
        id21=id9.id18(id21)
        if id19==id21:
            return
        if id9.id14[id19]>id9.id14[id21]:
            id9.id11[id21]=id19
        elif id9.id14[id19]<id9.id14[id21]:
            id9.id11[id19]=id21
        else:
            id9.id11[id21]=id19
            id9.id14[id19]+=1
id22=id6(id2)
id23=id6(id2)
for id24 in id13(id3):
    id25, id26=map(id5, input().split())
    id25-=1
    id26-=1
    id22.id20(id25, id26)
for id27 in id13(id4):
    id28, id29=map(id5, input().split())
    id28-=1
    id29-=1
    id23.id20(id28, id29)
id30=[]
id31=id1(id5)
for id32 in id13(id2):
    id33=id22.id18(id32)
    id34=id23.id18(id32)
    id31[id33, id34]+=1
for id32 in id13(id2):
    id33=id22.id11[id32]
    id34=id23.id11[id32]
    if id32==id2-1:
        print(id31[id33, id34])
    else:
        print(id31[id33, id34], id35=" ")