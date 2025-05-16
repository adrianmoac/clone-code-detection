import id0
def id1(id2,id3):
    id4=False
    if(id5!=1 and id6!=1):
        if(id7[id2][id3]=="#"):
            if(id2-1>=0 and id3-1>=0 and id7[id2-1][id3-1]=="#"):
                if(id7[id2][id3-1]=="#" and id7[id2-1][id3]=="#"):
                    id4=True
            if(id2-1>=0 and id3+1<id5 and id7[id2-1][id3+1]=="#"):
                if(id7[id2][id3+1]=="#" and id7[id2-1][id3]=="#"):
                    id4=True
            if(id2+1<id6 and id3-1>=0 and id7[id2+1][id3-1]=="#"):
                if(id7[id2][id3-1]=="#" and id7[id2+1][id3]=="#"):
                    id4=True
            if(id2+1<id6 and id3+1<id5 and id7[id2+1][id3+1]=="#"):
                if(id7[id2][id3+1]=="#" and id7[id2+1][id3]=="#"):
                    id4=True
    elif(id6==1 and id5==1):
        id4=True
    elif(id6==1):
        if(id7[id2][id3]=="#"):
            if(id3-1>=0 and id7[id2][id3-1]=="#"):
                id4=True
            if(id3+1<id5 and id7[id2][id3+1]=="#"):
                id4=True
    elif(id5==1):
        if(id7[id2][id3]=="#"):
            if(id2-1>=0 and id7[id2-1][id3]=="#"):
                id4=True
            if(id2+1<id6 and id7[id2+1][id3]=="#"):
                id4=True
    if(id7[id2][id3]=="."):
        id4=True
    return id4


def id8(id2,id3):
    return 0>id2 or id2>=id6 or 0>id3 or id3>=id5 or id7[id2][id3]=="#"


def id9(id2,id3):
    if(id8(id2-1,id3-1) and id8(id2-1,id3) and id8(id2-1,id3+1) and 
       id8(id2,  id3-1) and id8(id2,  id3) and id8(id2,  id3+1) and 
       id8(id2+1,id3-1) and id8(id2+1,id3) and id8(id2+1,id3+1)):
        id10[id2][id3]="#"


id6,id5=[id11(id3) for id3 in input().id12().split()]
id7=[]
id10=[["." for id13 in id14(id5)] for id15 in id14(id6)]

for id15 in id14(id6):
    id7.id16(id17(input().id12()))

for id15 in id14(id6):
    for id13 in id14(id5):
        if(id1(id15,id13)):
           id9(id15,id13) 
        else:
            print("impossible")
            id0.id18()

print("possible")
for id15 in id14(id6):
    print("".id19(id10[id15]))