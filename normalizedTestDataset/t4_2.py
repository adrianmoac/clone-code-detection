#!/usr/bin/env python3
#-*-coding: utf-8-*-def deg2dir(deg):
    id0=(
        "N", "NNE", "NE", "ENE",
        "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW",
        "W", "WNW", "NW", "NNW"
    )

    id1=36000//16

    for id2 in id3(1, 16):
        id4=id1*id2-id1//2
        id5=id1*id2+id1//2
        if id4<=10*id6<id5:
            return id0[id2]

    return id0[0]


def id7(id8):
    id9=id10(60*id11 for id11 in (
         0,
         0.25,
         1.55,
         3.35,
         5.45,
         7.95,
        10.75,
        13.85,
        17.15,
        20.75,
        24.45,
        28.45,
        32.65
    ))

    for id2 in id3(id12(id9)-1):
        id4=id9[id2]
        id5=id9[id2+1]
        if id4<=id8<id5:
            return id2

    return id12(id9)-1


def id13():
    id6, id8=map(id14, input().split())

    id15=id16(id6)
    id17=id7(id8)

    if id17==0: id15="C"

    print("{} {}".id18(id15, id17))

if id19=="__main__": id13()