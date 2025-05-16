id0=id1(id2())
id3=id2()

def id4():
    for id5 in id6(id0-2):
        id7=id3[id5]
        if id8[id5]==0: # hituji
            if id7=="o":
                id8[id5+1]=id8[id5-1]
            else:
                id8[id5+1]=id8[id5-1]^1
        else: # ookami
            if id7=="o":
                id8[id5+1]=id8[id5-1]^1
            else:
                id8[id5+1]=id8[id5-1]

def id9(id5):
    id10=False
    if id8[id5]==0:
        if id3[id5]=="o" and id8[id5-1]==id8[(id5+1)%id0]:
            id10=True
        elif id3[id5]=="x" and id8[id5-1]!=id8[(id5+1)%id0]:
            id10=True
    else:
        if id3[id5]=="o" and id8[id5-1]!=id8[(id5+1)%id0]:
            id10=True
        elif id3[id5]=="x" and id8[id5-1]==id8[(id5+1)%id0]:
            id10=True
    return id10

def id11():
    id12=""
    for id13 in id8:
        if id13==0:
            id12+="S"
        else:
            id12+="W"
    return id12

id8=[0]*id0

id8[-1]=0 # hituji
id8[0]=0 # hituji
id4()
if id9(id0-2) and id9(id0-1):
    print id11()
    id14()

id8[-1]=0 # hituji
id8[0]=1 # ookami
id4()
if id9(id0-2) and id9(id0-1):
    print id11()
    id14()

id8[-1]=1 # ookami
id8[0]=1 # ookami
id4()
if id9(id0-2) and id9(id0-1):
    print id11()
    id14()

id8[-1]=1 # ookami
id8[0]=0 # hituji
id4()
if id9(id0-2) and id9(id0-1):
    print id11()
    id14()

print-1