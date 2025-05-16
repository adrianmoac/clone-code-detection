#!/usr/bin/python
#-*-coding:utf-8-*-N=int(raw_input())
id0=id1()

id2=-1
id3=0
id4=0

for id5 in id6(id7):
    if id0[id5]=="o":
        id3+=1
    else:
        id4+=1
#print maru, batsu

id8={"S":"W", "W":"S"}
id2=""
id9=["SS", "SW", "WS", "WW"]

for id10 in id9:
    id2=""
    id11=0
    id12=0
    id2+=id10
    for id5 in id6(2, id7,1):
        if id2[id5-1]=="S":
            if id0[id5-1]=="o":
                id2+=id2[id5-2]
            else:
                id2+=id8[id2[id5-2]]
        else:
            if id0[id5-1]=="o":
                id2+=id8[id2[id5-2]]
            else:
                id2+=id2[id5-2]
    if id2[0]=="S":
        if id0[0]=="o":
            if id2[-1]==id2[1]:
                id11=1
        else:
            if id2[-1]!=id2[1]:
                id11=1
    else:
        if id0[0]=="o":
            if id2[-1]!=id2[1]:
                id11=1
        else:
            if id2[-1]==id2[1]:
                id11=1

    if id2[-1]=="S":
        if id0[-1]=="o":
            if id2[-2]==id2[0]:
                id12=1
        else:
            if id2[-2]!=id2[0]:
                id12=1
    else:
        if id0[-1]=="o":
            if id2[-2]!=id2[0]:
                id12=1
        else:
            if id2[-2]==id2[0]:
                id12=1

    if id11==1 and id12==1:
        break

if id11==0 or id12==0:
    print-1
else:
    print id2