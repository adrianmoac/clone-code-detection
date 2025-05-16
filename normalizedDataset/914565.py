import id0
import id1
import id2
import id3
import id4
id1.id5(10000)

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
    return id3.id20(id18,id19)
def id21(id18,id19):
    return id3.id22(id18,id19)

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

id47=id48([1,0,-1,0],[0,1,0,-1])

###########

id18,id19,id49=id11()
id50=id11()

id51=[[] for id52 in id53(id18)]
id54=[(id6,id52) for id52 in id53(id18)]
id54[0]=(0,0)
id55=[id6]*id18
id56=[False]*id18

id57=[[] for id52 in id53(id18)]
id58=[(id6,id52) for id52 in id53(id18)]
id58[0]=(0,0)
id59=[id6]*id18
id60=[False]*id18

id4.id61(id54)
id4.id61(id58)

#input
for id52 in id53(id19):
    id24,id25,id26=id11()
    id51[id24-1].id62((id25-1,id26))
    id57[id25-1].id62((id24-1,id26))


while(id39(id54)!=0):
    id63,id64=id4.id65(id54)
    if not id56[id64]:
        id56[id64]=True
        id55[id64]=id63
        for id25,id26 in id51[id64]:
            if not id56[id25]:
                id4.id66(id54,(id63+id26,id25))

while(id39(id58)!=0):
    id63,id64=id4.id65(id58)
    if not id60[id64]:
        id60[id64]=True
        id59[id64]=id63
        for id25,id26 in id57[id64]:
            if not id60[id25]:
                id4.id66(id58,(id63+id26,id25))

id67=0
for id52 in id53(id18):
    id68=(id49-id55[id52]-id59[id52])*id50[id52]
    if id67<id68:
        id67=id68

print id67