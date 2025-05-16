id0, id1=map(id2, input().split())
if id0>id1:
    id3=id0
    id0=id1
    id1=id3

if id0%3==0 or id1%3==0:
    print(0)
else:
    id4=id1//3
    id5=id4+1
    id6=id1-id4
    id7=id1-id5
    id8=id0//2
    id9=id0-id8
    id10=id0*id4
    id11=id6*id8
    id12=id6*id9
    id13=id14(id15(id10-id11), id15(id11-id12), id15(id12-id10))
    id16=id0*id5
    id17=id7*id8
    id18=id7*id9
    id19=id14(id15(id16-id17), id15(id17-id18), id15(id18-id16))
    id20=id21(id13, id19)

    id22=id4*id0
    id23=id22
    id24=(id1-2*id4)*id0
    id25=id15(id24-id22)

    id26=id5*id0
    id27=id26
    id28=(id1-2*id5)*id0
    id29=id15(id28-id26)
    
    id3=id0
    id0=id1
    id1=id3
    
    id4=id1//3
    id5=id4+1
    id6=id1-id4
    id7=id1-id5
    id8=id0//2
    id9=id0-id8
    id10=id0*id4
    id11=id6*id8
    id12=id6*id9
    id13=id14(id15(id10-id11), id15(id11-id12), id15(id12-id10))
    id16=id0*id5
    id17=id7*id8
    id18=id7*id9
    id19=id14(id15(id16-id17), id15(id17-id18), id15(id18-id16))
    id30=id21(id13, id19)

    id22=id4*id0
    id23=id22
    id24=(id1-2*id4)*id0
    id31=id15(id24-id22)

    id26=id5*id0
    id27=id26
    id28=(id1-2*id5)*id0
    id32=id15(id28-id26)    

    print(id21(id20, id25, id29, id30, id31, id32))
    