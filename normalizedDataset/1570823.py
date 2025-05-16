def id0(id1):
    if id1<0:
        return 0
    elif id1<id2:
        return id1
    else:
        return id2


if id3=="__main__":
    # 砂の合計量
    id2=id4(input())

    # ひっくり返す回数
    id5=id4(input())
    # ひっくり返す秒数
    id6=id7(map(id4, input().split()))
    # クエリの個数
    id8=id4(input())

    # r の制御のための変数
    id9=0
    id10=-1
    id11=0
    id12=id2
    id13=0
    id14=[id6[0]]
    for id15 in id16(1, id5):
        id14.id17(id6[id15]-id6[id15-1])

    id18=0
    for id15 in id16(id8):
        # t:時刻 a:初期に A に入っている砂の量
        id19, id20=id7(map(id4, input().split()))
        while id9<id5 and id6[id9]<id19:
            id13+=id10*id14[id9]
            # sについて更新
            if id13<0:
                id11+=-id13
                if id12<id11:
                    id11=id12
                id13=0
            # eについて更新
            if id2<id13+id12-id11:
                id21=(id13+id12-id11)-id2
                id12-=id21
                if id12<id11:
                    id12=id11
            if id2<id13:
                id13=id2

            id18=id6[id9]
            id9+=1
            id10*=-1

        id22=id19-id18

        if id20<id11:
            id23=id13
        elif id20<id12:
            id23=id13+id20-id11
        else:
            id23=id13+id12-id11

        id23+=id22*id10

        print(id0(id23))
        # print("s:"+str(s)+" e:"+str(e)+" y:"+str(y)+" a:"+str(a)+" ret:"+str(ret))