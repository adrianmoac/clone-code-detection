import id0 as id1
import id2

def id3():
    try:
        id4
        import id5
        import id6

        id7=[]
        id8=id6.id9.id10(id6.id9.id11(id12), "data.dat")
        with id5.id13(id8, "r", "utf-8") as id14:
            id15=id16(id14.id17())
            for id18 in id19(id15):
                id7.id20(id14.id17().id21("\r\n"))

    except id22:
        id7=[]
        id15=id16(input())
        for id18 in id19(id15):
            id7.id20(input())
    return id7

id23=id3()
id24=[]
for id25 in id23:
    id24.id20(id25.split())
id26=id1.id27(id24, id28="int64")
id29=id26.id30[0]


def id31():

    id32=False
    for id33 in id19(0, id29):
        for id18 in id19(0, id29):
            if(id33==id18): continue
            for id34 in id19(0, id29):
                if((id18==id34) or (id34==id33)): continue
                if(id26[id18][id33]+id26[id33][id34]<id26[id18][id34]):
                    id35=True
                if(id26[id18][id33]+id26[id33][id34]==id26[id18][id34]):
                    id36[id18][id34]=1
                    id36[id34][id18]=1

    try:
        id4
        print(id36)
    except id22:
        pass

    if(id32):
        print(-1)
    else:
        id37=0
        for id18 in id19(0, id29):
            for id34 in id19(id18, id29):
                if(id36[id18][id34]==0):
                    id37+=id26[id18][id34]
        print(id37)

def id38():

    import id39.id40.id41 as id42

    id43=[10000000000]*id29  # should be>2*10**9
    id44=id1.id45(id43)
    id46=id26.id47()
    id46+=id44
    id37=0
    id48=0
    for id18 in id19(id29-1):
        for id34 in id19(id18+1, id29):
            id49=id1.id50(id46[id18]+id46[id34])
            if id49>id46[id18,id34]:
                id37+=id46[id18,id34]
                # print(i, j)
            elif id49<id46[id18,id34]:
                print(-1)
                id51()

    print(id37)

def id52():
    import id0 as id1

    for id18 in id19(id29):
        id26[id18][id18]=10000000000

    id53=0
    for id18 in id19(id29-1):
        for id34, id54 in id55(id26[id18][id18+1:], id56=id18+1):
            id57=id1.id50(id26[id18]+id26[id34])
            # print(A[i][i+1:])
            # print (i, j, d1, d2)
            if id54>=id57:
                if id54>id57:
                    print(-1)
                    id51()
            else:
                id53+=id54
    print(id53)

id38()