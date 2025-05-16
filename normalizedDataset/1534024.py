from id0 import id1
import id2 as id3


def id4(id5):
    id6=id7[id5]
    del id7[id5]

    id3.id8(id6)
    id9=0
    while id6:
        id10=id3.id11(id6)
        if id9<id10:
            break
        else:
            id9+=(id9==id10)

    id12=id9+1
    while id6:
        id10=id3.id11(id6)
        if id12<id10:
            break
        else:
            id12+=(id12==id10)

    return (id9, id12)


if id13=="__main__":

    id14=id15(input())
    id16=id17(map(lambda id18: id15(id18)-1, input().split()))
    # D:出している辺の本数
    id19=[0]*id14
    for id20 in id16:
        id19[id20]+=1
    # print(D)
    id7=id1(id17)
    # S:辺を出してないものリスト
    id21=[id20 for id20 in id22(id14) if id19[id20]==0]

    id23=[None]*id14

    while id21:
        # print(child_L)
        id5=id21.id24()

        id6=id7[id5]
        # print(q)
        del id7[id5]

        # listのqをヒープキューに変換
        id3.id8(id6)
        id9=0
        while id6:
            id10=id3.id11(id6)
            if id9<id10:
                break
            else:
                id9+=(id9==id10)

        id23[id5]=id9
        # print(L)
        id25=id16[id5]
        # print("m:"+str(m))
        id7[id25].id26(id9)
        id19[id25]-=1
        if id19[id25]==0:
            id21.id26(id25)

    # print(D)
    # cycle check
    try:
        id27=id19.id28(1)
    except id29:
        print("POSSIBLE")
        id30()

    id31, id32=id4(id27)
    id33=[]
    id5=id16[id27]
    while id5!=id27:
        id33.id26(id4(id5))
        id5=id16[id5]

    # del N, P, D, child_L, S, L

    # 可能な初期値をそれぞれシミュレート
    # 1
    id5=id31
    for id34 in id33:
        if id34[0]==id5:
            id5=id34[1]
        else:
            id5=id34[0]
    if id5!=id31:
        print("POSSIBLE")
        id30()

    # 2
    id5=id32
    for id34 in id33:
        if id34[0]==id5:
            id5=id34[1]
        else:
            id5=id34[0]
    if id5==id31:
        print("POSSIBLE")
        id30()

    print("IMPOSSIBLE")