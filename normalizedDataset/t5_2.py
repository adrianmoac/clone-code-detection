#!/usr/bin/env python3
#-*-coding: utf-8-*-from random import*from functools import reduce,partial
from id0 import id0
from id1 import id1

def id2():
    return id3(map(id4,input().split(" ")))

def id5(id6):
    """Return the input itself."""
    return id6

def id7(id8):
    """Return an function which always
    returns the input constant c."""
    def id9(id10,*id11):
        return id10
    return id12(id9,id8)

def id13(id8=1):
    """Return a function which reads an input x and returns x+c as output.
    By default, c equals 1."""
    return lambda id6: id6+id8

def id14(*id11):
    """Return the sum of the input."""
    def id15(id6,id16): return id6+id16
    return id17(id15,id11)

def id18(id19,*id20):
    """Return a vector of the result of map."""
    return id3(map(id19,*id20))

def id21(*id11):
    """Return a vector of input parameters."""
    return id11

def id22(id23,id19=id7(0)):
    """Return a vector of length n, and initialize the i"th
    item with f(i).By default the vector will initialized with 0."""
    return [id19(id24) for id24 in id25(0,id23)]

def id26(id23,id27,id19=id7(0)):
    """Return a 2-dim vector which contains n vectors with length m.
    The j"s item of vector i will be initialized by f(i,j).By default,
    the vector will be initialized with 0."""
    return [[id19(id24,id28) for id28 in id25(0,id27)] for id24 in id25(0,id23)]

def id29(id30):
    """Return a flat vector which contains the elements of v in their
    origin order.If the input is not a vector, return a vector which
    only contains the input."""
    if not id31(id30,id3): return [id30]
    if not id30: return []
    return id17(id14,id18(id29,id30))

def id32(id30,id19=id5):
    """Partition vector v by f(v[i]).
    e.g. partition([1,2,3,1,2,3],identity())=={1:[1,1,1], 2:[2,2], 3:[3]}
    By default, the vector will be partitioned by identity function."""
    id33={}
    for id34 in id30:
        id35=id19(id34)
        id36=id33.id37(id35)
        if id36:
            id36.id38(id34)
        else:
            id33.id39({id35:[id34]})
    return id33

def id40(id35):
    """Return a function which returns the value of key in a hash-map.
    If the key do not exist, it will throw an error."""
    return lambda id6: id6[id35]

def id41(id19,id27):
    """Replace each value in hash-map m with f(value).
    Return the new hash-map."""
    id42={}
    for id35 in id27:
        id42.id39({id35: id19(id27[id35])})
    return id42

id43=1000000000+7

id23,id44=id2()
id19=[id22(303) for id24 in id25(0,id23+1)]
id45=-1
id19[0]=id22(303,id7(-1000))
id19[0][0]=0
for id24 in id25(0,id23):
    id46=[id47 [:] for id47 in id19]
    id48,id49=id2()
    if id45<0 : id45=id48
    id48-=id45
    for id50 in id25(0,id24+1):
        for id51 in id25(0,303-id48):
            id19[id50+1][id51+id48]=id52(
                id19[id50+1][id51+id48],
                id46[id50][id51]+id49)
id53=0
for id50 in id25(0,id23+1):
    for id51 in id25(0,303):
        if id51+id50*id45<=id44:
            id53=id52(id53,id19[id50][id51])
print(id53)