from id0 import id1 as id1

def id2(id3,id4):
    if id3>id4:
        return 0
    return id2(id3*2,id4)+1

def id5(id3,id4):
    if id3>id4:
        return 0
    return id5(id3*2+1,id4)+1

def id6(id3,id4):
    return id2(id3,id4)==id5(id3,id4)

def id7(id3,id4):
    if id3>id4:
        return 0
    return id7(2*id3,id4)+1

def id8(id3,id4,id9): # False->Takahashi
#print("x="+str(x)+", n="+str(n)+", phase="+str(phase))
    if id3>id4:
        return ["Takahashi","Aoki"][id9]
    if id3*2+1>id4:
        return id8(id3*2,id4,not id9)
    if id6(id3,id4):
        id10=id7(id3,id4)-1
        #print("dep="+str(dep))
        if id10%2==1:
            return ["Takahashi","Aoki"][id9]
        else:
            return ["Takahashi","Aoki"][not id9]
    id11=id6(id3*2,id4)
    id12=id6(id3*2+1,id4)
    #print("lef="+str(lef)+", rig="+str(rig))
    if id11 and id12:
        id13=id7(id3*2,id4)-1
        id14=id7(id3*2+1,id4)-1
        if id13%2==1:
            return ["Takahashi","Aoki"][id9]
        if id14%2==1:
            return ["Takahashi","Aoki"][id9]
        return ["Takahashi","Aoki"][not id9]
    if id11:
        id10=id7(id3*2,id4) 
    else:
        id10=id7(id3*2+1,id4)
    #print("depth="+str(dep))
    if id10%2==1:
        return ["Takahashi","Aoki"][id9]
    else:
        if id11:
            return id8(id3*2+1,id4,not id9)
        else:
            return id8(id3*2,id4,not id9)

def id15():
    id4=id16(input())
    print(id8(1,id4,False))

if id17=="__main__":
    id15()
