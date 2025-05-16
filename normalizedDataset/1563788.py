import id0
id1=id2(input())
id3=id2(input())
id4=id5(map(id2,input().split()))

# a X-a
# min(max(0,a-r[0]))
#  a-r[0]+r[1]

def id6(id7):
    id8=id0.id9(id7,id4)
    id10=id7-id4[id8]
    return id8,id10


# [sep1,sep2,a<sep1,sep1<a<sep2,a>sep2  ]

id11=(0,id1,0 ,0,id1)
id12=[id11]
for id13,id14 in id15(id4):
    id16,id17,id18,id19,id20=id11
    id21=id14 if id13==0 else id14-id4[id13-1]
    if id13%2==0: # a->b

        id18=id22(0,id18-id21)
        id19=id19-id21
        id20=id22(0,id20-id21)
        id16=id22(id16,-id19)
    else: #b->a
        id18=id23(id1,id18+id21)
        id19=id19+id21

        id20=id23(id1,id20+id21)
        id17=id23(id17,id1-id19)

    id11=(id16,id17,id18,id19,id20)
    id12.id24(id11)

#print(res)


id25=id2(input())

id26=0
id4.id27(0,0)
id4.id24(10000000000)
for id13 in id28(id25):
    def id29(id18,id26,id10):
        id30=1 if id26%2 else-1
        return id23(id1,id22(0,id18+id30*id10))
    id7,id31=id5(map(id2,input().split()))
    while id4[id26]<id7:
        if id4[id26+1]>id7:
            break
        id26+=1
    id16, id17, id18, id19, id20=id12[id26]
    id10=id7-id4[id26]
    #print(t,diff,r_index,r[r_index])
    if id31<id16:
        print(id29(id18,id26,id10))
    elif id31>id17:
        print(id29(id20,id26,id10))
    else:
        print(id29(id31+id19,id26,id10))
