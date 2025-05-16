class id0:
    def id1(id2, id3, id4):
        id2.id5=id3
        id2.id4=id4

    @id6
    def id7(id2):
        id8=id2.id9.split("+")
        id10=0
        for id11 in id8:
            id10+=id12(id11)
        return id10

    @id6
    def id9(id2):
        #print("rank={0}".format(self.rank))
        id13=id2.id14(id2.id4, id15(id2.id5)-1)
        #print("gen_points={0}".format(points))
        id9=id2.id16(id13)
        #print("expression={0}".format(expression))
        return id9

    def id14(id2, id11, id17):
        """
        num → 2進数に変換してリストで返す
        """
        id13=[0]*id17
        id18=id11
        id19=1
        while True:
            id20=id18%2 
            if id20==1:
                id13[id17-id19]=1
            id18=id18>>1
            if id18==0:
                break
            id19+=1

        return id13

    def id16(id2, id13):
        """
        point位置に"+"を挿入する
        """
        id19=0 #points[0]
        id21=id2.id5[0:id19]
        for id22 in id13:
            id21+=id2.id5[id19:id19+1]
            if id22==1:
                id21+="+"
            id19+=1

        id21+=id2.id5[id19:]
        return id21

class id23:
    def id1(id2, id3):
        id2.id3=id3
        id2.id24=id2.id25()

    def id15(id2):
        return id15(id2.id3)

    def id25(id2):
        id24=[]
        for id19 in id26(0, id27(2, id2.id15()-1)):
            id9=id0(id2.id3, id19)
            id24.id28(id9)
        return id24

    def id29(id2):
        id10=0
        for id9 in id2.id24:
            id10+=id9.id7

        return id10

if id30=="__main__":
    id11=input()
    id31=id23(id11)
    print(id31.id29())