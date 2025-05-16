def id0(id1, id2, id3, id4):
    from id5 import id6

    id7=[[-1]*id1 for _ in id8(id1)]

    def id9(id10, id11):
        # 原点と(x,y)から作れる長方形内でのおいしさの和
        if id10<0 or id11<0:
            return 0
        if id7[id10][id11]==-1:
            # ex.(x,y)=(2,3)
            # 全体     領域1 領域2 領域3 領域4
            #***--++---###--xx--------#***--++---###--xx--------#***--<=++---###--xx--------#***--++---------------o--#-------------------------# 原点から伸びる*の領域について計算するなら、領域1+2-3+4とすればよい。
            id12=0
            id12+=id9(id10-1, id11)  # 領域1
            id12+=id9(id10, id11-1)  # 領域2
            id12-=id9(id10-1, id11-1)  # 領域3
            id12+=id2[id10][id11]  # 領域4
            id7[id10][id11]=id12
        return id7[id10][id11]

    def id13(id10, id11, id14, id15):
        #(x,y),(w,h)が定める長方形内でのおいしさの和
        id12=0
        # ex.(x,y,w,h)=(1,1,3,3)
        # 全体     領域1 領域2 領域3 領域4
        #-----++++-####-x----o----#-***-++++------x---------#-***-<=++++------x---------#-***-++++------x---------#-------------------------s+=rectangleFromOrigin(w, h)  # 領域1
        id12-=id9(id10-1, id15)  # 領域2
        id12-=id9(id14, id11-1)  # 領域3
        id12+=id9(id10-1, id11-1)  # 領域4
        return id12

    id16=[0]*(id1**2)
    # いろいろな長方形に対して計算
    for id14, id15 in id6(id8(id1), id17=2):
        id18=id1-id14
        id19=id1-id15
        id20=(id14+1)*(id15+1)-1
        for id10, id11 in id6(id8(id18), id8(id19)):
            id21=id13(id10, id11, id10+id14, id11+id15)
            id16[id20]=id22(id16[id20], id21)  # 幅w、高さhの長方形を張ったときのおいしさのうち最大値

    # 「店員が焼ける能力の上限と同じ面積の長方形を張ると逆に点が下がる」場合があるため、
    # 調整を行う(それまでの最大値を上回るときのみ値を更新)
    id21=0
    for id23 in id8(id1**2):
        if id16[id23]>id21:
            id21=id16[id23]
        else:
            id16[id23]=id21

    for id23 in id4:
        print(id16[id23-1])
    return None

id1=id24(input())
id2=[[id24(id23) for id23 in input().split()] for _ in id8(id1)]
id3=id24(input())
id4=[id24(input()) for id23 in id8(id3)]
id0(id1, id2, id3, id4)