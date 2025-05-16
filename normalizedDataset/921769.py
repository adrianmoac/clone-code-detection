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

id49,id50,id18=id11()
id51=[(0,0) for id52 in id53(id18)]
for id52 in id53(id18):
    id51[id52]=id11()
id54=[0]*10
id55=[]

for id30,id32 in id51:
    for id56,id57 in id3.id58((-1,0,1),(-1,0,1)):
        if 2<=id30+id56<=id49-1 and 2<=id32+id57<=id50-1:
            id55.id59((id30+id56)*id50+(id32+id57))

id60=id4.id61(id55)
for id62,id63 in id60.id64():
    id54[id63]+=1

id54[0]=(id49-2)*(id50-2)-id65(id54)

for id52 in id53(10):
    print id54[id52]