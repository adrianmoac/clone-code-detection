
def id0():
    return map(id1, input().split())


def id2(id3):
    return "\n".id4(map("".id4, id3))

id5, id6=id0()
id7=[]
for _ in id8(id5):
    id7.id9(id10(input()))

id11=[["#" for id12 in id8(id6)] for id13 in id8(id5)]

for id14 in id8(id5):
    for id15 in id8(id6):
        if id7[id14][id15]==".":
            id11[id14][id15]="."
            if id15>0:
                id11[id14][id15-1]="."
            if id15<id6-1:
                id11[id14][id15+1]="."
            if id14>0:
                id11[id14-1][id15]="."
                if id15>0:
                    id11[id14-1][id15-1]="."
                if id15<id6-1:
                    id11[id14-1][id15+1]="."
            if id14<id5-1:
                id11[id14+1][id15]="."
                if id15>0:
                    id11[id14+1][id15-1]="."
                if id15<id6-1:
                    id11[id14+1][id15+1]="."

id16=[["." for id12 in id8(id6)] for id13 in id8(id5)]

for id14 in id8(id5):
    for id15 in id8(id6):
        if id11[id14][id15]=="#":
            id16[id14][id15]="#"
            if id15>0:
                id16[id14][id15-1]="#"
            if id15<id6-1:
                id16[id14][id15+1]="#"
            if id14>0:
                id16[id14-1][id15]="#"
                if id15>0:
                    id16[id14-1][id15-1]="#"
                if id15<id6-1:
                    id16[id14-1][id15+1]="#"
            if id14<id5-1:
                id16[id14+1][id15]="#"
                if id15>0:
                    id16[id14+1][id15-1]="#"
                if id15<id6-1:
                    id16[id14+1][id15+1]="#"

if id2(id16)==id2(id7):
    print("possible")
    print(id2(id11))
else:
    print("impossible")