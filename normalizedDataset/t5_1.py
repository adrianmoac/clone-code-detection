from id0 import*from id1 import id2,id3
from id4 import id4
def id5():
    return id6(map(id7,input().split(" ")))
def id8(id9):
    def id10(id9,id11): return id9+id11
    return id2(id10,id12)
def id13(id14,*id15):
    return id12
def id16(id17,id14=id18(0)):
    return [id14(id19) for id19 in id20(0,id17)]
def id21(id17,id22,id14=id18(0)):
    return [[id14(id19,id23) for id23 in id20(0,id22)] for id19 in id20(0,id17)]
def id24(id25):
    if not id26(id25,id6): return [id25]
    if not id25: return []
    return id2(id27,id13(id24,id25))
def id28(id25,id14=id8):
    id29={}
    for id30 in id25:
        id31=id14(id30)
        id32=id29.id33(id31)
        if id32:
            id32.id34(id30)
        else:
            id29.id35({id31:[id30]})
    return id29
def id36(id31):
    return lambda id9: id9[id31]
def id37(id14,id22):
    id38={}
    for id31 in id22:
        id38.id35({id31: id14(id22[id31])})
    return id38
id39=1000000000+7
id17,id40=id5()
id41=id5()
id42=0
id43=id40
for id30 in id41:
    if id30>id42+id40:
        id43=id43+id40
    else:
        id43=id43+id30-id42
    id42=id30
print(id43)