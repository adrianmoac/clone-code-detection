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
    id23,id24=id29(id23,id24),id30(id23,id24)
    if id23%id24==0:
        return id24
    else:
        return id28(id24,id23%id24)
 
def id27(id23, id18):
    (id31, id32, id33)=id28(id23, id18)
    return id31%id18

#bisect macro
def id34(id23, id35):
    #Locate the leftmost value exactly equal to x
    id7=id36(id23, id35)
    if id7!=id37(id23) and id23[id7]==id35:
        return id7
    return-1

#memoize macro
def id38(id39):
    id40={}
    def id41(*id42):
        if id42 not in id40:
            id40[(id42)]=id39(*id42)
        return id40[id42]
    return id41

@id38
def id43(id23,id24,id18):
    id24=id30([id23-id24,id24])
    if (id24>id23 or id24<0 or id23<0):
        return 0
    elif id23==0:
        return 1
    return (id43(id23-1,id24-1,id18)+id43(id23-1,id24,id18))%id18

###########

id23,id24,id18=id10()
id25=id28(id23,id24)
id44=id18

@id38
def id45(id35):
    if id35==1:
        return 10%id44
    elif id35%2==0:
        return id45(id35/2)**2%id44
    else:
        return id45(id35/2)**2*10%id44

@id38
def id46(id35):
    if id35==1:
        return 1
    elif id35%2==0:
        return (id45(id35/2)*id46(id35/2)+id46(id35/2))%id44
    else:
        return (id45(id35/2+1)*id46(id35/2)+id46(id35/2+1))%id44

@id38
def id47(id35):
    if id35==1:
        return 1
    elif id35%2==0:
        return (id47(id35/2)*id45(id35*id25/2)+id47(id35/2))%id44
    else:
        return (id47(id35/2)*id45((id35+1)*id25/2)+id47((id35+1)/2))%id44

print id47(id23/id25)*id46(id24)%id44