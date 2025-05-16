import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11,id12,id13

id9.id14(10**7)
id15=10**20
id16=1.0/10**10
id17=10**9+7

def id18(): return [id19(id20) for id20 in id9.id21.id22().split()]
def id23(): return [id19(id20)-1 for id20 in id9.id21.id22().split()]
def id24(): return [id25(id20) for id20 in id9.id21.id22().split()]
def id26(): return id9.id21.id22().split()
def id27(): return id19(id9.id21.id22())
def id28(): return id25(id9.id21.id22())
def id29(): return input()


def id30():
    id20=id27()
    id31=id27()
    id32=id18()
    id33=id27()
    id34=[id18() for _ in id35(id33)]
    id36=[[0,0,0,id20,0,0]]
    id37=0
    for id38 in id35(id31):
        id39=id36[-1][:]
        id40=id32[id38]-id37
        id37=id32[id38]
        if id38%2==0:
            id39[1]-=id40
            id39[3]-=id40
            id39[4]-=id40
            if id39[0]>id39[1]:
                id39[0]=id39[1]
        else:
            id39[1]+=id40
            id39[3]+=id40
            id39[4]+=id40
            if id39[2]<id39[1]:
                id39[2]=id39[1]
        if id39[3]>id20:
            id39[3]=id20
        if id39[3]<0:
            id39[3]=0
        if id39[4]>id20:
            id39[4]=id20
        if id39[4]<0:
            id39[4]=0

        id39[5]=id32[id38]

        id36.id41(id39)
    def id42(id38):
        id43=id31
        id44=0
        id45=0
        while id43>id44 and (id43+id44)//2!=id45:
            id45=(id43+id44)//2
            if id36[id45][5]<id38:
                id44=id45
            else:
                id43=id45-1
        if id36[id45][5]>id38:
            return id45-1
        if id45==id31:
            return id31
        if id36[id45+1][5]<=id38:
            return id45+1
        return id45

    #print(a)
    id40=[]
    for id39,id37 in id34:
        id46=id42(id39)
        id47=id36[id46]
        id48=id20-id37
        #print(c,d,e,ti,ai)
        if id37+id47[0]<=0:
            id49=id47[4]
        elif id48-id47[2]<=0:
            id49=id47[3]
        else:
            id49=id37+id47[1]
        #print('tt',tt)
        if id46%2==0:
            id49-=id39-id47[5]
        else:
            id49+=id39-id47[5]
        #print('tt2',tt)
        if id49<0:
            id49=0
        elif id49>id20:
            id49=id20
        id40.id41(id49)

    return "\n".id50(map(id51,id40))


print(id30())
