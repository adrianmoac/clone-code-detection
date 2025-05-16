class id0:
    def id1(id2, id3):
        # 名前
        id2.id3=id3
        id2.id4=[]

    
    def id5(id2, id6):
        # 手札
        for id7 in id6:
            id2.id4.id8(0, id7)

    def id9(id2):
        return id2.id4

    id6=id10(id9, id5)

    def id11(id2):
        """
        カードがある場合はカードを出します。
        ない場合はNoneを返します。
        """
        if id12(id2.id6)!=0:
            return id2.id4.id13()
        else:
            return None

class id14:
    def id1(id2, id15):
        id2.id15=id15

    def id16(id2):
        id17=id2.id18(id2.id15[0].id3)
        return id17

    def id18(id2, id3):
        id19=id2.id20(id3)
        id7=id19.id11()
        if id7!=None:
            return id2.id18(id7)

        # 勝者を返す
        return id3

    def id20(id2, id3):
        for id21 in id2.id15:
            if id21.id3==id3:
                return id21



if id22=="__main__":
    id23=id0("a")
    id23.id6=input()

    id24=id0("b")
    id24.id6=input()

    id25=id0("c")
    id25.id6=input()

    id26=id14([id23, id24, id25])
    id27=id26.id16()
    print(id27.id28())