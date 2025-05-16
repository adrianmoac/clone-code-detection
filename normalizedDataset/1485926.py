#!/usr/bin/env python3
#-*-coding: utf-8-*-import array
from id0 import*from id1 import*import id2
import id3 
from id4 import*import id5
import id6
import id7

id8=id9(input())
id10=id11(map(id9, input().split()))

id12=0
id13=0
id14=0
for id15 in id10:
    if id15%4==0:
        id12+=1
    elif id15%2==0:
        id13+=1
    else:
        id14+=1

id16=4

def id17():
    global id14, id16
    id14-=1
    id16=0

def id18():
    global id13, id16
    id13-=1
    id16=2

def id19():
    global id12, id16
    id12-=1
    id16=4

def id20():
    if id16==4:
        if id14>0:
            id17()
        elif id13>0:
            id18()
        elif id12>0:
            id19()
    elif id16==2:
        if id13>0:
            id18()
        elif id12>0:
            id19()
        else:
            return False
    elif id16==0:
        if id12>0:
            id19()
        else:
            return False
    return True

id21=True
for id22 in id23(id8):
    id24=id20()
    if not id24:
        id21=False
        break
if id21:
    print("Yes")
else:
    print("No")