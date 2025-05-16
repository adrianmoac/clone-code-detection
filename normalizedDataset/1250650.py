#!/usr/bin/env python3
#-*-coding: utf-8-*-from random import*from functools import reduce,partial
from id0 import id0

def id1():
    return id2(map(id3,input().split(" ")))

def id4(id5):
    """Return the input itself."""
    return id5

def id6(id7):
    """Return an function which always
    returns the input constant c."""
    def id8(id9,*id10):
        return id9
    return id11(id8,id7)

def id12(id7=1):
    """Return a function which reads an input x and returns x+c as output.
    By default, c equals 1."""
    return lambda id5: id5+id7

def id13(*id10):
    """Return the sum of the input."""
    def id14(id5,id15): return id5+id15
    return id16(id14,id10)

def id17(id18,*id19):
    """Return a vector of the result of map."""
    return id2(map(id18,*id19))

def id20(*id10):
    """Return a vector of input parameters."""
    return id10

def id21(id22,id18=id6(0)):
    """Return a vector of length n, and initialize the i"th
    item with f(i).By default the vector will initialized with 0."""
    return [id18(id23) for id23 in id24(0,id22)]

def id25(id22,id26,id18=id6(0)):
    """Return a 2-dim vector which contains n vectors with length m.
    The j"s item of vector i will be initialized by f(i,j).By default,
    the vector will be initialized with 0."""
    return [[id18(id23,id27) for id27 in id24(0,id26)] for id23 in id24(0,id22)]

def id28(id29):
    """Return a flat vector which contains the elements of v in their
    origin order.If the input is not a vector, return a vector which
    only contains the input."""
    if not id30(id29,id2): return [id29]
    if not id29: return []
    return id16(id13,id17(id28,id29))

def id31(id29,id18=id4):
    """Partition vector v by f(v[i]).
    e.g. partition([1,2,3,1,2,3],identity())=={1:[1,1,1], 2:[2,2], 3:[3]}
    By default, the vector will be partitioned by identity function."""
    id32={}
    for id33 in id29:
        id34=id18(id33)
        id35=id32.id36(id34)
        if id35:
            id35.id37(id33)
        else:
            id32.id38({id34:[id33]})
    return id32

def id39(id34):
    """Return a function which returns the value of key in a hash-map.
    If the key do not exist, it will throw an error."""
    return lambda id5: id5[id34]

def id40(id18,id26):
    """Replace each value in hash-map m with f(value).
    Return the new hash-map."""
    id41={}
    for id34 in id26:
        id41.id38({id34: id18(id26[id34])})
    return id41

id42=1000000000+7

id22,id43=id1()
id44=id1()
id45=0
id46=id43
for id33 in id44:
    if id33>id45+id43:
        id46=id46+id43
    else:
        id46=id46+id33-id45
    id45=id33
print(id46)