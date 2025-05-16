import id0
import id1
import id2
import id3
id1.id4(10000)

id5=id6("inf")

# input macro
def id7():
    return id8(id9())
def id10():
    return map(id8,id9().split(" "))
def id11():
    return id9()
def id12():
    return id9().split(" ")
def id13():
    return id14(id9())
#

def id15(id11):
    return "".id15(id11)

#iterate macro
def id16(id17,id18):
    return id3.id19(id17,id18)
def id20(id17,id18):
    return id3.id21(id17,id18)

#modulo macro
def id22(id23,id24,id18):
    id25=1
    for id7 in id26(id24):
        id25=id25*(id23-id7)%id18
        id25=id25*id27(id7+1,id18)%id18
    return id25
 
def id28(id23, id24):
    (id29, id30)=(0, 1)
    (id31, id32)=(1, 0)
    while id24!=0:
        id33=id23//id24
        (id23, id24)=(id24, id23%id24)
        (id29, id30)=(id30-id33*id29, id29)
        (id31, id32)=(id32-id33*id31, id31)
    return (id30, id32, id23)
 
def id27(id23, id18):
    (id34, id33, id35)=id28(id23, id18)
    return id34%id18

#bisect macro
def id36(id23, id29):
    #Locate the leftmost value exactly equal to x
    id7=id37(id23, id29)
    if id7!=id38(id23) and id23[id7]==id29:
        return id7
    return-1

#memoize macro
def id39(id40):
    id41={}
    def id42(*id43):
        if id43 not in id41:
            id41[(id43)]=id40(*id43)
        return id41[id43]
    return id42

@id39
def id44(id23,id24,id18):
    id24=id45([id23-id24,id24])
    if (id24>id23 or id24<0 or id23<0):
        return 0
    elif id23==0:
        return 1
    return (id44(id23-1,id24-1,id18)+id44(id23-1,id24,id18))%id18

id46=id47([1,0,-1,0],[0,1,0,-1])

###########

id48,id29,id31,id11,id49=id10()

if id29>=id31:
    if id11<=id49:
        print 1.*(id49-id11)/(id29+id31)
    else:
        print 1.*(id48+id49-id11)/(id29+id31)
else:
    if id11<=id49:
        id50=1.*(id49-id11)/(id29+id31)
        id51=1.*(id48+id11-id49)/(id31-id29)
    else:
        id50=1.*(id11-id49)/(id31-id29)
        id51=1.*(id48+id49-id11)/(id29+id31)
    print id45(id50,id51)