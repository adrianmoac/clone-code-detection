import id0
id1=id2(input())
id3=id4(id4([id5(map(id2, input().split())) for _ in [0]*id1], id6=lambda id7: id7[1], id8=True), id6=lambda id7: id7[0])

class id9:
    id10=["elem_size", "tree_size", "tree", "default"]

    def id11(id12, id13: id14, id15: id2):
        id16=id17(id13)
        id12.id18=1<<id0.id19(id0.id20(id16))
        id12.id21=2*id12.id18
        id12.id22=[id15]*id12.id18+id13+[id15]*(id12.id18-id16)
        id12.id15=id15
        id12.id23()

    def id23(id12)->None:
        id22=id12.id22
        for id24 in id25(id12.id18-1, 0,-1):
            id26, id27=id22[id24<<1], id22[(id24<<1)+1]
            #=====change me=====tree[i]=left if left>right else right

    def id28(id12, id7: id2, id29: id2):
        id30, id31=id7+id12.id18, id29+id12.id18
        id22, id32=id12.id22, id12.id15
        while id30<id31:
            if id30&1:
                #=====change me=====result=tree[l] if tree[l]>result else result
                id30+=1
            if id31&1:
                id31-=1
                #=====change me=====result=tree[r] if tree[r]>result else result
            id30, id31=id30>>1, id31>>1

        return id32

    def id33(id12, id24: id2, id34: id2, id35: id36="="):
        id22=id12.id22
        id37=id12.id18+id24
        if id35=="=":
            id22[id37]=id34
        elif id35=="+":
            id22[id37]+=id34
        elif id35=="?":
            #=====change me=====tree[k]=value if value>tree[k] else tree[k]

        while id37>1:
            id37>>=1
            id26, id27=id22[id37<<1], id22[(id37<<1)+1]
            #=====change me=====tree[k]=left if left>right else right

id38=[0]*(10**5)
id39=id9(id38, 0)
id32=0

for id40, id41 in id3:
    id42=id39.id28(0, id41)
    id39.id33(id41, id42+1, "?")

print(id39.id28(0, 10**5+1))