class id0(id1):
    
    def id2(id3):
        id3.id4=[
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]
        ]
        id3.id5=[0]*8
        id3.id6=[0]*8
        id3.id7=[0]*15
        id3.id8=[0]*15
    
    def id9(id3, id10, id11):
        assert id3.id4[id10][id11]==0
        id3.id4[id10][id11]=1
        id3.id5[id10]+=1
        id3.id6[id11]+=1
        id3.id7[id10+id11]+=1
        id3.id8[id10-id11+7]+=1
    
    def id12(id3, id10, id11):
        assert id3.id4[id10][id11]==1
        id3.id4[id10][id11]=0
        id3.id5[id10]-=1
        id3.id6[id11]-=1
        id3.id7[id10+id11]-=1
        id3.id8[id10-id11+7]-=1
    
    def id13(id3):
        if id14(id3.id5)>1: return False
        if id14(id3.id6)>1: return False
        if id14(id3.id7)>1: return False
        if id14(id3.id8)>1: return False
        return True
    
    def id15(id3, id10, id11):
        return id3.id4[id10][id11]==0
    
    def id16(id3):
        id17=[]
        for id18 in id3.id4:
            id19=""
            for id20 in id18:
                if id20==1:
                    id19+="Q"
                else:
                    id19+="."
            id17.id21(id19)
        return "\n".id22(id17)


class id23(id1):
    
    @id24
    def id25(id26, id4):
        id27=id26.id28(id4, 0)
        if id27:
            return id29(id27)
        else:
            return "No Answer"
    
    @id24
    def id28(id26, id4, id10):
        if not id4.id13():
            return None
        
        if id10>7:
            return id4
        
        if id4.id5[id10]>0:
            return id26.id28(id4, id10+1)
        
        for id11 in id30(8):
            if id4.id15(id10, id11):
                id4.id9(id10, id11)
                if id26.id28(id4, id10+1):
                    return id4
                id4.id12(id10, id11)
        return None


if id31=="__main__":
    id4=id0()
    for id10 in id30(8):
        id18=input()
        for id11 in id30(8):
            if id18[id11]=="Q":
                id4.id9(id10, id11)
    id27=id23.id25(id4)
    print(id27)