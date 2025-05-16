import id0

class id1:
    def id2(id3, id4):
        id3.id5=[1]*id4
        id3.id6=[1]*id4
        id3.id7=[ id8 for id8 in id9(id4) ]

    def id10(id3, id11):
        if id11==id3.id7[id11]:
            return id11
        else:
            id3.id7[id11]=id3.id10(id3.id7[id11])
            return id3.id7[id11]

    def id12(id3, id11, id13):
        return id3.id10(id11)==id3.id10(id13)

    def id14(id3, id11, id13):
        id15=id3.id10(id11)
        id16=id3.id10(id13)
        if id15==id16:
            return
        if id3.id5[id15]>id3.id5[id16]:
            id3.id7[id16]=id15
            id3.id6[id15]+=id3.id6[id16]
        else:
            id3.id7[id15]=id16
            id3.id6[id16]+=id3.id6[id15]
            if id3.id5[id15]==id3.id5[id16]:
                id3.id5[id16]+=1

#####

id17,id18=map(id19,input().split())

id20=[]
for id8 in id9(id18):
    id21, id22, id13=map(id19, id0.id23.id24().split())
    id20.id25( (id21,id22,id13) )
id20=id26(id20, id27=lambda id11: id11[2], id28=True)

id29=id1(id17+1) # 1-base

id30=[]
id31=id19(input())
for id8 in id9(id31):
    id32, id33=map(id19, id0.id23.id24().split())
    id30.id25( (id8,id32,id33) )

id30=id26(id30, id27=lambda id11: id11[2], id28=True)

id34=[]
id35=0
for id36 in id30:
    id8, id32, id33=id36
    while id35<id37(id20) and id20[id35][2]>id33:
        id29.id14(id20[id35][0], id20[id35][1])
        id35+=1
    id34.id25( (id8,id29.id6[id29.id10(id32)]) )

for id36 in id26(id34, id27=lambda id11: id11[0]):
    print(id36[1])
