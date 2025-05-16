#!-*-coding:utf-8-*-import sys
id0,id1=map(id2,input().split())
id3=[]
for id4 in id5(id0):
    id3.id6(id7(input()))
id8=[[]*id1]*id0

for id4 in id5(id0):
    id8[id4]=id9(id3[id4])

if id0==1 and id1==1:
    if id8[0][0]=="#":
        print("#")
    else:
        print(0)
    id10.id11()
elif id0==1:
    for id4 in id5(id1):
        id12=0
        if id8[0][id4]=="#":
            print("#",id13="",id14="")
        elif id4==0:
            if id8[0][1]=="#":
                id12+=1
            print(id12,id13="", id14="")
        elif id4==id1-1:
            if id8[0][-2]=="#":
                id12+=1
            print(id12,id13="", id14="")
        else:
            if id8[0][id4-1]=="#":
                id12+=1
            if id8[0][id4+1]=="#":
                id12+=1
            print(id12,id13="",id14="")
    print("")
    id10.id11()
elif id1==1:
    for id4 in id5(id0):
        id12=0
        if id8[id4][0]=="#":
            print("#")
        elif id4==0:
            if id8[1][0]=="#":
                id12+=1
            print(id12)
        elif id4==id0-1:
            if id8[-2][0]=="#":
                id12+=1
            print(id12)
        else:
            if id8[id4-1][0]=="#":
                id12+=1
            if id8[id4+1][0]=="#":
                id12+=1
            print(id12)
    id10.id11()
    
for id4 in id5(id0):
    for id15 in id5(id1):
        if id8[id4][id15]=="#":
            print("#",id13="", id14="")
        else:
            if id4==0 and id15==0:
                id12=0
                if id8[0][1]=="#":
                    id12+=1
                if id8[1][0]=="#":
                    id12+=1
                if id8[1][1]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            elif id4==0 and id15==id1-1:
                id12=0
                if id8[0][-2]=="#":
                    id12+=1
                if id8[1][-1]=="#":
                    id12+=1
                if id8[1][-2]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            elif id4==0:
                id12=0
                if id8[id4][id15-1]=="#":
                    id12+=1
                if id8[id4][id15+1]=="#":
                    id12+=1
                if id8[id4+1][id15-1]=="#":
                    id12+=1
                if id8[id4+1][id15]=="#":
                    id12+=1
                if id8[id4+1][id15+1]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            elif id4==id0-1 and id15==0:
                id12=0
                if id8[-1][1]=="#":
                    id12+=1
                if id8[-2][0]=="#":
                    id12+=1
                if id8[-2][1]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            elif id4==id0-1 and id15==id1-1:
                id12=0
                if id8[-1][-2]=="#":
                    id12+=1
                if id8[-2][-1]=="#":
                    id12+=1
                if id8[-2][-2]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            elif id4==id0-1:
                id12=0
                if id8[id4][id15-1]=="#":
                    id12+=1
                if id8[id4][id15+1]=="#":
                    id12+=1
                if id8[id4-1][id15-1]=="#":
                    id12+=1
                if id8[id4-1][id15]=="#":
                    id12+=1
                if id8[id4-1][id15+1]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            elif id15==0:
                id12=0
                if id8[id4-1][id15]=="#":
                    id12+=1
                if id8[id4+1][id15]=="#":
                    id12+=1
                if id8[id4][id15+1]=="#":
                    id12+=1
                if id8[id4-1][id15+1]=="#":
                    id12+=1
                if id8[id4+1][id15+1]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            elif id15==id1-1:
                id12=0
                if id8[id4-1][id15]=="#":
                    id12+=1
                if id8[id4+1][id15]=="#":
                    id12+=1
                if id8[id4][id15-1]=="#":
                    id12+=1
                if id8[id4-1][id15-1]=="#":
                    id12+=1
                if id8[id4+1][id15-1]=="#":
                    id12+=1
                print(id12,id13="", id14="")
            else:
                id12=0
                if id8[id4-1][id15-1]=="#":
                    id12+=1
                if id8[id4-1][id15]=="#":
                    id12+=1
                if id8[id4-1][id15+1]=="#":
                    id12+=1
                if id8[id4][id15-1]=="#":
                    id12+=1
                if id8[id4][id15+1]=="#":
                    id12+=1
                if id8[id4+1][id15-1]=="#":
                    id12+=1
                if id8[id4+1][id15]=="#":
                    id12+=1
                if id8[id4+1][id15+1]=="#":
                    id12+=1
                print(id12,id13="", id14="")
    print("")