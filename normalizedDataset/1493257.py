from id0 import id1


# 8近傍（右, 下, 左, 上，右上, 右下, 左下, 左上）
id2=[0,-1, 0, 1, 1,-1,-1, 1]
id3=[1, 0,-1, 0, 1, 1,-1,-1]
def id4(id5):
    id6=[[0]*id7(id5[0]) for _ in id8(id7(id5))]
    for id9 in id8(id7(id5)):
        for id10 in id8(id7(id5[0])):
            if id5[id9][id10]==1:
                for id11 in id8(8):
                    id12=id9+id2[id11]
                    id13=id10+id3[id11]
                    id6[id9][id10]=1
                    if 0<=id12<id7(id5) and 0<=id13<id7(id5[0]):
                        id6[id12][id13]=1
    return id6


def id14(id5):
    id6=[[None]*id7(id5[0]) for _ in id8(id7(id5))]
    for id9 in id8(id7(id5)):
        for id10 in id8(id7(id5[0])):
            if id5[id9][id10]==0:
                for id11 in id8(8):
                    id12=id9+id2[id11]
                    id13=id10+id3[id11]
                    id6[id9][id10]=0
                    if 0<=id12<id7(id5) and 0<=id13<id7(id5[0]):
                        id6[id12][id13]=0

    for id9 in id8(id7(id5)):
        for id10 in id8(id7(id5[0])):
            if id6[id9][id10] is None:
                id6[id9][id10]=1

    return id6


def id15():
    id16, id17=map(id18, input().split())
    id5=[id19(input()) for _ in id8(id16)]
    for id9 in id8(id16):
        for id10 in id8(id17):
            id5[id9][id10]=1 if id5[id9][id10]=="#" else 0

    id6=id14(id5)
    id20=id4(id6)
    if id5!=id20:
        print("impossible")
    else:
        print("possible")
        for id9 in id8(id16):
            for id10 in id8(id17):
                id6[id9][id10]="#" if id6[id9][id10]==1 else "."
        print(*["".id21(id22) for id22 in id6], id23="\n")

if id24=="__main__":
    id15()