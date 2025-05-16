import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13

id9.id14(10**7)
id15=10**20
id16=10**9+7

def id17(): return [id18(id19) for id19 in id9.id20.id21().split()]
def id22(): return [id18(id19)-1 for id19 in id9.id20.id21().split()]
def id23(): return [id24(id19) for id19 in id9.id20.id21().split()]
def id25(): return id9.id20.id21().split()
def id26(): return id18(id9.id20.id21())
def id27(): return id24(id9.id20.id21())
def id28(): return input()


def id29():
    id30=[[id31 for id31 in id28()] for _ in id32(19)]
    id33=id5.id34(id18)
    for id35 in id30:
        for id31 in id35:
            id33[id31]+=1
    if id33["o"]-id33["x"]>1 or id33["o"]-id33["x"]<0:
        return "NO"
    def id36(id30):
        # yoko
        id37=[[False]*19 for _ in id32(19)]
        for id38 in id32(19):
            id35=id30[id38]
            for id39 in id32(19):
                if id37[id38][id39] or id35[id39]==".":
                    continue
                id40=id35[id39]
                id41=1
                for id42 in id32(id39+1,19):
                    if id35[id42]!=id40:
                        break
                    id37[id38][id42]=True
                    id41+=1
                if id41>4:
                    return
        # tate
        id37=[[False]*19 for _ in id32(19)]
        for id38 in id32(19):
            for id39 in id32(19):
                if id37[id38][id39] or id30[id39][id38]==".":
                    continue
                id40=id30[id39][id38]
                id41=1
                for id42 in id32(id39+1,19):
                    if id30[id42][id38]!=id40:
                        break
                    id37[id38][id42]=True
                    id41+=1
                if id41>4:
                    return False
        # naname1
        id37=[[False]*19 for _ in id32(19)]
        for id38 in id32(19):
            for id39 in id32(19):
                if id37[id38][id39] or id30[id38][id39]==".":
                    continue
                id40=id30[id38][id39]
                id41=1
                for id42 in id32(id39+1,19):
                    if id38+id41>18 or id30[id38+id41][id42]!=id40:
                        break
                    id37[id38+id41][id42]=True
                    id41+=1
                if id41>4:
                    return
        # naname2
        id37=[[False]*19 for _ in id32(19)]
        for id38 in id32(18,-1,-1):
            for id39 in id32(19):
                if id37[id38][id39] or id30[id38][id39]==".":
                    continue
                id40=id30[id38][id39]
                id41=1
                for id42 in id32(id39+1,19):
                    if id38-id41<0 or id30[id38-id41][id42]!=id40:
                        break
                    id37[id38-id41][id42]=True
                    id41+=1
                if id41>4:
                    return

        return True

    if id33["o"]-id33["x"]==1:
        for id38 in id32(19):
            for id39 in id32(19):
                if id30[id38][id39]!="o":
                    continue
                id30[id38][id39]="."
                if id36(id30)==True:
                    return "YES"
                id30[id38][id39]="o"
    else:
        if id33["x"]==0:
            return "YES"
        for id38 in id32(19):
            for id39 in id32(19):
                if id30[id38][id39]!="x":
                    continue
                id30[id38][id39]="."
                if id36(id30)==True:
                    return "YES"
                id30[id38][id39]="x"
    return "NO"




print(id29())





