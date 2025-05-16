id0=input()
id1=[id2() for id3 in id4(2)]

id5=[[[0]*3 for id3 in id4(3)] for id6 in id4(id0)]

id7=10**9+7

if id1[0][0]==id1[1][0]:
    for id3 in id4(3):
        id5[0][id3][id3]=1
else:
    for id3 in id4(3):
        for id6 in id4(3):
            if id3==id6:
                continue
            id5[0][id3][id6]=1

for id3 in id4(1, id0):
    if id1[0][id3-1]==id1[0][id3]:
        for id8 in id4(3):
            for id9 in id4(3):
                id5[id3][id8][id9]=id5[id3-1][id8][id9]
    else:
        if id1[0][id3-1]==id1[1][id3-1]:
            if id1[0][id3]==id1[1][id3]:
                # AB
                # AB
                for id10 in id4(3):
                    for id11 in id4(3):
                        if id10==id11:
                            continue
                        id5[id3][id10][id10]+=id5[id3-1][id11][id11]
                        id5[id3][id10][id10]%=id7
            else:
                # AB
                # AC
                for id12 in id4(3):
                    for id10 in id4(3):
                        if id12==id10:
                            continue
                        for id11 in id4(3):
                            if id12==id11 or id11==id10:
                                continue
                            id5[id3][id10][id11]+=id5[id3-1][id12][id12]
                            id5[id3][id10][id11]%=id7
        else:
            if id1[0][id3]==id1[1][id3]:
                # AC
                # BC
                for id12 in id4(3):
                    for id10 in id4(3):
                        if id12==id10:
                            continue
                        for id11 in id4(3):
                            if id12==id11 or id11==id10:
                                continue
                            id5[id3][id12][id12]+=id5[id3-1][id10][id11]
                            id5[id3][id12][id12]%=id7
            else:
                # AC ps
                # BD qt
                for id8 in id4(3):
                    for id9 in id4(3):
                        if id8==id9:
                            continue
                        for id10 in id4(3):
                            if id8==id10:
                                continue
                            for id11 in id4(3):
                                if id10==id11 or id9==id11:
                                    continue
                                id5[id3][id10][id11]+=id5[id3-1][id8][id9]
id13=0
for id3 in id4(3):
    for id6 in id4(3):
        id13+=id5[id0-1][id3][id6]
print id13%id7