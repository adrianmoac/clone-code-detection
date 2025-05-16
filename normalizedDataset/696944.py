#!/usr/bin/env python

id0=1000000007


def id1():
    id2, id3, id4=map(id5, id6().split())
    id7=map(id5, id6().split())
    return id3, id4, id7


def id8(id9, id10):
    if id10==0:
        return 1
    id11=id8(id9, id10/2)
    return id11*id11%id0 if id10%2==0 else id11*id11*id9%id0


def id12((id3, id4, id7)):

    if id3==1:
        for id13 in id14(id7):
            print id13
        return

    
    id15=id16(id7)-1
    for id17 in id18(id16(id7)-1,-1,-1):
        if id7[id15]<id7[id17]:
            id15=id17
    
    while id4:
        id19=-1
        id20=-1
        for id21, id22 in id23(id7):
            if id19==-1 or id19>id22:
                id19=id22
                id20=id21
        id7[id20]*=id3
        
        id4-=1
        
        if id20==id15:
            id7.id24()
            for id17 in id18(id4%id16(id7)):
                id7[id17]*=id3
            id7=id7[id4%id16(id7):]+id7[:id4%id16(id7)]
                
            id25=id4/id16(id7)
            for id17 in id18(id16(id7)):
                id7[id17]=id7[id17]*id8(id3, id25)%id0

            for id13 in id7:
                print id13
            return

    for id13 in id14(id7):
        print id13%id0


if id26=="__main__":
    id12(id1())