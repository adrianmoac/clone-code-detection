#coding=UTF-8
#9マス黒塗りスタンプで塗れるかどうかじゃないかな


def id0(id1,id2):
    if id1<0 or id1>=id3:
        return True
    elif id2<0 or id2>=id4:
        return True
    else:
        return (True if id5[id2][id1]=="#" else False)

def id6(id7):
    for id8 in id9(0,id4,1):
        id10=""
        for id11 in id9(0,id3,1):
            id10=id10+id7[id8][id11]
        print(id10)
            
id12=input()
id13=id12.split(" ")
id4=id14(id13[0])
id3=id14(id13[1])

id5=[]
for id11 in id9(0,id4,1):
    id5.id15(input())

#更地
id16=id17(id9(0,id4,1))
for id8 in id9(0,id4,1):
    id16[id8]=id17(id9(0,id3,1))
    for id11 in id9(0,id3,1):
        id16[id8][id11]="."
for id8 in id9(0,id4,1):
    for id11 in id9(0,id3,1):
        #(x,y)について隣接9マスが入力で全部'#'か場外なら塗る
        for id18 in id9(0,9,1):
            if not id0(id11+id18%3-1,id8+id18//3-1):
                break
        else:
            id16[id8][id11]="#"

#kouhoで塗る
#更地
id19=id17(id9(0,id4,1))
for id8 in id9(0,id4,1):
    id19[id8]=id17(id9(0,id3,1))
    for id11 in id9(0,id3,1):
        id19[id8][id11]="."
        
for id8 in id9(0,id4,1):
    for id11 in id9(0,id3,1):
        if id16[id8][id11]=="#":
            for id18 in id9(0,9,1):
                id20=id11+id18%3-1
                id21=id8+id18//3-1
                if id20>=0 and id20<id3 and id21>=0 and id21<id4:
                    id19[id21][id20]="#"
#print('kouho:')
#printba(kouho)
#print('myon:')
#printba(myon)
#完全再現P
id22="possible"
for id8 in id9(0,id4,1):
    for id11 in id9(0,id3,1):
        if id19[id8][id11]!=id5[id8][id11]:
            id22="im"+id22
            break
    if id22!="possible":
        break

print(id22)
if id22=="possible":
    #print myon
    id6(id16)