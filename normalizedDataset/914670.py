import id0
import id1
import id2
import id3
import id4
id2.id5(10000)

id6=id7("inf")

# input macro
def id8():
    return id9(id10())
def id11():
    return map(id9,id10().split(" "))
def id12():
    return id10()
def id13():
    return id10().split(" ")
def id14():
    return id15(id10())
#

def id16(id12):
    return "".id16(id12)

#iterate macro
def id17(id18,id19):
    return id4.id20(id18,id19)
def id21(id18,id19):
    return id4.id22(id18,id19)

#modulo macro
def id23(id24,id25,id19):
    id26=1
    for id8 in id27(id25):
        id26=id26*(id24-id8)%id19
        id26=id26*id28(id8+1,id19)%id19
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
    id8=id38(id24, id30)
    if id8!=id39(id24) and id24[id8]==id30:
        return id8
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

###########
id47=1000000007
id48,id49,id50=id11()
id24=id11()
id51=[0]*id48
id24.id52()
id0.id53(id24)

def id54(id30):
    if id30==0:
        return 1
    elif id30==1:
        return id49
    elif id30%2==0:
        return id54(id30/2)**2%id47
    else:
        return id54(id30/2)**2*id49%id47

if id49==1:
    for id55 in id56(id48):
        print id24[id55]
else:
    while(id50>0 and id46(id24)*id49<=id57(id24)):
        id30=id0.id58(id24)
        id0.id59(id24,id30*id49)
        id50-=1

    id24.id52()
    for id55 in id56(id48-id50%id48):
        id51[id55]=id24[id55+id50%id48]*id54(id9(id50/id48))%id47
    for id55 in id56(id50%id48):
        id51[id48-id50%id48+id55]=id24[id55]*id54(id9(id50/id48)+1)%id47
    for id55 in id56(id48):
        print id51[id55]
        