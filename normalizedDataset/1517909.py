import id0
from id1 import id2, id3


class id4:
    id5=["elem_size", "tree_size", "tree", "default"]

    def id6(id7, id8: id9, id10: id11):
        id12=id13(id8)
        id7.id14=1<<id0.id15(id0.id16(id12))
        id7.id17=2*id7.id14
        id7.id18=[id10]*id7.id14+id8+[id10]*(id7.id14-id12)
        id7.id19()
        id7.id10=id10

    def id19(id7):
        id18=id7.id18
        for id20 in id21(id7.id14-1, 0,-1):
            id22, id23=id18[id20<<1], id18[(id20<<1)+1]
            id18[id20]=id22 if id22<id23 else id23

    def id24(id7, id25: id11, id26: id11):
        id18=id7.id18
        id27, id28=id25+id7.id14, id26+id7.id14
        id29=id7.id10
        while id27<id28:
            if id27&1:
                id29=id18[id27] if id18[id27]<id29 else id29
                id27+=1
            if id28&1:
                id28-=1
                id29=id18[id28] if id18[id28]<id29 else id29
            id27, id28=id27>>1, id28>>1

        return id29


id30=id11(input())>>1
id31=id32(map(id11, input().split()))

id33=id34("inf")
id35=id4([(id36, id20) for id20, id36 in id37(id31[::2])], (id33, 0))
id38=id4([(id36, id20) for id20, id36 in id37(id31[1::2])], (id33, 0))
id39, id40=id35.id24, id38.id24

id29=[]
id41=id29.id41
id42=[(id39(0, id30), 0, id30, 0)]

while id42:
    id25, id43, id44, id45=id3(id42)
    if id45:
        id46, id47=id40, id39
    else:
        id46, id47=id39, id40
    id26=id47(id25[1]+id45, id44+id45)

    id41(id25[0])
    id41(id26[0])

    id48, id49=id43, id25[1]
    id50, id51=id25[1]+id45, id26[1]
    id52, id53=id26[1]+1-id45, id44

    if id48<id49:
        id2(id42, (id46(id48, id49), id48, id49, id45))
    if id50!=id51:
        id2(id42, (id47(id50, id51), id50, id51, id45^1))
    if id52<id53:
        id2(id42, (id46(id52, id53), id52, id53, id45))

print(" ".id54(map(id55, id29)))