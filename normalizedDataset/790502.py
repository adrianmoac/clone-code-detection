import id0


def id1():
    id2, id3=map(id4, input().split())
    id5=[]
    for id6 in id7(id3):
        id8, id9=map(id4, input().split())
        id5.id10((id8-1, id9-1))
    return id2, id3, id5

def id11(id2, id3, id5):
    id12=0
    for id13 in id0.id14(id15(id7(id2))):
        if id16(id13, id5):
            id12+=1
    return id12

def id16(id13, id5):
    id17=[0]*id18(id13)
    for id19, id20 in id21(id13):
        id17[id20]=id19
    for id8, id9 in id5:
        if id17[id8]>id17[id9]:
            return False
    return True


def id22(id2):
    id23=[[] for id19 in id7(1<<id2)]
    for id24 in id7(1<<id2):
        id25=id23[id24]
        for id26 in id7(id2):
            if id24&(1<<id26):
                id25.id10(id26)
    return id23

def id27(id2, id3, id5):
    """
    faster[x][y]: pos(x)<pos(y) なら 1 pos(x)>pos(y) なら-1, 不明なら0 
    Es[x]=[y1, y2...]: pos(x)<pos(yi) である yi のリスト 
    """
    id23=id22(id2)
    id28=[[0]*id2 for id19 in id7(id2)]
    id29=[[] for id19 in id7(id2)]
    for id8, id9 in id5:
        id28[id8][id9]=1
        id28[id9][id8]=-1
        id29[id8].id10(id9)
    for id8 in id7(id2):
        id30=[id8]
        id31=[False]*id2
        id31[id8]=True
        while id30:
            id32=[]
            for id33 in id30:
                for id34 in id29[id33]:
                    if id31[id34]:
                        continue
                    id31[id34]=True
                    id32.id10(id34)
                    id28[id8][id34]=1
                    id28[id34][id8]=-1
            id30=id32
    id35=[0]*(1<<id2)
    for id24 in id7(1, 1<<id2):
        if id18(id23[id24])==1:
            id35[id24]=1
            continue
        id36=id23[id24]
        for id37 in id36:
            id38=id28[id37]
            for id39 in id36:
                if id38[id39]==-1:
                    break
            else:
                id35[id24]+=id35[id24-(1<<id37)]
    return id35[(1<<id2)-1]

        
id2, id3, id5=id1()
print(id27(id2, id3, id5))