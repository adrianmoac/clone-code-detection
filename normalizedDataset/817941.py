#!/usr/bin/python3
import id0

id1, id2=input().split()
id1=id3(map(id4, id1))
id2=id4(id2)
id5=id3(map(id4, input().split()))
id6=id3(id7(id8(10))-id7(id5))
id6.id9()

print("a={}".id10(id1), id11=id0.id12)
print("avail={}".id10(id6), id11=id0.id12)

id13=id14(id1)

def id15(id1):
    id16=0
    for id17 in id1:
        id16*=10
        id16+=id17
    return id16

# i桁目を決めたい
# flag: もう超えてる? フラグ
def id18(id1, id19, id20):
    print("a={}, i={}, flag={}".id10(id1, id19, id20), id11=id0.id12)
    if id19==id13:
        return id1

    if id1[id19] in id6:
        return id18(id1, id19+1, id20)
    else:
        if id20:
            id1[id19]=id21(id6)
            return id18(id1, id19+1, id20)

        id22=[id23 for id23 in id6 if id23>id1[id19]]
        if id22:
            id1[id19]=id21(id22)
            return id18(id1, id19+1, True)
        else:
            if id19>0:
                id24=[id23 for id23 in id6 if id23>id1[id19-1]]
                if id24:
                    id1[id19-1]=id21(id24)
                    id1[id19]=id21(id6)
                    return id18(id1, id19+1, True)
                else:
                    raise id25("not impl")
            else:
                id1[id19]=id21(id7(id6)-id7([0]))*10+id21(id6)
                return id18(id1, id19+1, True)






try:
    id26=id18(id1, 0, False)
except id25 as id27:
    print(id27, id11=id0.id12)
    id26=[id21(id7(id6)-id7([0]))]+[id21(id7(id6))]*(id13-1)
    if id15(id26)<id15(id1):
        id26[0]=id21(id7(id6)-id7([0]))*10+id21(id6)


    
print(id26, id11=id0.id12)
id16=id15(id26)

print(id16)