from id0 import id1


def id2():
    """
    とおり方
    2<=N<=200
    2<=R<=min(8, N)
    より、
    最大でも 2<=R<=8
    8!=40320

    道路
    1<=M<=N*(N-1)/2
    より、
    最大でも 100*199=19900

    調べ方
    rに現れない町を経由する可能性がある
    ある町Aからある町Bまでの最短距離を求める
    ABCの町を訪れるならば、
    A→B→C、
    B→C→A
    C→A→B
    の３パターン（組合せ）がある
    もちろん他の町を経由するかもしれない
        A→(D)→B→(E)→C
    """
    id3, id4, id5=map(id6, input().split())
    id7=map(id6, input().split())

    id8=id9("inf")
    id10=[[id8]*(id3+1) for _ in id11(id3+1)]
    for id12 in id11(1, id3+1):
        id10[id12][id12]=0

    for _ in id11(id4):
        id13, id14, id15=map(id6, input().split())
        id10[id13][id14]=id15
        id10[id14][id13]=id15

    for id16 in id11(1, id3+1):
        for id17 in id11(1, id3+1):
            for id18 in id11(1, id3+1):
                if id10[id17][id18]>id10[id17][id16]+id10[id16][id18]:
                    id10[id17][id18]=id10[id17][id16]+id10[id16][id18]

    id19=id8
    for id20 in id1(id7):
        id21=0
        for id17 in id11(id22(id20)-1):
            id23, id24=id20[id17:id17+2]
            id21+=id10[id23][id24]
        id19=id25(id19, id21)

    print(id19)

if id26=="__main__":
    id2()