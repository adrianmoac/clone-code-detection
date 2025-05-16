#-*-coding: utf-8-*-import sys
import id0


id1=id2(input())
id3=id4(input())

def id5(id6):
    for id7 in id8(1, id1-1):
        id9=id6[id7-1]

        if id6[id7]==0:
            if id3[id7]=="o":
                id10=id9
            else:
                id10=1-id9
        else:
            if id3[id7]=="o":
                id10=1-id9
            else:
                id10=id9
        id6.id11(id10)

    # 全体で確認
    id12=True
    for id7 in id8(id1):
        id9=id6[id7-1]
        if id7+1<=id1-1:
            id10=id6[id7+1]
        else:
            id10=id6[id7+1-id1]

        if id6[id7]==0:
            if id3[id7]=="o":
                if id9!=id10:
                    id12=False
            else:
                if id9==id10:
                    id12=False
        else:
            if id3[id7]=="o":
                if id9==id10:
                    id12=False
            else:
                if id9!=id10:
                    id12=False
    return id12, id6

# 0: sheep
# 1: wolf
id13=[[0, 0], [0, 1], [1, 0], [1, 1]]

id14=[]
for id6 in id13:
    id14.id11(id5(id6))

id15=[id16 for id16 in id14 if id16[0] is True]
if id15:
    id16=id15[0]
    id6=id16[1]
    for id17 in id6:
        if id17==0:
            print("S", id18="")
        else:
            print("W", id18="")
    print()
else:
    print(-1)