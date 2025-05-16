import id0,id1,id2,id3,id4,id5,id6,id7,id8,id9,id10,id11

id9.id12(10**7)
id13=10**10
id14=10**9+7


def id15():
    id16,id17,id18,id19=id20(map(id21, input().split()))
    id22=id21(input())
    id23=[False]*id22
    id24=[id20(map(id21, input().split())) for _ in id25(id22)]
    id26=[[id13]*id22 for _ in id25(id22)]
    id27=[0]*id22
    for id28 in id25(id22):
        id29=id24[id28]
        id30=id0.id31((id16-id29[0])**2+(id17-id29[1])**2)-id29[2]
        if id30<=0:
            id30=0
        id27[id28]=id30

    for id28 in id25(id22-1):
        id29=id24[id28]
        for id32 in id25(id28+1, id22):
            id33=id24[id32]
            id30=id0.id31((id33[0]-id29[0])**2+(id33[1]-id29[1])**2)-id29[2]-id33[2]
            if id30<0:
                id30=0
            id26[id28][id32]=id30
            id26[id32][id28]=id30

    while True:
        id34=-1
        id35=id13
        for id28 in id25(id22):
            if id23[id28]:
                continue
            if id27[id28]<id35:
                id35=id27[id28]
                id34=id28
        if id34<0:
            break

        id36=id26[id34]
        id23[id34]=True
        #print('aai',mi,aai)
        #print('aaik',k)
        for id32 in id25(id22):
            if id36[id32]+id27[id34]<id27[id32]:
                id27[id32]=id36[id32]+id27[id34]

    id37=id0.id31((id16-id18)**2+(id17-id19)**2)
    for id28 in id25(id22):
        id29=id24[id28]
        id30=id0.id31((id18-id29[0])**2+(id19-id29[1])**2)-id29[2]
        if id30<0:
            id30=0
        #print('it',i,t)
        if id37>id27[id28]+id30:
            id37=id27[id28]+id30

    #print('aa',aa)
    #print('k',k)
    return id37


print(id15())