#coding=UTF-8

id0=id1(input())
id2=id3(id4(0,id0,1))

#initalize
for id5 in id4(0,id0,1):
    id2[id5]=[]

#input
for id5 in id4(0,id0-1,1):
    id6=input()
    id7=id6.split(" ")
    id8=id1(id7[0])-1
    id9=id1(id7[1])-1

    id2[id8].id10(id9)
    id2[id9].id10(id8)

#path 0 to N-1
#width serach
id11=id3(id4(0,id0,1))
for id5 in id4(0,id0,1):
    id11[id5]=None

id11[0]="F"
id11[id0-1]="S"

id12=[0]
id13=[id0-1]
id14=1
id15=1
id16=1 #for breaking cond
id17=1 #also
id18="F"
while True:
    if id18=="F":
        id19=[]
        for id20 in id12:
            id21=id2[id20]
            for id22 in id21:
                if id11[id22]==None:
                    id19.id10(id22)
                    id11[id22]="F"

        id12=id19
        id16=id23(id19)
        id14=id14+id16
    else:
        id24=[]
        for id20 in id13:
            id21=id2[id20]
            for id22 in id21:
                if id11[id22]==None:
                    id24.id10(id22)
                    id11[id22]="S"

        id13=id24
        id17=id23(id24)
        id15=id15+id17
        
    if id16==0 and id17==0:
        break
    id18="F" if id18=="S" else "S"

#when fennec_haven==sunuke_haven==k
#k+1 th turn fennec 33-4
if id14>id15:
    print("Fennec")
else:
    print("Snuke")