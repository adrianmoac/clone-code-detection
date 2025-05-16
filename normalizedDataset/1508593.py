
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

    def id52(id2):

        import id42

        id10=id16(id2.id10.id53())
        id43=id15(id10)

        id54=[id10[0]]
        id55=[]
        for id17 in id2.id13[id54[0]]:
            id42.id29(id55,(id2.id13[id54[0]][id17],id54[0],id17))

        id56=0
        id57={id34:False for id34 in id10}
        id57[id54[0]]=True
        while True:
            #print(unused)
            #print(X,total_cost)
            id5,id17,id18=id42.id51(id55)
            if id57[id18]:
                continue
            id54.id11(id18)
            id57[id18]=True
            id56+=id5
            if id15(id54)==id43:
                break

            for id17 in id2.id13[id18]:
                if id57[id17]:
                    continue
                id42.id29(id55,(id2.id13[id17][id18],id18,id17))

        return id56




    def id58(id2):

        import id59 as id60
        import id61.id62 as id63
        id64=id60.id65()

        for id17 in id2.id13:
            for id18 in id2.id13[id17]:

                #G.add_edge(e.node_from,e.node_to,weight=e.cost)
                id64.id14(id17,id18,id66=id2.id13[id17][id18])
                #print(e.node_from,e.node_to,e.cost)

        id67=id60.id68(id64)
        #nx.draw_networkx_edges(G,pos=pos,edgelist=G.edges())
        id69=id70([((id17,id18,),id71(id49["weight"])) for id17,id18,id49 in id64.id23(id72=True)])

        id60.id73(id64,id67,id74=id69)
        #nx.draw_networkx_labels(G, pos)
        id60.id75(id64,id67)
        id60.id76(id64,id67)
        id60.id77(id64,id67)
        #plt.axis('off')
        #nx.draw(G,with_labels=True)
        id63.id58()



def id78():
    id79=input()
    if id15(id79)==0:
        return False

    return id16(map(id71,id79.split(" ")))

if id80=="__main__":

    id43=id71(input())

    id81=id12()


    for id36 in id37(id43-1):
        try:
            id82=id78()
            if not id82:
                break
        except:
            break
        id81.id14((id82[0],id82[1]),id82[2])
        #g.add_directed_edge((ss[0],ss[1]),ss[2])

    id83,id84=id78()

    id85=id81.id40(id84)
    id86=[]
    for id39 in id37(id83):
        id86.id11(id78())



    for id87,id88 in id86:
        print(id71(id85[id87]+id85[id88]))