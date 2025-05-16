from id0 import id1


def id2(id3, id4):
    for id5 in id6(1, id7(id3)+1):
        id5%=id7(id3)
        id8=id5-1
        id9=(id5+1)%id7(id3)

        # 整合性のチェック
        if id4[id8] is not None and id4[id9] is not None:
            if id4[id5]==1:
                if id3[id5]=="o":
                    if id4[id9]!=id4[id8]:
                        return False
                else:
                    if id4[id9]==id4[id8]:
                        return False
            else:
                if id3[id5]=="o":
                    if id4[id9]==id4[id8]:
                        return False
                else:
                    if id4[id9]!=id4[id8]:
                        return False

        # nextを決める
        if id4[id8] is not None and id4[id9] is None:
            # ひつじ
            if id4[id5]==1:
                # 両隣が同じはず
                if id3[id5]=="o":
                    id4[id9]=id4[id8]

                # 両隣が違うはず
                else:
                    id4[id9]=-1*id4[id8]
            # おおかみ
            else:
                # 両隣が違うはず
                if id3[id5]=="o":
                    id4[id9]=-1*id4[id8]
                # 両隣が同じはず
                else:
                    id4[id9]=id4[id8]

    return True


def id10():
    id11=id12(input())
    id13=input()

    for id14, id15 in [(1, 1), (1,-1), (-1, 1), (-1,-1)]:
        id16=[None]*id11
        id16[0], id16[1]=id14, id15

        if id2(id13, id16):
            print(*["S" if id17==1 else "W" for id17 in id16], id18="")
            return

    print(-1)


if id19=="__main__":
    id10()