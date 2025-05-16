

def id0():
    id1=id2(input())
    id3=[id4(map(id2, input().split())) for id5 in id6(id1)]
    id7=id2(input())
    id8=[id2(input()) for id5 in id6(id7)]

    id9={}

    for id10 in id6(1, id1+1):
        for id11 in id6(1, id1+1):

            id12=id13(id10)+","+id13(id11)

            if id10==1 and id11==1:
                id9[id12]=id3[0][0]
                continue

            if id10==1:
                id14=id13(id10)+","+id13(id11-1)
                id9[id12]=id9[id14]+id3[0][id11-1]
                continue

            if id11==1:
                id14=id13(id10-1)+","+id13(id11)
                id9[id12]=id9[id14]+id3[id10-1][0]
                continue

            id15=id13(id10)+","+id13(id11-1)
            id16=id13(id10-1)+","+id13(id11)
            id17=id13(id10-1)+","+id13(id11-1)
            id18=0
            id18+=id9[id15]
            id18+=id9[id16]
            id18-=id9[id17]
            id18+=id3[id10-1][id11-1]
            id9[id12]=id18

    #OK
    #print(scores_from_top_left)

    id19={}

    for id10 in id6(1, id1+1):
        for id11 in id6(1, id1+1):

            id12=id10*id11
            id20=0

            for id21 in id6(id10, id1+1):
                for id22 in id6(id11,id1+1):
                    id23=0

                    if id21==id10 and id22==id11:
                        id23=id9[id13(id21)+","+id13(id22)]
                    elif id21==id10:
                        id24=id9[id13(id21)+","+id13(id22)]
                        id25=id9[id13(id21)+","+id13(id22-id11)]
                        id23=id24-id25

                    elif id22==id11:
                        id24=id9[id13(id21)+","+id13(id22)]
                        id25=id9[id13(id21-id10)+","+id13(id22)]
                        id23=id24-id25
                    else:

                        id14=id13(id21)+","+id13(id22)
                        id15=id13(id21-id10)+","+id13(id22)
                        id16=id13(id21)+","+id13(id22-id11)
                        id17=id13(id21-id10)+","+id13(id22-id11)

                        id23=id9[id14]
                        id23-=id9[id15]
                        id23-=id9[id16]
                        id23+=id9[id17]

                    if id23>id20:
                        id20=id23

            if id12 not in id19:

                id19[id12]=id20
            else:
                if id19[id12]<id20:
                    id19[id12]=id20

    #print(max_scores)
    for id5 in id6(id7):

        id20=0

        for id26 in id6(1, id8[id5]+1):
            if id26 not in id19.id27():
                continue
            if id19[id26]>id20:
                id20=id19[id26]
        print(id20)




if id28=="__main__":
    id0()