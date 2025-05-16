def id0(id1, id2):
    """
    n:nから1,2,3のどれかを引いていき、0にできればOK
    ng:引いていく際にこのリストの要素と一致してはいけない
    """
    if id1 in id2:
        return "NO"

    id3=id4(id2)[::-1]
    id5=id1

    id6=99
    while id6>=0:
        id7=id5
        id8, id9, id10=id7-1, id7-2, id7-3

        id11=["0","0","0"]
        for id12,id13 in id14([id8,id9,id10]):
            if id13 in id3:
                id11[id12]="1"
        id15="".id16(id11)

        if id15=="000":
            if id8==0:
                id5=id8
            elif id9==0:
                id5=id9
            elif id10==0:
                id5=id10
            else:
                id5=id10
        elif id15=="001":
            if id8==0:
                id5=id8
            elif id9==0:
                id5=id9
            else:
                id5=id9
        elif id15=="010":
            if id8==0:
                id5=id8
            elif id10==0:
                id5=id10
            else:
                id5=id10
        elif id15=="011":
            id5=id8
        elif id15=="100":
            if id9==0:
                id5=id9
            elif id10==0:
                id5=id10
            else:
                id5=id10
        elif id15=="101":
            id5=id9
        elif id15=="110":
            id5=id10
        elif id15=="111":
            return "NO"

        if id5==0:
            return "YES"
        id6-=1
    return "NO"

id1=id17(input())
id2=[id17(input()) for id8 in id18(3)]
print(id0(id1, id2))