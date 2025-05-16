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
    id7=id0.id37(id23, id29)
    if id7!=id38(id23) and id23[id7]==id29:
        return id7
    else:
        return-1

###########


id17,id39=id10()
id40=map(id8,id9().split(" "))

while 1:
    id41=1
    for id23 in id14(id42(id17)):
        if id36(id40,id8(id23))!=-1:
            id41=0
    if id41:
        print id17
        break
    id17+=1