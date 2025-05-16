#!/usr/bin/env python3
#-*-coding: utf-8-*-def hhmm2min(hhmm):
    id0=id1(id2[:2])
    id3=id1(id2[2:4])
    return 60*id0+id3

def id4(id3):
    id0=id3//60
    id3=id3%60
    return "{:02d}{:02d}".id5(id0, id3)

def id6():
    id7=id1(input())

    id8=[]
    for _ in id9(id7):
        id10, id11=map(id12, input().split("-"))
        id8.id13((id10, id11))

    return id8

def id14(id8):
    id15=[False]*(24*60//5+1)

    for id10, id11 in id8:
        id16=id10//5
        id17=id11//5+(1 if id11%5 else 0)
        id15[id16:id17]=[True]*(id17-id16)

    return id15

def id18(id15):
    id10=None
    id11=None
    id19=False

    for id20, id21 in id22(id15):
        if id21:
            if not id19:
                id10=5*id20
                id19=True
        else:
            if id19:
                id11=5*id20
                yield (id10, id11)
                id19=False

    if id19:
        yield (id10, 24*60)

def id23():
    id8=id6()

    id15=id14(id8)

    for id10, id11 in id18(id15):
        id24, id25=map(id4, (id10, id11))
        print("{}-{}".id5(id24, id25))

if id26=="__main__": id23()