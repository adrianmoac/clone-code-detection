from id0 import*from id1 import id2,id3
from id4 import id4
from id5 import id5
def id6():
    return id7(map(id8,input().split(" ")))
def id9(id10):
    def id11(id10,id12): return id10+id12
    return id2(id11,id13)
def id14(id15,*id16):
    return id13
def id17(id18,id15=id19(0)):
    return [id15(id20) for id20 in id21(0,id18)]
def id22(id18,id23,id15=id19(0)):
    return [[id15(id20,id24) for id24 in id21(0,id23)] for id20 in id21(0,id18)]
def id25(id26):
    if not id27(id26,id7): return [id26]
    if not id26: return []
    return id2(id28,id14(id25,id26))
def id29(id26,id15=id9):
    id30={}
    for id31 in id26:
        id32=id15(id31)
        id33=id30.id34(id32)
        if id33:
            id33.id35(id31)
        else:
            id30.id36({id32:[id31]})
    return id30
def id37(id32):
    return lambda id10: id10[id32]
def id38(id15,id23):
    id39={}
    for id32 in id23:
        id39.id36({id32: id15(id23[id32])})
    return id39
id40=1000000000+7
id18,id41=id6()
id15=[id17(303) for id20 in id21(0,id18+1)]
id42=-1
id15[0]=id17(303,id19(-1000))
id15[0][0]=0
for id20 in id21(0,id18):
    id43=[id44 [:] for id44 in id15]
    id45,id46=id6()
    if id42<0 : id42=id45
    id45-=id42
    for id47 in id21(0,id20+1):
        for id48 in id21(0,303-id45):
            id15[id47+1][id48+id45]=id49(
                id15[id47+1][id48+id45],
                id43[id47][id48]+id46)
id50=0
for id47 in id21(0,id18+1):
    for id48 in id21(0,303):
        if id48+id47*id42<=id41:
            id50=id49(id50,id15[id47][id48])
print(id50)