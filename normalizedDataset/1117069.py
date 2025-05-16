from id0 import id1


def id2(id3, id4):

    for id5 in id6(1, id7(id3)-1):
        # ひつじ
        if id4[id5]==1:
            if id3[id5]=="o":
                id4[id5+1]=id4[id5-1]
            else:
                id4[id5+1]=-1*id4[id5-1]
        # おおかみ
        else:
            if id3[id5]=="o":
                id4[id5+1]=-1*id4[id5-1]
            else:
                id4[id5+1]=id4[id5-1]

    if id4[0]==1:
        if id3[0]=="o":
            id8=id4[1]==id4[-1]
        else:
            id8=id4[1]!=id4[-1]
    # おおかみ
    else:
        if id3[0]=="o":
            id8=id4[1]!=id4[-1]
        else:
            id8=id4[1]==id4[-1]

    if id4[-1]==1:
        if id3[-1]=="o":
            id9=id4[0]==id4[-2]
        else:
            id9=id4[0]!=id4[-2]
    # おおかみ
    else:
        if id3[-1]=="o":
            id9=id4[0]!=id4[-2]
        else:
            id9=id4[0]==id4[-2]

    return id8 and id9

def id10():
    id11=id12(input())
    id13=input()
    id14=[None]*id11
    id14[0]=1
    id14[1]=1
    if id2(id13, id14):
        print(*["S" if id15==1 else "W" for id15 in id14], id16="")
        return

    id14=[None]*id11
    id14[0]=1
    id14[1]=-1
    if id2(id13, id14):
        print(*["S" if id15==1 else "W" for id15 in id14], id16="")
        return

    id14=[None]*id11
    id14[0]=-1
    id14[1]=1
    if id2(id13, id14):
        print(*["S" if id15==1 else "W" for id15 in id14], id16="")
        return

    id14=[None]*id11
    id14[0]=-1
    id14[1]=-1
    if id2(id13, id14):
        print(*["S" if id15==1 else "W" for id15 in id14], id16="")
        return

    print(-1)


if id17=="__main__":
    id10()