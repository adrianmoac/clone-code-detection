import id0
import id1
import id2

class id3(id4):
    @id5
    def id6():
        #return raw_input()
        return input()

    @id5
    def id7():
        #TODO: impl this for each problem
        pass

    @id5
    def id8():
        return id3.id6().id9()

    @id5
    def id10():
        return id11(id3.id6().id9())

    @id5
    def id12(id13):
        return id14(map(\
                id11,\
                id0.split("\s+", id3.id6().id9())))[ : id13]

def id15(id13):
    """>>>a=think_appr_square_with_tiles(26)>>>a[0]+a[1]
    1>>>a=think_appr_square_with_tiles(41)>>>a[0]+a[1]
    4>>>a=think_appr_square_with_tiles(100000)>>>a[0]+a[1]
    37
    """
    id16=id11(id1.id17(id13))
    if id16**2==id13:
        #print('path 1')
        return 0, 0 # diff, remain

    id18, id19=id13, id13
    for id20 in id21(id16, 0,-1):
        id22=id13//id20
        id23=id24(id20-id22)
        id25=id13%id22
        if id18+id19>id23+id25:
            #print('{0:d}, {1:d}=>{2:d}, {3:d} # {4:d} {5:d} # {6:d}'.format(diff, remain, d, r, n, m, i))
            id18, id19=id23, id25 
    #print('path 2 {0:d} {1:d}'.format(diff, remain))
    return id18, id19

def id26():
    id13=id3.id10()
    id18, id19=id15(id13)
    print(id18+id19)

if id27=="__main__":
    id2.id28()
    id26()