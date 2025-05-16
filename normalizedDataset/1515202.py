import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13

id9.id14(10**7)
id15=10**20
id16=1.0/10**9
id17=10**9+7

def id18(): return [id19(id20) for id20 in id9.id21.id22().split()]
def id23(): return [id19(id20)-1 for id20 in id9.id21.id22().split()]
def id24(): return [id25(id20) for id20 in id9.id21.id22().split()]
def id26(): return id9.id21.id22().split()
def id27(): return id19(id9.id21.id22())
def id28(): return id25(id9.id21.id22())
def id29(): return input()


def id30():
    id31=[[id32=="Q" for id32 in id29()] for _ in id33(8)]
    id34=[0]*8
    id35=[0]*8
    id36=[0]*15
    id37=[0]*15

    for id38 in id33(8):
        for id39 in id33(8):
            if not id31[id38][id39]:
                continue
            id34[id39]+=1
            id35[id38]+=1
            id36[id38+id39]+=1
            id37[id38-id39+7]+=1

    if id40(id40(id34),id40(id35),id40(id36),id40(id37))>1:
        return "No Answer"

    def id41(id38):
        if id38==8:
            return True

        if id35[id38]>0:
            return id41(id38+1)

        for id39 in id33(8):
            if id34[id39]+id36[id38+id39]+id37[id38-id39+7]>0:
                continue
            id34[id39]=id36[id38+id39]=id37[id38-id39+7]=1
            if id41(id38+1):
                id31[id38][id39]=True
                return True
            id34[id39]=id36[id38+id39]=id37[id38-id39+7]=0

    id42=id41(0)
    if id42:
        return "\n".id43(["".id43(["Q" if id32 else "." for id32 in id34]) for id34 in id31])

    return "No Answer"



print(id30())
