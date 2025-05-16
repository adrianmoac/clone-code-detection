import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11

id9.id12(10**7)
id13=10**20
id14=10**9+7

def id15(): return id16(map(id17, input().split()))
def id18(): return id17(input())
def id19(): return input().split()
def id20(): return input()


def id21():
    id22,id23,id24=id15()
    id25=0
    id26=id15()

    id27=id26[0]
    id26.id28()
    id29=id26.id30(id27)
    if id29==id22-1 or id29==0:
        for id31 in id32(id22-1):
            if (id26[id31+1]-id26[id31])*id23<id24:
                id25+=(id26[id31+1]-id26[id31])*id23
            else:
                id25+=id24
        return id25

    if (id26[id29+1]-id26[0])*id23<id24:
        id25+=((id27-id26[0])+(id26[id29+1]-id26[0]))*id23
        for id31 in id32(id29+2,id22):
            if (id26[id31]-id26[id31-1])*id23<id24:
                id25+=(id26[id31]-id26[id31-1])*id23
            else:
                id25+=id24
        return id25
    if (id26[-1]-id26[id29-1])*id23<id24:
        id25+=((id26[-1]-id27)+(id26[-1]-id26[id29-1]))*id23
        for id31 in id32(id29-1):
            if (id26[id31+1]-id26[id31])*id23<id24:
                id25+=(id26[id31+1]-id26[id31])*id23
            else:
                id25+=id24
        return id25

    for id31 in id32(id29+2,id22):
        if (id26[id31]-id26[id31-1])*id23<id24:
            id25+=(id26[id31]-id26[id31-1])*id23
        else:
            id25+=id24
    for id31 in id32(id29-1):
        if (id26[id31+1]-id26[id31])*id23<id24:
            id25+=(id26[id31+1]-id26[id31])*id23
        else:
            id25+=id24
    id25+=id24

    return id25


print(id21())