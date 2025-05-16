import id0 as id1
import id2
import id3
import id4


class id5(id6):

    def id7(id8, id9, id10):
        id8.id11=id4.id12(id13)
        id8.id14=id4.id12(id13)
        id8.id9=id9
        id8.id10=id10
        id8.id15=None
        id8.id16=id17("inf")

    def id18(id8, id11):
        id8.id11[id11[0]][id11[1]]=id11[2]
        id8.id14[id11[1]][id11[0]]=id11[2]

    def id19(id8, id15):
        id8.id15=id1.id20(id15)

    def id21(id8, id22, id9, id23):
        id24=[id8.id16]*id9
        id24[id22]=0
        id25=[[0, id22]]
        while id26(id25):
            id27, id28=id3.id29(id25)
            try:
                for id30 in id23[id28]:
                    id31=id27+id23[id28][id30]
                    if id31<=id24[id30]:
                        id24[id30]=id31
                        id3.id32(id25, [id31, id30])
            except id33:
                pass
        return id1.id20(id24)

    def id34(id8, id22, id9):
        return id8.id21(0, id8.id9, id8.id11)+id8.id21(0, id8.id9, id8.id14)

    def id35(id8, id22, id9):
        id36=id8.id34(id22, id9)
        return id37.id15*(id37.id10-id36)

    def id38(id8, id22, id39, id40=5):
        if id22 in id8.id11 and id39 in id8.id11[id22]:
            return id8.id11[id22][id39]
        id41=id8.id16
        id25=[[0, id22]]
        id42=id8.id16
        while id43(id26(id25)):
            id44=[]
            for _ in id45(id40):
                if id26(id25)==0:
                    break
                id46=id3.id29(id25)
                if id46[0]>=id41:
                    break
                if id46[-1] in id8.id11:
                    for id30 in id8.id11[id46[-1]]:
                        id47=id46[0]+id8.id11[id46[-1]][id30]
                        if id30==id39:
                            if id41>=id47:
                                id42=id47
                                id41=id47
                        else:
                            if id41>=id47 and id30 not in id46[1:]:
                                id44.id48([id47]+id46[1:]+[id30])
            for id49 in id44:
                id3.id32(id25, id49)
        return id42

    def id50(id8, id22, id39, id40=5):
        if id22 in id8.id11 and id39 in id8.id11[id22]:
            return [id22, id39, id8.id11[id22][id39]]
        id42=[]
        id51=[]
        id52=[[id22]]
        id53=[[0]]
        id54=id8.id16
        for _ in id45(id40):
            id55=[]
            id56=[]
            for id57, id58 in id59(id52, id53):
                id47=id58[-1]
                if id57[-1] in id8.id11:
                    for id30 in id8.id11[id57[-1]].id60():
                        id61=id47+id8.id11[id57[-1]][id30]
                        if id54>=id61:
                            id62=id57[:]+[id30]
                            id63=id58[:]+[id61]
                            if id30==id39:
                                id42=id62
                                id51=id63
                                id54=id61
                            elif id26(id62)==id26(id64(id62)):
                                id55.id48(id62)
                                id56.id48(id63)
            id52=id55[:]
            id53=id56[:]
            if id26(id52)==0:
                if id26(id42)==0:
                    return [id22, id8.id16]
                else:
                    id8.id65(id42, id51)
                    return id42+[id51[-1]]
        if id26(id42)==0:
            return [id22, id8.id16]
        else:
            id8.id65(id42, id51)
            return id42+[id51[-1]]

    def id65(id8, id42, id51):
        id66=[]
        for id67, id68 in id2.id69(id45(id26(id42)), 2):
            id66.id48([id42[id67], id42[id68], id51[id68]-id51[id67]])
        id8.id18(id66)

    def id70(id8, id22, id39, id40):
        if id22==id39:
            return id8.id10*id8.id15[id39]
        id71=id8.id16
        id72=id8.id16
        # go=min(self.look_for_minimum_path(start, end, depth=depth)[-1], min_go)
        id73=id74(id8.id38(id22, id39, id40=id40), id71)
        if id73==id8.id16:
            return-1
        id8.id18([id22, id39, id73])
        # back=min(self.look_for_minimum_path(end, start, depth=depth)[-1], min_back)
        id75=id74(id8.id38(id39, id22, id40=id40), id72)
        if id75==id8.id16:
            return-1
        id8.id18([id39, id22, id75])
        id76=id8.id10-id73-id75
        return id76*id8.id15[id39]

id77, id78, id79=map(id80, id81().split())
id37=id5(id77,id79)
id37.id19(map(id80, id81().split()))
for _ in id45(id78):
    id82,id83,id27=map(id80, id81().split())
    id37.id18([id82-1,id83-1,id27])
print(id80(id1.id84(id37.id35(0,id37.id9))))