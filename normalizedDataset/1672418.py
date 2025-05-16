import id0 as id1
import id2
import id3

def id4():
    try:
        id5
        import id6
        import id7

        id8=[]
        id9=id7.id10.id11(id7.id10.id12(id13), "data073.dat")
        with id6.id14(id9, "r", "utf-8") as id15:
            id8.id16(id15.id17().id18("\r\n"))
            id19, id20, id21=id22(map(id23, id8[0].split()))
            for id24 in id25(id20+1):
                id8.id16(id15.id17().id18("\r\n"))


    except id26:
        id8=[]
        id8.id16(input())
        id19, id20, id21=id22(map(id23, id8[0].split()))
        for id24 in id25(id20+1):
            id8.id16(input())

    return id8

def id27(id28, id29):
    id30=0
    for id24 in id25(id31(id29)-1):
        id30+=id28[id29[id24]][id29[id24+1]]
    return id30


def id32():

    id33=id4()
    id19, id20, id21=id22(map(id23, id33[0].split()))
    id29=id22(map(id23, id33[1].split()))
    id34=id35([])

    id36=200000
    # D=np.zeros((N+1, N+1), dtype='int32')
    # D+=MAX
    id28=[[id37("inf")]*(id19+1) for _ in id25(id19+1)]


    for id24 in id25(2, id20+2):
        id38, id39, id40=id22(map(id23, id33[id24].split()))
        id28[id38][id39]=id40
        id28[id39][id38]=id40

    # for i in range(1, N+1):
    #     for j in range(1, N+1):
    #         dis_two_node=np.min(D[i]+D[j])
    #         if dis_two_node<D[i,j]:
    #             D[i,j]=dis_two_node
    #             D[j,i]=dis_two_node

    # for i in range(N+1):
    #     D[i][i]=0

    for id41 in id25(1, id19+1):
        for id24 in id25(1, id19+1):
            for id42 in id25(1, id19+1):
                id43=id28[id24][id41]+id28[id41][id42]
                if id43<id28[id24][id42]:
                    id28[id24][id42]=id43
                    id28[id42][id24]=id43

   
    id44=id37("inf")
    for id45 in id3.id46(id29):
        id44=id47(id27(id28, id45), id44)

    print(id44)




id32()