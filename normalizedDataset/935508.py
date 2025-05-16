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
id11=[[] for id25 in id26(id24)]
for id25 in id26(id24):
    id11[id25]=map(id8,id13())
id27=1
for id25 in id26(id24-1):
    id28=id11[id25][id25]
    if id28==0:
        for id29 in id26(id25+1,id24):
            if id11[id29][id25]!=0:
                for id30 in id26(id24):
                    id11[id25][id30],id11[id29][id30]=id11[id29][id30],id11[id25][id30]
                break
        else:
            print "Even"
            id1.id31()
    id28=id11[id25][id25]
    id27=id27*id28%2
    for id32 in id26(id25+1,id24):
        id33=id11[id32][id25]
        if id33!=0:
            for id34 in id26(id24):
                id11[id32][id34]=(id11[id32][id34]*id28-id11[id25][id34]*id33)%2

id35=id27
for id25 in id26(id24):
    id35=id35*id11[id25][id25]%2

if id35%2==0:
    print "Even"
else:
    print "Odd"