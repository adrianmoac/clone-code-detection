import id0

class id1:

    def id2(id3, id4):

        
        id5=id4/id3.id6[0][2]
        id7=id3.id6[0][0]-id5
        id8=id3.id6[0][0]+id5
        id9=id3.id6[0][1]-id5
        id10=id3.id6[0][1]+id5

        for id11 in id12(1, id3.id13):

            id5=id4/id3.id6[id11][2]
            id14=id3.id6[id11][0]-id5
            id15=id3.id6[id11][0]+id5

           
            if id14>id8 or id15<id7:
                return False

           
            id7=id16(id7, id14)
            id8=id17(id8, id15)

        for id11 in id12(1, id3.id13):

            id5=id4/id3.id6[id11][2]
            id18=id3.id6[id11][1]-id5
            id19=id3.id6[id11][1]+id5

            
            if id18>id10 or id19<id9:
                return False

            
            id9=id16(id9, id18)
            id10=id17(id10, id19)

        return True

    def id20(id3, id13, id6):

        id3.id13=id13
        id3.id6=id6

        id21=-1
        id22=id23(10, 9)
        id24=(id21+id22)/2.0

        for _ in id12(100):

            if id3.id2(id24):
                id22=id24
            else:
                id21=id24

            id24=(id21+id22)/2.0

        print id24

if id25=="__main__":

    id13=id26(id27())
    id6=[[id28(id29) for id29 in id27().split()] for id11 in id12(id13)]

    id30=id1()
    id30.id20(id13, id6)