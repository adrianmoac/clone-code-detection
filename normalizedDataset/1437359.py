import id0
from id1 import id2
import id3

from id4 import*def id5(id6):
    if id6==None :
        return id7
    else:
        return id6.id8

class id9():
    def id10(id11, id12, id13):
        id11.id12=id12
        id11.id13=id14(id13)
        id11.id13.id15(id12)

    def id16(id11, id12):
        id11.id12=id12
        id11.id13.id15(id12)

def id17():
    if id18(id0.id19)>1:
        id20=id21(id0.id19[1])
    else:
        id20=None
    id22=id5(id20);
    id23=id22().id24().split()
    [id25]=[id26(id23[0])]

    id27={}
    for id28 in id29(id25):
        id27[id28+1]=[]

    for id28 in id29(id25-1):
        id23=id30(id22().id24().split())
        id27[id26(id23[0])].id31(id26(id23[1]))
        id27[id26(id23[1])].id31(id26(id23[0]))


    #node_list=[mas_node(1, [])]
    id32=[False]*id25
    id32[0]=True
    id33=[1]
    id34=0
    while 1:
        #count+=1
        #print count
        #new_node_list=[]
        id35=id33[id18(id33)-1]
        id32[id35-1]=True
        id36=True
        if id35==id25:
            break;
        for id37 in id27[id35]:
            if id32[id37-1]==False:
                id36=False
                id33.id31(id37)
        if id36==True:
            id33.id38()
        if id18(id33)==0:
            break;

    id39=id2([])
    for id28 in id29(id18(id33)):
        if id32[id33[id28]-1]==True:
            id39.id31(id33[id28])


    id39.id40()
    id39.id38()
    id41=[False]*id25
    id42={}
    id42["b"]=[1]
    id42["w"]=[id25]
    id43=id18(id39)

    #print to_N_pass_route
    for id28 in id29(id43):
        if id18(id39)==0:
            break;
        id44=id39.id40()
        id41[id44-1]=True
        id42["b"].id31(id44)
        if id18(id39)==0:
            break;
        id45=id39.id38()
        id41[id45-1]=True
        id42["w"].id31(id45)

    id46=id3.id47(id42["b"])
    id48=id3.id47(id42["w"])
    while 1:
        id49=[]
        for id50 in id46:
            for id51 in id27[id50]:
                if id41[id51-1]==False:
                    id42["b"].id31(id51)
                    id49.id31(id51)
                    id41[id51-1]=True
        id46=id3.id47(id49)

        id52=[]
        for id53 in id48:
            for id54 in id27[id53]:
                if id41[id54-1]==False:
                    id42["w"].id31(id54)
                    id52.id31(id54)
                    id41[id54-1]=True
        id48=id3.id47(id52)

        if id18(id48)==0&id18(id46)==0:
            break;

    if id18(id42["b"])>id18(id42["w"]):
        print "Fennec"
    else:
        print "Snuke"



if id55=="__main__":
    id17()