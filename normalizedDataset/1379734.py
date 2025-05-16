# coding: utf-8
import id0, id1, id2, id3, id4, id5, id6, id7, id8, id9, id10, id11
id10.id12(10**7)
id13=10**20
id14=10**9+7


def id15(): return id16(input())
def id17(): return id18(map(id16, input().split()))
def id19(id20): return [id17() for id21 in id22(id20)]
def id23(): return {id24: id25 for id24, id25 in id17()}


def id26():
    id27, id28, id29=id17()
    id30=[]
    for id21 in id22(id29):
        id31, id32, id33, id34=id17()
        id30.id35([(id31, id32), (id33, id34)])
    return id27, id28, id29, id30


# 周上を (0, 0) を原点として反時計回りに 1 本の数直線とした時の point の座標を返す．
# 周上にあるかの判定も行う．
def id36(id27, id28, id37):
    id38, id39=id37
    if id38==0:
        return id27*2+id28+(id28-id39)
    if id38==id27:
        return id27+id39
    if id39==0:
        return id38
    if id39==id28:
        return id27+id28+(id27-id38)


def id40(id27, id28, id29, id30):
    id41=[]
    for id42, id37 in id43(id30):
        id44, id45=id37
        if ((id44[0]==0 or id44[0]==id27) or (id44[1]==0 or id44[1]==id28)) and ((id45[0]==0 or id45[0]==id27) or (id45[1]==0 or id45[1]==id28)):
            id41.id35((id42+1, id36(id27, id28, id44)))
            id41.id35((id42+1, id36(id27, id28, id45)))
    id41.id46(id24=lambda  id38: id38[1])
    id47=[]
    for id37 in id41:
        if id48(id47)==0:
            id47.id35(id37[0])
            continue
        if id37[0]==id47[-1]:
            id47.id49()
        else:
            id47.id35(id37[0])
    
    if id48(id47)==0:
        return "YES"
    else:
        return "NO"
    

def id50():
    id51=id26()
    print(id40(*id51))


if id52=="__main__":
    id50()