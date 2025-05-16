#!/usr/bin/python

import id0
import id1
import id2

def id3(id4):
    id5, id6, id7, id8, id9=id4.id10()
    id11=id12((id9-id8)%id5)/(id6+id7)
    if id7>id6:
        id11=id13(id11, id12((id8-id9)%id5)/(id7-id6))

    return id11

class id14(id15):
    def id16(id17, id18=None):
        id17.id19=id18 is not None
        id17.id20=1
        id17.id21=[]
        if id17.id19:
            with id22(id18) as id4:
                id23=False
                for id24 in id4:
                    id24=id24.id25()
                    if id24:
                        id17.id21.id26(id24)
                        id23=False
                    else:
                        if not id23: id17.id20+=1
                        id23=True

    def id27(id17):
        return id17.id21.id28(0) if id17.id19 else id29()

    def id30(id17):
        return id31(id17.id27())
    def id32(id17):
        return id12(id17.id27())
    def id33(id17):
        return id34(id17.id27())
    def id35(id17):
        return id17.id27()

    def id10(id17):
        return [id31(id36) for id36 in id17.id27().split()]
    def id37(id17):
        return [id12(id36) for id36 in id17.id27().split()]
    def id38(id17):
        return [id34(id36) for id36 in id17.id27().split()]
    def id39(id17):
        return id17.id27().split()

if id40=="__main__":
    id18=id1.id41[1] if id42(id1.id41)>1 else None
    id4=id14(id18)
    if id4.id19:
        for id43 in id44(id4.id20):
            print "Case #%d"%(id43+1)
            print id3(id4)
    else:
        print id3(id4)