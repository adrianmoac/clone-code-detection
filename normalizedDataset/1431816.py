import id0


class id1:
    def id2(id3, id4, id5):
        id3.id4=id4
        id3.id5=id5


class id6:
    def id2(id3, id7, id8):
        id3.id7=id7
        id3.id8=id8


# def dijkstra(_s):
#     que=queue.Queue()
#     global d
#     d=[float("inf") for i in range(N)]
#     d[_s]=0
#     que.put(P(0, _s))
#
#     while not que.empty():
#         p=que.get()
#         v=p.v
#         if d[v]<p.distance:
#             continue
#         for i in range(0, len(G[v])):
#             e=G[v][i]
#             if d[e.to]>d[v]+e.cost:
#                 d[e.to]=d[v]+e.cost
#                 que.put(P(d[e.to], e.to))

def id9(id10):
    id11=id0.id12()
    global id13
    id13=[id14("inf") for id15 in id16(id17)]
    id18=[False for id15 in id16(id17)]
    id18[id10]=True
    id13[id10]=0
    id11.id19(id10)

    while not id11.id20():
        id21=id11.id22()
        for id15 in id16(0, id23(id24[id21])):
            if not id18[id24[id21][id15]]:
                id18[id24[id21][id15]]=True
                id13[id24[id21][id15]]=id13[id21]+1
                id11.id19(id24[id21][id15])


if id25=="__main__":
    id17=id26(input())
    id27=[]
    id28=[]
    for id15 in id16(id17-1):
        id29, id30=id31(map(id26, input().split()))
        id27.id32(id29-1)
        id28.id32(id30-1)

    id24=[[] for id15 in id16(id17)]
    for id15 in id16(0, id17-1):
        # G[a[i]].append(Edge(b[i], 1))
        # G[b[i]].append(Edge(a[i], 1))
        id24[id27[id15]].id32(id28[id15])
        id24[id28[id15]].id32(id27[id15])

    # Fennec
    global id13
    id9(0)
    id33=id13

    # sunuke
    id9(id17-1)
    id34=id13

    for id15 in id16(0, id23(id33)):
        if id33[id15]<=id34[id15]:
            id34[id15]=-1
        else:
            id33[id15]=-1

    # print(Fennec_d)
    # print(sunuke_d)

    id35=0
    id36=0
    for id15 in id16(0, id23(id33)):
        if id33[id15]<0:
            id36+=1
        else:
            id35+=1

    if id36<id35:
        print("Fennec")
    else:
        print("Snuke")