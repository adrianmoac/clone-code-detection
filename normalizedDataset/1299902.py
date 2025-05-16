import id0
class id1:
    def id2(id3, id4):
        id3.id4=id4
        id3.id5=[[] for id6 in id7(id4)]
    def id8(id3, id9, id10, id11):
        id3.id5[id9].id12([id10, id11, id13(id3.id5[id10])])
        id3.id5[id10].id12([id9, 0, id13(id3.id5[id9])-1])
    def id14(id3, id15, id16, id17, id18):
        id3.id5[id15].id12([id16, id17, id13(id3.id5[id16])])
        id3.id5[id16].id12([id15, id18, id13(id3.id5[id15])-1])
    def id19(id3, id20):
        id21=[-1]*id3.id4
        id22=id0.id23()
        id21[id20]=0
        id22.id12(id20)
        while id22:
            id24=id22.id25()
            for id26 in id3.id5[id24]:
                if id26[1]>0 and id21[id26[0]]<0:
                    id21[id26[0]]=id21[id24]+1
                    id22.id12(id26[0])
        id3.id21=id21
    def id27(id3, id24, id28, id29):
        if id24==id28: return id29
        id30=id3.id5[id24]
        id21=id3.id21
        for id6 in id7(id3.id31[id24], id13(id3.id5[id24])):
            id26=id30[id6]
            if id26[1]>0 and id21[id24]<id21[id26[0]]:
                id32=id3.id27(id26[0], id28, id33(id29, id26[1]))
                if id32>0:
                    id26[1]-=id32
                    id3.id5[id26[0]][id26[2]][1]+=id32
                    id3.id31[id24]=id6
                    return id32
        id3.id31[id24]=id13(id3.id5[id24])
        return 0
    def id34(id3, id20, id28):
        id35=0
        while True:
            id3.id19(id20)
            if id3.id21[id28]<0: break
            id3.id31=[0]*id3.id4
            while True:
                id29=id3.id27(id20, id28, 10**9+7)
                if id29>0:
                    id35+=id29
                else:
                    break
        return id35
id36, id37=map(id38, id39().split())
id40=[id39() for id6 in id7(id36)]
id41=id1(id36+id37+2)
id42=id36+id37; id43=id36+id37+1
id44=10**9+7
for id6 in id7(id36):
    for id45 in id7(id37):
        id46=id40[id6][id45]
        if id46 is "o":
            id41.id14(id6, id36+id45, 1, 1)
        elif id46 is "S":
            id41.id8(id42, id6, id44)
            id41.id8(id42, id36+id45, id44)
        elif id46 is "T":
            id41.id8(id6, id43, id44)
            id41.id8(id36+id45, id43, id44)
id47=id41.id34(id42, id43)
if id47>=id44:
    print-1
else:
    print id47