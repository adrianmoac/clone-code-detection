from id0 import*# Queue, LifoQueue, PriorityQueue
from id1 import*#bisect, insort
from id2 import*#deque, Counter,OrderedDict,defaultdict
#set([]) 
import id3
import id4
import id5
import id6
import id7
id8=lambda : map(id9,id10().split())
def id11(id12, id13, id14, id15, id16):
    id17=[-1,-1,-1,0,0,0,1,1,1]
    id18=[-1,0,1,-1,0,1,-1,0,1]
    for id19 in id20(9):
        id21, id22=id13+id17[id19], id14+id18[id19]
        if 0<=id21<id15 and 0<=id22<id16:
            if id12[id21][id22]!="#":
                return False
    return True
def id23(id13, id14, id12, id24, id15, id16):
    if id12[id13][id14]==".":
        return True
    
    id17=[-1,-1,-1,0,0,0,1,1,1]
    id18=[-1,0,1,-1,0,1,-1,0,1]
    for id19 in id20(9):
        id21, id22=id13+id17[id19], id14+id18[id19]
        if 0<=id21<id15 and 0<=id22<id16:
            if id24[id21][id22]=="#":
                return True
            if id11(id12, id21, id22, id15, id16):
                id24[id21][id22]="#"
                return True
    return False

def id25():
    id15, id16=id8()
    #bd=[raw_input() for _ in xrange(H)]
    id12=[["." for id26 in id20(id16)] for id26 in id20(id15)]
    for id26 in id20(id15):
        id27=id10()
        for id28 in id20(id16):
            id12[id26][id28]=id27[id28]
    id24=[["." for id26 in id20(id16)] for id26 in id20(id15)]
    for id26 in id20(id15):
        for id28 in id20(id16):
            if not id23(id26,id28, id12, id24, id15, id16):
                print "impossible"
                return
    print "possible"
    for id26 in id20(id15):
        for id28 in id20(id16):
            id7.id29.id30(id24[id26][id28])
        id7.id29.id30("\n")



if id31=="__main__":
    id25()
    