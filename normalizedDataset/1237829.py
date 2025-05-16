#-*-coding: utf-8-*-N=int(input())
id0=[id1(id2) for id2 in input().split()]

id3=0 #+start
id4=0 #-start

id5=id0[0]
if id5!=0:
    for id2 in id6(1, id7):
        if id5*(id5+id0[id2])>=0:
            id3+=id8(id5+id0[id2])+1
            if id5<0:
                id5=1
            else:
                id5=-1
        else:
            id5+=id0[id2]

    id4+=id8(id0[0])+1
    id5=id1(id0[0]/id8(id0[0])*-1)

    for id2 in id6(1, id7):
        if id5*(id5+id0[id2])>=0:
            id4+=id8(id5+id0[id2])+1
            if id5<0:
                id5=1
            else:
                id5=-1
        else:
            id5+=id0[id2] 

    print(id9(id3, id4))

else:
    id0[0]=1
    id3+=1
    id5=1
    for id2 in id6(1, id7):
        if id5*(id5+id0[id2])>=0:
            id3+=id8(id5+id0[id2])+1
            if id5<0:
                id5=1
            else:
                id5=-1
        else:
            id5+=id0[id2]
    
    id0[0]=-1
    id4+=1
    id5=-1
    for id2 in id6(1, id7):
        if id5*(id5+id0[id2])>=0:
            id4+=id8(id5+id0[id2])+1
            if id5<0:
                id5=1
            else:
                id5=-1
        else:
            id5+=id0[id2]   
    print(id9(id3, id4))
            
