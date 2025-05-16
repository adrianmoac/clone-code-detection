def id0(id1, id2, id3, id4):
    id5=2**50
    id6=0
    id7=id1*id3
    id8=id1*id4
    id9=id2*(id3+id4)
    id5=id10(id5, id7)
    id5=id10(id5, id8)
    id5=id10(id5, id9)
    id6=id11(id6, id7)
    id6=id11(id6, id8)
    id6=id11(id6, id9)
    return id6-id5

def id12(id1, id2, id3, id4):
    id5=2**50
    id6=0
    id7=id1*(id3+id4)
    id8=id2*(id3)
    id9=id2*id4
    id5=id10(id5, id7)
    id5=id10(id5, id8)
    id5=id10(id5, id9)
    id6=id11(id6, id7)
    id6=id11(id6, id8)
    id6=id11(id6, id9)
    return id6-id5

def id13(id1, id2, id3, id4):
    id5=2**50
    id6=0
    id7=id3*(id1+id2)
    id8=id4*id1
    id9=id4*id2
    id5=id10(id5, id7)
    id5=id10(id5, id8)
    id5=id10(id5, id9)
    id6=id11(id6, id7)
    id6=id11(id6, id8)
    id6=id11(id6, id9)
    return id6-id5

def id14(id1, id2, id3, id4):
    id5=2**50
    id6=0
    id7=id4*(id1+id2)
    id8=id3*id1
    id9=id3*id2
    id5=id10(id5, id7)
    id5=id10(id5, id8)
    id5=id10(id5, id9)
    id6=id11(id6, id7)
    id6=id11(id6, id8)
    id6=id11(id6, id9)
    return id6-id5

def id15(id16, id17, id18):
    id5=2**50
    id6=0
    id5=id10(id5, id16, id17, id18)
    id6=id11(id6, id16, id17, id18)
    return id6-id5

if id19=="__main__":
    id20,id21=map(id22, input().split())
    if (id20>id21):
        id20,id21=id21,id20
    if (id20%3==0 or id21%3==0):
        print (0)
        id23()
    if (id20==2 and id21==2):
        print (1)
        id23()
    id1=id20//2
    id2=id20-id1
    id3=id21//2
    id4=id21-id3
    id24=2**50
    id24=id10(id24, id0(id1, id2, id3, id4))
    id24=id10(id24, id12(id1, id2, id3, id4))
    id24=id10(id24, id13(id1, id2, id3, id4))
    id24=id10(id24, id14(id1, id2, id3, id4))

    for id25 in id26(1, id21+1):
        id1=id20//2
        id2=id20-id1

        id3=id25
        id4=id21-id3

        id27=id4//2
        id28=id4-id27

        id16=id3*id20
        id17=id27*id20
        id18=id28*id20

        id24=id10(id24, id15(id16, id17, id18))
        id16=id3*id20
        id17=id4*id1
        id18=id4*id2
        id24=id10(id24, id15(id16, id17, id18))

    for id29 in id26(1,  id20+1):
        id1=id29
        id2=id20-id1

        id30=id2//2
        id31=id30-id2

        id3=id21//2
        id4=id21-id3


        id16=id1*id21
        id17=id30*id21
        id18=id31*id21

        id24=id10(id24, id15(id16, id17, id18))
        id16=id1*id21
        id17=id2*id3
        id18=id2*id4
        id24=id10(id24, id15(id16, id17, id18))


    print (id24)