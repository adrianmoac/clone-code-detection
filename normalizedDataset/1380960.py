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
    id32=None
    id33=None
    id34=[]
    for id35 in id36(id30):
        id37=[_ for _ in id28()]
        if "s" in id37:
            id32=(id35, id37.id38("s"))

        if "g" in id37:
            id33=(id35, id37.id38("g"))
        id34.id39([1 if _=="#" else 0 for _ in id37])

    id19=[1,-1,0,0]
    id40=[0,0,1,-1]

    def id41(id32,id33):
        id42=id5.id43(lambda: id15)
        id42[id32]=0
        id44=[]
        id4.id45(id44, (0, id32))
        id46=id5.id43(id47)
        while id48(id44):
            id49, id50=id4.id51(id44)
            if id46[id50]:
                continue
            id46[id50]=True
            if id50==id33:
                return id49

            for id52 in id36(4):
                id53=id50[0]+id19[id52]
                id54=id50[1]+id40[id52]
                if id53<0 or id53>=id30 or id54<0 or id54>=id31:
                    continue
                id55=(id53,id54)
                if id46[id55]:
                    continue
                id56=id49+id34[id53][id54]
                if id42[id55]>id56:
                    id42[id55]=id56
                    id4.id45(id44, (id56, id55))

        return 3
    if id41(id32,id33)<=2:
        return "YES"

    return "NO"


print(id29())





