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
def id15(id11):
    return "".id15(id11)

#memoize macro
def id16(id17):
    id18={}
    def id19(*id20):
        if id20 not in id18:
            id18[(id20)]=id17(*id20)
        return id18[id20]
    return id19

id21=id22([1,0,-1,0],[0,1,0,-1])
id23=1000000007

###########

id24=id7()
id25=[]
id26=[]
for id27 in id28(id24):
    id29,id30=id10()
    if id29<id30:
        id25.id31([id29,id30])
    else:
        id26.id31([id30,id29])
id25.id32()
id26.id32()
id26.id33()

id34=0
id35=0
for id29,id30 in id25:
    id34+=id29
    id35=id36(id35,id34)
    id34-=id30
for id30,id29 in id26:
    id34+=id29
    id35=id36(id35,id34)
    id34-=id30

print id35