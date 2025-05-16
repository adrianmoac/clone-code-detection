#!/usr/bin/env python
#-*-coding: UTF-8-*-import sys
import id0
import id1
import id2
import id3
import id4
#sys.stdin=file('input.txt')
#sys.stdout=file('output.txt','w')
#10**9+7
id5=1000000007
#mod=1777777777
id6=3.141592653589
id7=id8("inf")
id9=[(1,0),(-1,0),(0,1),(0,-1)]
id10=[(-1,-1),(-1,1),(1,1),(1,-1)]
def id11(id12,id13): return id14(id12-id13) if id12>=0 and id13>=0 else  id12+id14(id13) if id12>=0 else id14(id12)+id13 if id13>=0 else id14(id14(id12)-id14(id13))
def id15(id16): return [(id17.id18(id17[id19-2]+id17[id19-1]), id17[id19-2])[1] for id17 in [[0, 1]] for id19 in id20(2, id16)]
def id21(id12,id13): return id12 if id13==0 else id21(id13,id12%id13)
def id22(id12,id13): return id12*id13/id21(id12,id13)
def id23(id24,id25,id26,id27): return ((id24-id26)**2+(id25-id27)**2)**0.5
def id28(id29,id30,id31,id32,id33,id34,id35,id36): return 1 if id14((id32-id30)*(id36-id34)+(id31-id29)*(id35-id33))<1.e-10 else 0
def id37(id38,id39=[1]):
    for id19 in id20(id38):
        id39=map(lambda id40,id41:id40+id41,[0]+id39,id39+[0])
    return id39

class id42:
    def id43(id44, id45):
        id44.id46=[0]*id45
        id44.id47=id20(id45)
        id44.id48=id45

    def id49(id44, id40):
        if id40==id44.id47[id40]: return id40

        id44.id47[id40]=id44.id49(id44.id47[id40])
        return id44.id47[id40]

    def id50(id44, id40, id41): #2つの頂点が同じグループであるかを判定する
        return id44.id49(id40)==id44.id49(id41)

    def id51(id44, id40, id41): #辺で接続されている2つの頂点を投げて統合する
        id40,id41=id44.id49(id40),id44.id49(id41)
        if id40==id41:
            return

        id44.id48-=1
        if id44.id46[id40]<id44.id46[id41]:
            id44.id47[id40]=id41
        else:
            id44.id47[id41]=id40
            if id44.id46[id40]==id44.id46[id41]:
                id44.id46[id40]+=1

    def id52(id44):
        return id44.id48
    def id53(id44):
        return id44.id47

id16,id54,id39=map(id55,id56().split())
id57=id42(id16)
id58=id42(id16)
id59=[1]*id16

for id19 in id20(id54):
    id12,id13=map(id55,id56().split())
    id57.id51(id12-1,id13-1)

for id19 in id20(id39):
    id12,id13=map(id55,id56().split())
    id58.id51(id12-1,id13-1)

id60=id57.id53()
id61=id58.id53()
id62={}
for id19 in id20(id16):
    while 1:
        if id60[id19]!=id60[id60[id19]]:
            id60[id19]=id60[id60[id19]]
        else:
            break
    while 1:
        if id61[id19]!=id61[id61[id19]]:
            id61[id19]=id61[id61[id19]]
        else:
            break

for id19 in id20(id16):
    if (id60[id19],id61[id19]) in id62:
        id62[(id60[id19],id61[id19])]+=1
    else:
        id62[(id60[id19],id61[id19])]=1
for id19 in id20(id16):
    print id62[(id60[id19],id61[id19])],