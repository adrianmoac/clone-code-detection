#!/usr/bin/env python
#-*-coding: UTF-8-*-import time
import id0
import id1
import id2
import id3
import id4
import id5
import id6
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
id7=1000000007
#mod=1777777777
id8=3.141592653589
id9=id10("inf")
id11=[(1,0),(-1,0),(0,1),(0,-1)]
id12=[(-1,-1),(-1,1),(1,1),(1,-1)]
def id13(id14,id15): return id14 if id15==0 else id13(id15,id14%id15)
def id16(id14,id15): return id14*id15/id13(id14,id15)
def id17(id18,id19,id20,id21): return ((id18-id20)**2+(id19-id21)**2)**0.5
def id22(id23,id24,id25,id26,id27,id28,id29,id30): return 1 if id31((id26-id24)*(id30-id28)+(id25-id23)*(id29-id27))<1.e-10 else 0

id32,id33=map(id34,id35().split())
#l=map(int,raw_input().split())
id36=[]
id37=id11+id12
for id38 in id39(id32):
    id36.id40(id35())

id41=[["."]*id33 for id38 in id39(id32)]
id42=[["."]*id33 for id38 in id39(id32)]
id43=[(0,0)]+id11+id12

def id44(id45,id46):
    for id14,id15 in id43:
        if 0<=id45+id14<id32 and 0<=id46+id15<id33:
            if id36[id45+id14][id46+id15]==".":
                return 0
    return 1
for id38 in id39(id32):
    for id47 in id39(id33):
        if id44(id38,id47):
            id41[id38][id47]="#"

for id38 in id39(id32):
    id41[id38]="".id48(id41[id38])

for id38 in id39(id32):
    for id47 in id39(id33):
        if id41[id38][id47]=="#":
            for id14,id15 in id43:
                if 0<=id38+id14<id32 and 0<=id47+id15<id33:
                    id42[id38+id14][id47+id15]="#"
for id38 in id39(id32):
    id42[id38]="".id48(id42[id38])
    if id42[id38]!=id36[id38]:
        print "impossible"
        id49()
print "possible"
for id38 in id41:
    print id38