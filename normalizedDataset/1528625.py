def id0():
    """
    2*N, square
    N domino
    domino, 2*1 or 1*2

    [pattern 1]
    aabb
    ccdd
    (a, d) and (b, c)=>2 colors
    (a, d) and c and b=>3 colors
    (c, b) and a and d=>3 colors

    [pattern 2]
    aab
    ccb=>3 colors

    [pattern 3]
    abc
    abc
    2 or 3 colors

    このような塗り方が何通りあるかを
    mod 1000000007 で求めてください．
    """
    id1=id2(input())
    id3=input()
    id4=input()

    id5=1
    id6="f"
    # f irst
    # v ertical
    # h orizontal
    id7=0
    while id7<id1:
        if id3[id7]==id4[id7]:
            # v
            if id6=="f":
                id5*=3
            elif id6=="v":
                id5*=2
            else:
                pass
            id6="v"
            id7+=1
        else:
            # h
            if id6=="f":
                # 3 P 2
                id5*=6
            elif id6=="v":
                id5*=2
            else:
                id5*=3
            id6="h"
            id7+=2

    print(id5%1000000007)

if id8=="__main__":
    id0()