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
    return map(id8,id12(id9()))
def id13():
    return id9()
def id14():
    return id9().split(" ")
def id15():
    return id12(id9())
#

def id16(id13):
    return "".id16(id13)

#iterate macro
def id17(id18,id19):
    return id3.id20(id18,id19)
def id21(id18,id19):
    return id3.id22(id18,id19)

#modulo macro
def id23(id24,id25,id19):
    id26=1
    for id7 in id27(id25):
        id26=id26*(id24-id7)%id19
        id26=id26*id28(id7+1,id19)%id19
    return id26
 
def id29(id24, id25):
    (id30, id31)=(0, 1)
    (id32, id33)=(1, 0)
    while id25!=0:
        id34=id24//id25
        (id24, id25)=(id25, id24%id25)
        (id30, id31)=(id31-id34*id30, id30)
        (id32, id33)=(id33-id34*id32, id32)
    return (id31, id33, id24)
 
def id28(id24, id19):
    (id35, id34, id36)=id29(id24, id19)
    return id35%id19

#bisect macro
def id37(id24, id30):
    #Locate the leftmost value exactly equal to x
    id7=id38(id24, id30)
    if id7!=id39(id24) and id24[id7]==id30:
        return id7
    return-1

#memoize macro
def id40(id41):
    id42={}
    def id43(*id44):
        if id44 not in id42:
            id42[(id44)]=id41(*id44)
        return id42[id44]
    return id43

@id40
def id45(id24,id25,id19):
    id25=id46([id24-id25,id25])
    if (id25>id24 or id25<0 or id24<0):
        return 0
    elif id24==0:
        return 1
    return (id45(id24-1,id25-1,id19)+id45(id24-1,id25,id19))%id19

id47=id48([1,0,-1,0],[0,1,0,-1])

###########

id49=id11()
id18=id39(id49)
id50=0
for id51 in id52(id18+1):
    for id53 in id52(id51+1,id18+1):
        id54=id8(id16(map(id55,id49[id51:id53])))
        if id51==0 and id53==id18:
            id50+=id54
        elif id51!=0 and id53==id18:
            id50+=id54*(2**(id51-1))
        elif id51==0 and id53!=id18:
            id50+=id54*(2**(id18-id53-1))
        else:
            id50+=id54*(2**(id51+id18-id53-2))

print id50