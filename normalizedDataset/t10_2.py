from id0 import id1
import id2
import id3
import id4
import id5
id3.id6(10000)
id7=id8("inf")
def id9():
    return id10(id11())
def id12():
    return map(id10,id11().split(" "))
def id13():
    return id11()
def id14():
    return id11().split(" ")
def id15():
    return id16(id11())
def id17(id13):
    return "".id17(id13)
def id18(id19,id20):
    return id5.id21(id19,id20)
def id22(id19,id20):
    return id5.id23(id19,id20)
def id24(id25,id26,id20):
    id27=1
    for id9 in id28(id26):
        id27=id27*(id25-id9)%id20
        id27=id27*id29(id9+1,id20)%id20
    return id27
def id30(id25, id26):
    (id31, id32)=(0, 1)
    (id33, id34)=(1, 0)
    while id26!=0:
        id35=id25//id26
        (id25, id26)=(id26, id25%id26)
        (id31, id32)=(id32-id35*id31, id31)
        (id33, id34)=(id34-id35*id33, id33)
    return (id32, id34, id25)
def id29(id25, id20):
    (id36, id35, id37)=id30(id25, id20)
    return id36%id20
def id38(id25, id31):
    id9=id39(id25, id31)
    if id9!=id40(id25) and id25[id9]==id31:
        return id9
    return-1
def id41(id42):
    id43={}
    def id44(*id45):
        if id45 not in id43:
            id43[(id45)]=id42(*id45)
        return id43[id45]
    return id44
@id41
def id46(id25,id26,id20):
    id26=id47([id25-id26,id26])
    if (id26>id25 or id26<0 or id25<0):
        return 0
    elif id25==0:
        return 1
    return (id46(id25-1,id26-1,id20)+id46(id25-1,id26,id20))%id20
id13=id13()
id19=id40(id13)
id27=id1(id16(id13))
id48=0
for id49,id50 in id27.id51():
    if id50%2==1:
        id48+=1
if id48==0:
    print (id19)
else:
    print (id10(((id19-id48)/2)/id48)*2+1)