#coding=UTF-8

# y/x 0 1 2 3
#   0 . . . .
#   1 . . . .
#   2 . . . .
#   3 . . . .
#

def id0(id1,id2):
#    print(lst)
    if id1==0:
        return id2
    else:
        #find least y s.t. there in no quin
        for id3 in id4(0,8,1):
            if id5[id3]==False:
                id6=id3
                break

        for id7 in id4(0,8,1):
            if id8([id9[id7],id10[id7+id6],id11[id7-id6+7]]):
                pass
            else:
                #place
                id5[id6]=True
                id9[id7]=True
                id10[id7+id6]=True
                id11[id7-id6+7]=True
                id12=id0(id1-1,id2+[(id7,id6)])
                if id12!=None:
                    return id12
                else:
                    #unplace
                    id5[id6]=False
                    id9[id7]=False
                    id10[id7+id6]=False
                    id11[id7-id6+7]=False

        return None


id13=[]
for id7 in id4(0,8,1):
    id14=input()
    id13.id15(id14)

id9=[False]*8
id5=[False]*8

id10=[False]*15
id11=[False]*15

id16=False

for id7 in id4(0,8,1):
    for id3 in id4(0,8,1):
        if id13[id3][id7]=="Q":
            if id8([id9[id7],id5[id3],id10[id7+id3],id11[id7-id3+7]]):
                id16=True
            else:
                id9[id7]=True
                id5[id3]=True
                id10[id7+id3]=True
                id11[id7-id3+7]=True

if id16:
#    print('Broken')
    print("No Answer")
else:
    id12=id0(8-3,[])
#    print('kaeshi:{}'.format(kaeshi))
    if id12!=None:
        for id3 in id4(0,8,1):
            id17=""
            for id7 in id4(0,8,1):
                if id13[id3][id7]=="Q" or ((id7,id3) in id12):
                    id17+="Q"
                else:
                    id17+="."
            print(id17)
    else:
        print("No Answer")
        
    