#!/usr/bin/env python3
#-*-coding: utf-8-*-from collections import defaultdict

id0=1000000007

id1,id2,id3=[id4(id5) for id5 in input().split()]
id6=[id4(id5) for id5 in input().split()]

id7=[(id5,id5) for id5 in id6]
id7.id8()


id9=0
id10=None

id11=id12(id13)

id14={}

while True:
    id15=id13(id5[1] for id5 in id7)
    #print(hash(idx_order))
    # if idx_order in dd:
    #     print("seen!")
    #     if dd[idx_order]==turn-1:
    #         pass
    #     else:
    # dd[idx_order]=turn

    # process
    id16=id7[0]
    id17=[(id16[0]*id2, id16[1])]+id7[1:]
    id17.id8()

    id7=id17

    # print(arr)

    id9+=1
    if id9==id3:
        print("\n".id18( [id19(id5[0]%id0) for id5 in id7] ))
        break

    id20=1000
    if id20<=id9<id20+id1:
        id14[id9]=id7
        id15=id13(id5[1] for id5 in id7)
        #print("turn, idxes:", turn, idx_order)

    elif id9>=id20+id1:
        id9=id3

        id21=id9-id20
        id22=id21%id1
        id23=id21//id1

        id24=[(id5[0]*id25(id2,id23,id0))%id0 for id5 in id14[id20+id22]]

        print("\n".id18(id19(id5) for id5 in id24))
        break