import id0
from id1 import id2
import id3
import id4 as id5

from id6 import*def id7(id8):
    if id8==None :
        return id9
    else:
        return id8.id10

def id11():
    if id12(id0.id13)>1:
        id14=id15(id0.id13[1])
    else:
        id14=None
    id16=id7(id14);
    id17=id16().id18().split()
    [id19, id20]=[id21(id17[0]), id21(id17[1])]
    id17=id16().id18().split()
    [id22]=[id21(id17[0])]
    id17=id23(id16().id18().split())
    #color_num_list=[]
    #color_num_list={}
    id24=id5.id25((id22))
    for id26 in id27(id22):
        id24[id26]=(id21(id17[id26]))

    id28=id5.id29(id24)[::-1]
    id30=id5.id31(id24)[::-1]

    id32=id5.id25((id19, id20),"int")
    id33=0
    id34=0
    id35=False
    #tmp_color_num_list=copy.deepcopy(color_num_list)
    #while len(color_num_list)>0:
        #color_num=max(color_num_list.values())
        #color=color_num_list.keys()[color_num_list.values().index(color_num)]
        #color_num_list.pop(color)
        #tmp_color_num_list.remove(color_num)
    for id26 in id27(id22):
        id36=id30[id26]
        id37=id28[id26]+1
        while id36>0:
            id32[id33][id34]=id37
            if (id34<id20-1 and id35==False)  or  (id34>=1 and id35==True):
                id38=-1 if id35==True else 1
                id34+=id38
            else:
                id33+=1
                id35=not(id35)
            id36-=1

    for id26 in id27(id19):
        for id39 in id27(id20):
            print id32[id26][id39],
        print


if id40=="__main__":
    id11()