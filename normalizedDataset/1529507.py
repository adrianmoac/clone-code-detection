def id0(*id1): return [id2(id3) for id3, id2 in id4(input().split(), id1)]

id5,=id0(id6)

id7=1000000007

id8=[]
id8.id9(input())
id8.id9(input())

# print(domino[0])
# print(domino[1])

def id10(id11):
    id12=[id11[0]]
    for id13 in id11[1:]:
        if id12[-1]!=id13:
            id12.id9(id13)
    return id12

id8[0]=id10(id8[0])
id8[1]=id10(id8[1])

id14=[]
for id15 in id16(id17(id8[0])):
    id14.id9(id8[0][id15]!=id8[1][id15])
# print(xs)

id18=None
if id14[0]:
    id18=6
else:
    id18=3

id19=id14[0]
for id12 in id14[1:]:
    if id12:
        # T->T
        if id19:
            id18*=3
        else:
            # F->T
            id18*=2
    else:
        # T->F
        if id19:
            id18*=1
        else: # F->F
            id18*=2
    id19=id12

print(id18%id7)

# T->T

# 6*4=24

# 0|1120
# 1|2002

# 0
# 2

# 1
# 0

# 1
# 2

# 2
# 0

# 2
# 1


# F->T

# 3*2=6

# 0|12
# 0|21
# 
# 1|02
# 1|20
# 
# 2|10
# 2|01


# T->F

# 6*1=6

# 0|2
# 1|2

# 0|1
# 2|1

# 1|2
# 0|2

# 1|0
# 2|0

# 2|1
# 0|1

# 2|0
# 1|0

# F->F

# 3*2=6

# 0|12
# 1|02
# 2|01