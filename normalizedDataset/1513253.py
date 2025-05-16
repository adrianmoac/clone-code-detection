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

def id30(id31):
    id32=id19(id0.id33(id31)+1)
    id34=id5.id35(id19)
    while id31%2==0:
        id31//=2
        id34[2]+=1
    id36=3
    while id31>1 and id32>=id36:
        if id31%id36==0:
            id31//=id36
            id34[id36]+=1
        else:
            id36+=2

    if id31>1:
        id34[id31]+=1

    id37=[1]
    for id38, id39 in id34.id40():
        for id41 in id37[:]:
            for id36 in id42(1,id39+1):
                id37.id43(id41*(id38**id36))

    return id44(id37)

def id45():
    id31,id38=id18()
    id37=0

    id46=id30(id38)[::-1]
    id47=id5.id35(id19)
    for id48 in id42(id49(id46)):
        id34=id46[id48]
        id50=id31//id34
        id51=(id34*(id50+1))*id50//2
        for id52 in id42(id48):
            id53=id46[id52]
            if id53%id34==0:
                id51-=id47[id53]
        id47[id34]=id51%id17
        id37+=id51*id38//id3.id54(id38,id34)%id17
        id37%=id17

    return id37



print(id45())
