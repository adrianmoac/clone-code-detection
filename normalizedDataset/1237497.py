id0=id1(input())
id2=id3(map(id1, input().split()))

id4=0
id5=id2[0]

if id2[0]<0:
    id5=1
    id6=1-id2[0]
    for id7 in id8(1, id0):
        if id5<0:
            id5+=id2[id7]
            if id5<=0:
                id6+=1-id5
                id5=1
        elif id5>0:
            id5+=id2[id7]
            if id5>=0:
                id6+=id5+1
                id5=-1
    id5=id2[0]
    id9=0
    for id7 in id8(1, id0):
        if id5<0:
            id5+=id2[id7]
            if id5<=0:
                id9+=1-id5
                id5=1
        elif id5>0:
            id5+=id2[id7]
            if id5>=0:
                id9+=id5+1
                id5=-1
    if id9<id6:
        id4=id9
    else:
        id4=id6
elif id2[0]>0:
    id5=id2[0]
    id6=0
    for id7 in id8(1, id0):
        if id5<0:
            id5+=id2[id7]
            if id5<=0:
                id6+=1-id5
                id5=1
        elif id5>0:
            id5+=id2[id7]
            if id5>=0:
                id6+=id5+1
                id5=-1
    id5=-1
    id9=1+id2[0]
    for id7 in id8(1, id0):
        if id5<0:
            id5+=id2[id7]
            if id5<=0:
                id9+=1-id5
                id5=1
        elif id5>0:
            id5+=id2[id7]
            if id5>=0:
                id9+=id5+1
                id5=-1
    if id9<id6:
        id4=id9
    else:
        id4=id6
else:
    id5=1
    id6=1
    for id7 in id8(1, id0):
        if id5<0:
            id5+=id2[id7]
            if id5<=0:
                id6+=1-id5
                id5=1
        elif id5>0:
            id5+=id2[id7]
            if id5>=0:
                id6+=id5+1
                id5=-1
    id5=-1
    id9=1
    for id7 in id8(1, id0):
        if id5<0:
            id5+=id2[id7]
            if id5<=0:
                id9+=1-id5
                id5=1
        elif id5>0:
            id5+=id2[id7]
            if id5>=0:
                id9+=id5+1
                id5=-1
    if id9<id6:
        id4=id9
    else:
        id4=id6

print(id4)