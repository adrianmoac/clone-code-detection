#!/usr/bin/env python
#-*-coding: utf-8-*-_=input()
id0=input()
# print(s)

id1=[None]*id2(id0)

def id3(id4, id5, id0):
    if id5=="S":
        if id0=="o":
            return id4
        if id0=="x":
            if id4=="S":
                return "W"
            else:
                return "S"
    if id5=="W":
        if id0=="x":  # 両隣同じ
            if id4=="S":
                return "S"
            else:
                return "W"
        if id0=="o":
            if id4=="S":
                return "W"
            else:
                return "S"

# aN, a0, a1
def id6(id4, id5, id7, id0):
    id8=id4+id7
    if id5=="S":
        if id8=="SS" or id8=="WW":
            return id0=="o"
        if id4!=id7:
            return id0=="x"
    if id5=="W":
        if id8=="SS" or id8=="WW":
            return id0=="x"
        if id4!=id7:
            return id0=="o"


id9="-1"
for id10 in [("S", "S"), ("S", "W"), ("W", "S"), ("W", "W")]:
    id1[0], id1[1]=id10
    for id11 in id12(1, id2(id0)-1):
        id1[id11+1]=id3(id1[id11-1], id1[id11], id0[id11])
    # print("#", ini)
    # print(a)
    id13=(id6(id1[-2], id1[-1], id1[0], id0[-1]))
    id14=(id6(id1[-1], id1[0], id1[1], id0[0]) )

    if id13 and id14:
        id9="".id15(id1)
        break
print(id9)


        
    
