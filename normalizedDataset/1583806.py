import id0
import id1
import id2 as id3
import id4

from id5 import*def id6(id7):
    if id7==None :
        return id8
    else:
        return id7.id9

class id10:
    def id11(id12, id13, id14):
        id12.id13=id13
        id12.id14=id14

    def id15(id12, id16):
        return id12.id14<id16.id14

class id17:
    def id11(id12):
        id12.id18={}

    def id19(id12, id20, id21):
        id22=id23()
        id24={}
        id24[id21]=0
        #heapq.heapify

        id25=id10(id21, 0)
        id26=[id25]
        while id27(id26)>0:
            id25=id4.id28(id26)
            if id25.id13 in id22:
                continue;
            id22.id29(id25.id13)
            id12.id18[(id21, id25.id13)]=id25.id14
            #self.table[(n.point, start)]=n.cost
            for id30 in id20[id25.id13]:
                if id30[0] not in id22:
                    if id30[0] not in id24:
                        id24[id30[0]]=id25.id14+id30[1]
                        id4.id31(id26, id10(id30[0], id24[id30[0]]))
                    else:
                        if id25.id14+id30[1]<id24[id30[0]]:
                            id24[id30[0]]=id25.id14+id30[1]
                            id4.id31(id26, id10(id30[0], id24[id30[0]]))

class id32:
    def id11(id12, id33, id34):
        id12.id33=id33
        id12.id34=id34
        id12.id35=id23([])
        id12.id36=id1.id37

    def id19(id12, id38, id39):
        if id27(id12.id35)==id27(id12.id33):
            if id38<id12.id36:
                id12.id36=id38
            return

        for id30 in id12.id33:
            if id30 not in id12.id35:
                id12.id35.id29(id30)
                if id39==0:
                    id12.id19(0, id30)
                else:
                    id12.id19(id38+id12.id34[(id39, id30)], id30)
                id12.id35.id40(id30)




def id41():
    if id27(id1.id42)>1:
        id43=id44(id1.id42[1])
    else:
        id43=None
    id45=id6(id43);
    id46=id45().id47().split()
    [id48, id49, id50]=[id51(id46[0]), id51(id46[1]), id51(id46[2])]
    id46=id45()
    id52=id46.id47().split()
    id53=[]
    for id54 in id55(id50):
        id53.id56(id51(id52[id54]))

    id20={}
    for id54 in id55(id49):
        id46=id45().id47().split()
        [id57, id58, id59]=[id51(id46[0]), id51(id46[1]), id51(id46[2])]
        if id57 not in id20:
            id20[id57]=[]
        if id58 not in id20:
            id20[id58]=[]
        id20[id57].id56((id58, id59))
        id20[id58].id56((id57, id59))


    id60=id17()
    for id30 in id53:
        id60.id19(id20, id30)
    #print D.table

    id61=id32(id53, id60.id18)
    id61.id19(0, 0)
    print id61.id36

if id62=="__main__":
    id41()