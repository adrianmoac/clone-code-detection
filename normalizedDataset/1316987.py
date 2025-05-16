def id0(id1, id2, id3):
    id4=2**50
    id5=0
    id4=id6(id4, id1, id2, id3)
    id5=id7(id5, id1, id2, id3)
    return id5-id4

if id8=="__main__":
    id9,id10=map(id11, input().split())
    if (id9>id10):
        id9,id10=id10,id9
    if (id9%3==0 or id10%3==0):
        print (0)
        id12()

    id13=2**50
    for id14 in id15(1, id10+1):
        id16=id9//2
        id17=id9-id16

        id18=id14
        id19=id10-id18

        id20=id19//2
        id21=id19-id20

        id1=id18*id9
        id2=id20*id9
        id3=id21*id9

        id13=id6(id13, id0(id1, id2, id3))
        id1=id18*id9
        id2=id19*id16
        id3=id19*id17
        id13=id6(id13, id0(id1, id2, id3))

    for id22 in id15(1,  id9+1):
        id16=id22
        id17=id9-id16

        id23=id17//2
        id24=id23-id17

        id18=id10//2
        id19=id10-id18


        id1=id16*id10
        id2=id23*id10
        id3=id24*id10

        id13=id6(id13, id0(id1, id2, id3))
        id1=id16*id10
        id2=id17*id18
        id3=id17*id19
        id13=id6(id13, id0(id1, id2, id3))


    print (id13)