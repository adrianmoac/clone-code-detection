from id0 import id1

def id2(id3):
    for id4 in id3:
        for id5 in id4:
            print(id5, id6="")
        print()

id7, id8=map(id9, input().split())

id3=[]
for id10 in id11(id7):
    id3.id12(id13(input()))

id14=id1(id3)

for id10 in id11(id7):
    for id15 in id11(id8):
        if id3[id10][id15]==".":
            if id10-1>=0 and id15-1>=0:
                id14[id10-1][id15-1]="."
            if id10-1>=0:
                id14[id10-1][id15    ]="."
            if id10-1>=0 and id15+1<id8:
                id14[id10-1][id15+1]="."
            if id15-1>=0:
                id14[id10    ][id15-1]="."
            if id15+1<id8:
                id14[id10    ][id15+1]="."
            if id10+1<id7 and id15-1>=0:
                id14[id10+1][id15-1]="."
            if id10+1<id7:
                id14[id10+1][id15    ]="."
            if id10+1<id7 and id15+1<id8:
                id14[id10+1][id15+1]="."

id16=id1(id14)

for id10 in id11(id7):
    for id15 in id11(id8):
        if id14[id10][id15]=="#":
            if id10-1>=0 and id15-1>=0:
                id16[id10-1][id15-1]="#"
            if id10-1>=0:
                id16[id10-1][id15    ]="#"
            if id10-1>=0 and id15+1<id8:
                id16[id10-1][id15+1]="#"
            if id15-1>=0:
                id16[id10    ][id15-1]="#"
            if id15+1<id8:
                id16[id10    ][id15+1]="#"
            if id10+1<id7 and id15-1>=0:
                id16[id10+1][id15-1]="#"
            if id10+1<id7:
                id16[id10+1][id15    ]="#"
            if id10+1<id7 and id15+1<id8:
                id16[id10+1][id15+1]="#"

if id16==id3:
    print("possible")
    id2(id14)
else:
    print("impossible")