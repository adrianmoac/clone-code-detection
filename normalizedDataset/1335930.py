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
    id30,id31=id17()

    def id32(id33):
        if id33<4:
            return 0
        id30=[]
        while id33>0:
            id30.id34(id33%10)
            id33//=10
        id30.id35()
        id36=id37(id30)
        id38=[[[0]*2, [0]*2] for _ in id39(id36)]
        for id40 in id39(id30[0]):
            if id40==4:
                id38[0][1][1]+=1
            else:
                id38[0][1][0]+=1
        if id30[0] in [4,9]:
            id38[0][0][1]=1
        else:
            id38[0][0][0]=1

        for id40 in id39(1,id36):
            id41=id30[id40]
            if id41 in [4,9]:
                id38[id40][0][1]=id38[id40-1][0][0]+id38[id40-1][0][1]
            else:
                id38[id40][0][0]=id38[id40-1][0][0]
                id38[id40][0][1]=id38[id40-1][0][1]

            for id42 in id39(id41):
                if id42==4:
                    id38[id40][1][1]+=id43(id38[id40-1][0])
                else:
                    id38[id40][1][1]+=id38[id40-1][0][1]
                    id38[id40][1][0]+=id38[id40-1][0][0]

            for id42 in id39(10):
                if id42 in [4,9]:
                    id38[id40][1][1]+=id43(id38[id40-1][1])
                else:
                    id38[id40][1][1]+=id38[id40-1][1][1]
                    id38[id40][1][0]+=id38[id40-1][1][0]


        return id38[-1][0][1]+id38[-1][1][1]

    return id32(id31)-id32(id30-1)


print(id29())