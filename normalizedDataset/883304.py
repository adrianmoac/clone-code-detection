# 提出2
def id0(id1):
    for id2 in id3(id4(id1)):
            id5=id1[id2]
            for id6 in id3(id4(id5)):
                id7=id1[id2][id6]
                if id2==0:
                    if id6==0:
                        if "." not in [id1[id2][id6],id1[id2][id6+1],id1[id2+1][id6],id1[id2+1][id6+1]] :
                            id8[id2][id6]="#"
                    elif id6==id9(id10)-1:
                        if "." not in [id1[id2][id6],id1[id2][id6-1],id1[id2+1][id6],id1[id2+1][id6-1]] :
                            id8[id2][id6]="#"
                    else:
                        if "." not in [id1[id2][id6],id1[id2][id6+1],id1[id2][id6-1],id1[id2+1][id6],id1[id2+1][id6+1],id1[id2+1][id6-1]] :
                            id8[id2][id6]="#"
                elif id2==id9(id11)-1:
                    if id6==0:
                        if "." not in [id1[id2][id6],id1[id2][id6+1],id1[id2-1][id6],id1[id2-1][id6+1]] :
                            id8[id2][id6]="#"
                    elif id6==id9(id10)-1:
                        if "." not in [id1[id2][id6],id1[id2][id6-1],id1[id2-1][id6],id1[id2-1][id6-1]] :
                            id8[id2][id6]="#"
                    else:
                        if "." not in [id1[id2][id6],id1[id2][id6+1],id1[id2][id6-1],id1[id2-1][id6],id1[id2-1][id6+1],id1[id2-1][id6-1]] :
                            id8[id2][id6]="#"
                else:
                    if id6==0:
                        if "." not in [id1[id2][id6],id1[id2][id6+1],id1[id2+1][id6],id1[id2+1][id6+1],id1[id2-1][id6],id1[id2-1][id6+1]] :
                            id8[id2][id6]="#"
                    elif id6==id9(id10)-1:
                        if "." not in [id1[id2][id6],id1[id2][id6-1],id1[id2+1][id6],id1[id2+1][id6-1],id1[id2-1][id6],id1[id2-1][id6-1]] :
                            id8[id2][id6]="#"
                    else:
                        if "." not in [id1[id2][id6],id1[id2][id6+1],id1[id2][id6-1],id1[id2+1][id6],id1[id2+1][id6+1],id1[id2+1][id6-1],id1[id2-1][id6],id1[id2-1][id6+1],id1[id2-1][id6-1]] :
                            id8[id2][id6]="#"

def id12(id1):
    for id2 in id3(id4(id1)):
        id5=id1[id2]
        for id6 in id3(id4(id5)):
            id7=id1[id2][id6]
            if id2==0:
                if id6==0:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6+1]="#"
                        id13[id2+1][id6]="#"
                        id13[id2+1][id6+1]="#"
                elif id6==id9(id10)-1:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6-1]="#"
                        id13[id2+1][id6]="#"
                        id13[id2+1][id6-1]="#"
                else:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6-1]="#"
                        id13[id2][id6+1]="#"
                        id13[id2+1][id6]="#"
                        id13[id2+1][id6-1]="#"
                        id13[id2+1][id6+1]="#"
            elif id2==id9(id11)-1:
                if id6==0:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6+1]="#"
                        id13[id2-1][id6]="#"
                        id13[id2-1][id6+1]="#"
                elif id6==id9(id10)-1:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6-1]="#"
                        id13[id2-1][id6]="#"
                        id13[id2-1][id6-1]="#"
                else:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6-1]="#"
                        id13[id2][id6+1]="#"
                        id13[id2-1][id6]="#"
                        id13[id2-1][id6-1]="#"
                        id13[id2-1][id6+1]="#"
            else:
                if id6==0:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6+1]="#"
                        id13[id2+1][id6]="#"
                        id13[id2+1][id6+1]="#"
                        id13[id2-1][id6]="#"
                        id13[id2-1][id6+1]="#"
                elif id6==id9(id10)-1:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6-1]="#"
                        id13[id2+1][id6]="#"
                        id13[id2+1][id6-1]="#"
                        id13[id2-1][id6]="#"
                        id13[id2-1][id6-1]="#"
                else:
                    if id7=="#":
                        id13[id2][id6]="#"
                        id13[id2][id6-1]="#"
                        id13[id2][id6+1]="#"
                        id13[id2+1][id6]="#"
                        id13[id2+1][id6-1]="#"
                        id13[id2+1][id6+1]="#"
                        id13[id2-1][id6]="#"
                        id13[id2-1][id6-1]="#"
                        id13[id2-1][id6+1]="#"
                        

id11,id10=input().split(" ")
id1=[input() for id2 in id3(id9(id11))]
id13=[["." for id6 in id3(id9(id10))] for id2 in id3(id9(id11))]
id8=[["." for id6 in id3(id9(id10))] for id2 in id3(id9(id11))]

if id10=="1" and id11=="1":
    print("possible")
    print(id1[0])
        
elif id10=="1" or id11=="1":
    id14=id9(id10)*id9(id11)
    id1=[id2 for id2 in "".id15(id1)]
    for id2 in id3(id14):
        if id2==0:
            id13[id2]="#" if (id1[id2]=="#" and id1[id2+1]=="#") else "."
        elif id2==id14-1:
            id13[id2]="#" if (id1[id2]=="#" and id1[id2-1]=="#") else "."
        else:
            id13[id2]="#" if (id1[id2]=="#" and id1[id2+1]=="#" and id1[id2-1]=="#") else "."
    for id2 in id3(id14):
        if id2==0:
            if id13[id2]=="#":
                id8[id2]="#"
                id8[id2+1]="#"
        elif id2==id14-1:
            if id13[id2]=="#":
                id8[id2]="#"
                id8[id2-1]="#"
        else:
            if id13[id2]=="#":
                id8[id2]="#"
                id8[id2+1]="#"
                id8[id2-1]="#"
    if id1==id13:
        if id10=="1":
            print("possible")
            for id2 in id3(id4(id13)):
                print(id13[id2])
        else:
            print("possible")
            print("".id15(id13))
    else:
        print("impossible")
else:
    id0(id1)
    id12(id8)
    if id1==["".id15(id2) for id2 in id13]:
        print("possible")
        for id2 in id8:
            print("".id15(id2))
    else:
        print("impossible")