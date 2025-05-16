
class id0:
    def id1(id2):
        pass

class id3:
    def id1(id2,id4,id5=1):
        id2.id6=id4[0]
        id2.id7=id4[1]
        id2.id5=id5

    def id8(id2,id9):
        id2.id10.id11(id9)

class id12:

    def id1(id2):
        id2.id13={}
        id2.id10={}

    def id14(id2,id4,id5):
        if id15(id4)==1:
            id4=id16(id4)

        id17,id18=id4[0],id4[1]

        if id17 not in id2.id10:
            id2.id13[id17]={}
            id2.id10[id17]={}

        if id18 not in id2.id10:
            id2.id13[id18]={}
            id2.id10[id18]={}

        # add the edge
        id2.id13[id17][id18]=id5
        id2.id13[id18][id17]=id5

    def id19(id2,id4,id5):
        if id15(id4)==1:
            id4=id16(id4)


        id17,id18=id4[0],id4[1]

        if id17 not in id2.id10:
            id2.id13[id17]={}
            id2.id10[id17]={}

        if id18 not in id2.id10:
            id2.id13[id18]={}
            id2.id10[id18]={}

        id2.id13[id17][id18]=id5

    def id20(id2,id9):
        return [(id2.id13[id9][id21],id9,id21) for id21 in id2.id13[id9]]


    def id22(id2):
        id23=[]
        for id24 in id2.id10:
            for id25 in id2.id20(id24):
                id23.id11(id3([id25[1],id25[2]],id25[0]))

        return id23

    def id26(id2,id23,id27):
        for id25 in id27:
            id28.id29(id23,id25)
        return id23

    def id30(id2,id31,id32=0):

        id10=id2.id10
        id33={}
        for id34 in id10:
            id33[id34]=id35("inf")

        id33[id31]=id32
        id23=id2.id22()

        for id36 in id37(id15(id10)):
            id38=False
            for id39 in id37(id15(id23)):
                id25=id23[id39]
                if  id33[id25.id6]!=id35("inf") and id33[id25.id7]>id33[id25.id6]+id25.id5:
                    id33[id25.id7]=id33[id25.id6]+id25.id5
                    id38=True

            if id36==id15(id10)-1:
                return False

            if not id38:
                break

        return id33


    def id40(id2,id31, id41=None):
        import id42
        """
            get minimum cost
        """

        id43=id15(id2.id13)          # グラフのノード数
        #dist=[float('inf') for i in range(N)] # 始点から各頂点までの最短距離を格納する
        id44={id39:id35("inf") for id39 in id2.id10}
        #prev=[float('inf') for i in range(N)]

        id44[id31]=0
        id45=[]

        id46=[]
        id42.id29(id46,(0,id31))

        id47=id16(id2.id10)
        id47.id48(id31)

        while id15(id46)!=0:
            id49,id50=id42.id51(id46)
            if id44[id50]<id49:
                continue


            for id39 in id16(id2.id13[id50]):
                id5=id2.id13[id50][id39]
                if id5!=id35("inf") and id44[id39]>id44[id50]+id5:# and not(k in visited):
                    id44[id39]=id44[id50]+id5
                    id42.id29(id46,(id44[id39],id39))
                    #prev[k]=mini

        return id44



id43=id52(input())

id53=id12()
for id36 in id37(id43-1):
    id54,id55=id16(map(id52,input().split(" ")))
    id53.id14([id54,id55],1)

id56=id53.id40(1)
id57=id53.id40(id43)

id58=0
for id39 in id37(1,id43+1):
    if id56[id39]<=id57[id39]:
        id58+=1

if id58>id43/2:
    print("Fennec")
else:
    print("Snuke")