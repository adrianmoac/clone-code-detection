id0=id1(input())
id2=id3(input())
id4=[0]*id0
for id5 in id6(id0):
    if id2[id5]=="o":
        id4[id5]=1
    else:
        id4[id5]=-1

id7=[[1]*id0,[1]*id0,[-1]*id0,[-1]*id0]

if id4[0]==1:
    id7[0][1]=1
    id7[0][id0-1]=1
    id7[1][1]=-1
    id7[1][id0-1]=-1
    id7[2][1]=1
    id7[2][id0-1]=-1
    id7[3][1]=-1
    id7[3][id0-1]=1
else:
    id7[0][1]=1
    id7[0][id0-1]=-1
    id7[1][1]=-1
    id7[1][id0-1]=1
    id7[2][1]=1
    id7[2][id0-1]=1
    id7[3][1]=-1
    id7[3][id0-1]=-1

id8=-1
for id5 in id6(1,id0-1):
    if id5==id0-2:
        for id9 in id6(4):
            if id4[id5]*id7[id9][id5]==1:
                if id7[id9][id5+1]==id7[id9][id5-1]:
                    if id4[id5+1]*id7[id9][id5+1]==1:
                        if id7[id9][0]==id7[id9][id5]:
                            id8=id9
                            break
                    else:
                        if id7[id9][0]==-id7[id9][id5]:
                            id8=id9
                            break
            else:
                if id7[id9][id5+1]==-id7[id9][id5-1]:
                    if id4[id5+1]*id7[id9][id5+1]==1:
                        if id7[id9][0]==id7[id9][id5]:
                            id8=id9
                            break
                    else:
                        if id7[id9][0]==-id7[id9][id5]:
                            id8=id9
                            break
    for id9 in id6(4):
        if id4[id5]*id7[id9][id5]==1:
            id7[id9][id5+1]=id7[id9][id5-1]
        else:
            id7[id9][id5+1]=-id7[id9][id5-1]

if id8==-1:
    print(id8)
else:
    for id5 in id6(id0):
        if id7[id8][id5]==1:
            print("S",id10="")
        else:
            print("W",id10="")