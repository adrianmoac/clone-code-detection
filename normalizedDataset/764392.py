#!/usr/bin/env python


def id0():
    id1, id2=map(id3, id4().split())
    id5=[]
    for id6 in id7(id1):
        id5.id8(id4())
    return id1, id2, id5


def id9((id1, id2, id5)):
    id10=[[True for id11 in id7(id2)] for id6 in id7(id1)]

    for id12 in id7(id1):
        for id13 in id7(id2):
            if id5[id12][id13]=="#":
                continue
            for (id14, id15) in [(-1,-1), (-1, 0), (-1, 1),\
                             ( 0,-1), ( 0, 0), ( 0, 1),\
                             ( 1,-1), ( 1, 0), ( 1, 1)]:
                id16=id12+id14
                id17=id13+id15
                if not (0<=id16<id1 and 0<=id17<id2):
                    continue
                id10[id16][id17]=False


    id18=[["." for id11 in id7(id2)] for id6 in id7(id1)]
    for id12 in id7(id1):
        for id13 in id7(id2):
            
            if not id10[id12][id13]:
                continue
            
            for (id14, id15) in [(-1,-1), (-1, 0), (-1, 1),\
                             ( 0,-1), ( 0, 0), ( 0, 1),\
                             ( 1,-1), ( 1, 0), ( 1, 1)]:
                id16=id12+id14
                id17=id13+id15
                if not (0<=id16<id1 and 0<=id17<id2):
                    continue
                id18[id16][id17]="#"

    
    for id12 in id7(id1):
        for id13 in id7(id2):
            if id18[id12][id13]!=id5[id12][id13]:
                print "impossible"
                return

    
    id19=[[] for id6 in id7(id1)]
    
    for id12 in id7(id1):
        for id13 in id7(id2):
            id19[id12].id8("#" if id10[id12][id13] else ".")
    
    print "possible"
    for id12 in id7(id1):
        print "".id20(id19[id12])


if id21=="__main__":
    id9(id0())