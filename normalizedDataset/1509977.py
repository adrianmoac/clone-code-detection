
import id0
from id1 import id2
import id3

from id4 import*def id5(id6):
    if id6==None :
        return id7
    else:
        return id6.id8

#class edge:
#    def __init__(x, y, cost):

class id9:
    def id10(id11, id12, id13):
        id11.id12=id12
        id11.id13=id13

def  id14(id15, id16):
    id17={}
    id17[id16]=0

    id18=id2([id9(id16, 0)])
    while 1:
        #new_node_list=[]
        #for i in range(len(node_list)):
        id19=id18.id20()
        id21=id15[id19.id12]
        for id22 in id21:
            if id22[0] not in id17:
                id17[id22[0]]=id22[1]+id19.id13
                id18.id23(id9(id22[0], id22[1]+id19.id13))
        if id24(id18)==0:
            break
        #node_list=copy.deepcopy(new_node_list)

    return id17


def id25():
    if id24(id0.id26)>1:
        id27=id28(id0.id26[1])
    else:
        id27=None
    id29=id5(id27);
    id30=id29().id31().split()
    [id32]=[id33(id30[0])]
    id34={}
    for id35 in id36(id32-1):
        id30=id29().id31().split()
        [id37, id38, id22]=[id33(id30[0]), id33(id30[1]), id33(id30[2])]
        if id37 not in id34:
            id34[id37]=[]
        id34[id37].id23((id38, id22))
        if id38 not in id34:
            id34[id38]=[]
        id34[id38].id23((id37, id22))

    id30=id29().id31().split()
    [id39, id40]=[id33(id30[0]), id33(id30[1])]

    id17=id14(id34, id40)

    for id35 in id36(id39):
        id30=id29().id31().split()
        [id41, id42]=[id33(id30[0]), id33(id30[1])]
        print id17[id41]+id17[id42]


if id43=="__main__":
    id25()