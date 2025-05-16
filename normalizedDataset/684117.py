#!/usr/bin/env python
#coding:utf-8

def id0():
    return map(id1, id2().split())


def id3(id4, id5):
    return id4 if id5==0 else id3(id5, id4%id5)


def id6(id4, id5, id7):
    id8=[[0,0],[0,0]]
    for id9 in id10(2):
        for id11 in id10(2):
            for id12 in id10(2):
                id8[id9][id11]=(id8[id9][id11]+id4[id9][id12]*id5[id12][id11])%id7
    return id8


def id13(id14, id15, id7):

    if id15==0:
        return [[1,0],[0,1]]

    id16=id13(id14, id15/2, id7)

    return id6(id16, id16, id7) if id15%2==0 else id6(id6(id16, id16, id7), id14, id7)
    

def id17(id14, id15, id7):
    
    if id15==0:
        return 1

    id16=id17(id14, id15/2, id7)
    
    return id16*id16%id7 if id15%2==0 else id16*id16*id14%id7


def id18((id19, id20, id7)):
    
    id21=id3(id19, id20)

    # one(n): 111...111 のように、1 が n 個並んだ整数とする
    # lcm(one(A), one(B))=one(A)*one(B)/one(C)
    
    # one(A)%MOD を計算
    id22=[[10,1], [0,1]]
    id23=id13(id22, id19, id7)
    
    # (one(B)/one(C))%MOD を計算
    id22=[[id17(10, id21, id7),1],[0,1]]
    id24=id13(id22, id20/id21, id7)

    # one(A)*(one(B)/one(C))%MOD を計算
    print id23[0][1]*id24[0][1]%id7


if id25=="__main__":
    id18(id0())