class id0:
    def id1(id2, id3, id4, id5):
        id2.id3=id3
        id2.id4=id4
        id2.id5=id5
        # self.n=n


class id6:
    def id1(id2, id7, id8, id9):
        id2.id7=id7
        id2.id8=id8
        id2.id9=id9

    def id10(id2):
        return id11((id2.id7, id2.id8))


# union find。初期化
def id12(id13):
    for id14 in id15(0, id13):
        id16[id14]=id14
        id17[id14]=0


# 木の根を求める
def id18(id19):
    if id16[id19]==id19:
        return id19
    else:
        id16[id19]=id18(id16[id19])
        return id16[id19]


# 集合を併合
def id20(id19, id21):
    id19=id18(id19)
    id21=id18(id21)
    if id19==id21:
        return

    if id17[id19]<id17[id21]:
        id16[id19]=id21
    else:
        id16[id21]=id19
        if id17[id19]==id17[id21]:
            id17[id19]+=1


# 同じ集合かどうか
def id22(id19, id21):
    return id18(id19)==id18(id21)


def id23(id24, id25):
    return id24.id5<id25.id5


def id26():
    id27=id28(id29, id30=lambda id31: id31.id5)
    id12(id32)
    id33=0
    # for i in range(E):
    # # print("u"+str(sorted_edges[i].u)+"v"+str(sorted_edges[i].v)+"cost"+str(sorted_edges[i].cost))

    for id14 in id15(0, id34):
        id35=id27[id14]
        if not id22(id35.id3, id35.id4):
            id20(id35.id3, id35.id4)
            # print("tmp_edge.cost"+str(tmp_edge.cost))
            id33+=id35.id5

    return id33


if id36=="__main__":
    id37=id38(input())
    id7=[]
    id8=[]
    id39=[]
    for id14 in id15(0, id37):
        id40, id41=id42(map(id38, input().split()))
        # x.append(tmp_x)
        # y.append(tmp_y)
        id39.id43(id6(id40, id41, id14))

    id44=id28(id39, id30=lambda id45: id45.id7)
    id46=id28(id39, id30=lambda id45: id45.id8)

    id29=[]
    for id14 in id15(0, id37-1):
        id47=id48(id49(id44[id14].id7-id44[id14+1].id7), id49(id44[id14].id8-id44[id14+1].id8))
        id29.id43(id0(id44[id14].id9, id44[id14+1].id9, id47))
        # Edges.append(Edge(sorted_by_x[i+1].n, sorted_by_x[i].n, cost_x))
        id50=id48(id49(id46[id14].id7-id46[id14+1].id7), id49(id46[id14].id8-id46[id14+1].id8))
        id29.id43(id0(id46[id14].id9, id46[id14+1].id9, id50))
        # Edges.append(Edge(sorted_by_y[i+1].n, sorted_by_y[i].n, cost_y))

    id16=[0 for id14 in id15(id37)]
    id17=[0 for id14 in id15(id37)]
    id32=id37
    id34=2*(id37-1)

    print(id26())