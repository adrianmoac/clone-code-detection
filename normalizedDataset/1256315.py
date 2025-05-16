import id0
from id1 import id2
 
id3=1<<30
 
def id4():
    id5=id6(id0.id7.id8())
 
    # r_max=MAX, b_min=MIN にしたとき
 
    id9=id10=0
    id11=id12=id3

    id13=[]
 
    for id14 in id15(id5):
        id16, id17=map(id6, id0.id7.id8().split())

        if id16>id17:
            id16, id17=id17, id16

        id13.id18((id16, id17))

        id9=id19(id9, id17)
        id11=id20(id11, id17)
        id10=id19(id10, id16)
        id12=id20(id12, id16)
 
    id21=(id9-id11)*(id10-id12)
 
    # r_max=MAX, r_min=MIN にしたとき
 
    id22=(id9-id12)

    id13.id23(id24=id2(0))

    id12=id13[0][0]
    id10=id13[-1][0]

    id25=id3

    id26=id10-id12
 
    for id14 in id15(id5-1):
        if id13[id14][1]==id9:
            break
        id25=id20(id25, id13[id14][1])

        id12=id20(id13[id14+1][0], id25)
        id10=id19(id10, id13[id14][1])

        id26=id20(id26, id10-id12)
 
    id22*=id26
 
    id27=id20(id21, id22)
 
    print(id27)
 
if id28=="__main__":
    id4()