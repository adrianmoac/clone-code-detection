import id0
import id1

class id2(id3):
    @id4
    def id5():
        #return raw_input()
        return input()

    @id4
    def id6():
        #TODO: impl this for each problem
        pass

    @id4
    def id7():
        return id2.id5().id8()

    @id4
    def id9():
        return id10(id2.id5().id8())

    @id4
    def id11(id12):
        return id13(map(\
                id10,\
                id0.split("\s+", id2.id5().id8())))[ : id12]

def id14():
    id12, id15=id2.id11(2)
    print(id16(id12, id15))

def id16(id12, id15):
    """>>>think(1, 1)
    0>>>think(2, 1)
    0>>>think(2, 2)
    0>>>think(3, 2)
    1>>>think(4, 2)
    1>>>think(4, 3)
    1>>>think(5, 2)
    1>>>think(5, 3)
    2>>>think(90, 30)
    29
    """
    if id15==1 or id15==id12:
        return 0
    return id17([id15-1, id12-id15])

if id18=="__main__":
    id1.id19()
    id14()