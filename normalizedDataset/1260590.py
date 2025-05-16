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
    id32=[]
    for _ in id33(id30):
        id19,id34=id25()
        if id34=="L":
            id32.id35([id18(id19),1])
        else:
            id32.id35([id18(id19),2])

    id36=0
    id37=0
    while id37<id30 and id32[id37][1]==1:
        id36+=id32[id37][0]-id37-1
        id37+=1

    id38=id30-1
    while id38>-1 and id32[id38][1]==2:
        id36+=id31-id32[id38][0]-(id30-1-id38)
        id38-=1

    if id37>id38:
        return id36

    id39=id37
    while id39<=id38:

        id40=id39
        while id32[id39][1]==2:
            id39+=1
        id41=id32[id39-1][0]
        for id42 in id33(id40,id39):
            id36+=(id41-id32[id42][0])-(id39-id42-1)
        id43=id39-id40

        id44=id39
        while id39<id30 and id32[id39][1]==1:
            id39+=1
        id45=id32[id44][0]
        for id42 in id33(id44,id39):
            id36+=(id32[id42][0]-id45)-(id39-id42-1)
        id46=id39-id44

        id36+=id47(id43,id46)*(id32[id44][0]-id32[id44-1][0]-1)

    return id36


print(id29())