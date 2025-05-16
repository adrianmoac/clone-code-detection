class id0(id1):
    def id2(id3, id4):
        id3.id5=id6(id7(id4))
        id3.id8=[0]*id4
        id3.id9=id4  # number of disjoint sets

    def id10(id3, id11, id12):
        id3.id13(id3.id14(id11), id3.id14(id12))

    def id13(id3, id11, id12):
        if id11==id12:
            return
        id3.id9-=1
        if id3.id8[id11]>id3.id8[id12]:
            id3.id5[id12]=id11
        else:
            id3.id5[id11]=id12
            if id3.id8[id11]==id3.id8[id12]:
                id3.id8[id12]+=1

    def id14(id3, id11):
        id15=id3.id5[id11]
        if id15!=id11:
            id3.id5[id11]=id3.id14(id15)
        return id3.id5[id11]

def id16():
    id17=id18(input())
    id19=[]
    id20=[]
    for id21 in id7(id17):
        id11, id12=map(id18, input().split())
        id19.id22((id11, id21))
        id20.id22((id12, id21))
    return id17, id19, id20

def id23(id19):
    id24=[]
    id25, id26=id19[0]
    for id11, id21 in id19[1:]:
        id24.id22((id11-id25, id26, id21))
        id25=id11
        id26=id21
    return id24

def id27(id17, id19, id20):
    id19.id28()
    id20.id28()
    id24=id23(id19)
    id24.id29(id23(id20))
    id24.id28()
    id30=id0(id17)
    id31=0
    for id32, id21, id33 in id24:
        if id30.id14(id21)==id30.id14(id33):
            continue
        id30.id10(id21, id33)
        id31+=id32
    return id31

id17, id19, id20=id16()
print(id27(id17, id19, id20))