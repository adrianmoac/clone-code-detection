import id0
from id1 import id2
import id3

from id4 import*def id5(id6):
    if id6==None :
        return id7
    else:
        return id6.id8

class id9():
    def id10(id11):
        if id11.id12<=id11.id13*id11.id14/100:
            return True
        return False
    def id15(id11, id13, id12, id14):
        id11.id13=id13
        id11.id12=id12
        id11.id16=id13+id12
        id11.id14=id14
        id11.id17=id11.id10()
        if id11.id12+id11.id13>0:
            id11.id18=id11.id12*100.0/id19(id11.id12+id11.id13)
        else:
            id11.id18=-1.0


    def id20(id11,id21):
        return (id11.id13==id21.id13) and (id11.id12==id21.id12)

    def id22(id11):

        return id23 (id11.id13+id11.id12*10000)


def id24(id25, id26, id27, id28, id29, id30):
    id31=id9(0, 0, id29)
    id32=id33([id31])
    id34=id2([id31])
    id35=id31
    while id36(id34)>0:
        id31=id34.id37()
        #ope1
        id38=[]
        id38.id39(id9(id31.id13+id25*100, id31.id12, id29))
        id38.id39(id9(id31.id13+id26*100, id31.id12, id29))
        id38.id39(id9(id31.id13, id31.id12+id27, id29))
        id38.id39(id9(id31.id13, id31.id12+id28, id29))
        for id40 in id38:
            if id40.id16<=id30:
                if id40 not in id32:
                    id32.id41(id40)
                    id34.id39(id40)
                    if id40.id17==True and id40.id18>id35.id18:
                        id35=id40
    return id35


def id42():
    if id36(id0.id43)>1:
        id44=id45(id0.id43[1])
    else:
        id44=None
    id46=id5(id44);
    id47=id46().id48().split()
    [id25, id26, id27, id28, id29, id30]=[id49(id47[0]), id49(id47[1]), id49(id47[2]), id49(id47[3]), id49(id47[4]), id49(id47[5])]
    id50=id24(id25, id26, id27, id28, id29, id30)
    print id49(id50.id16), id49(id50.id12)

if id51=="__main__":
    id42()