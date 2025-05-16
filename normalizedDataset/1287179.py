#coding=UTF-8

#ゴールに関係無い袋小路で永パされると、探索が収束しない
#かつ答えがinfでないということで 修正

#表にあるかを尋ねるのが重いので
#データ構造を変えて回避する
id0=input()
id1=id0.split(" ")

id2=id3(id1[0])
id4=id3(id1[1])

#idx番目の都市に繋っている道とコストのタプルを持つリスト
id5=[]
# [] はコピーがしんどいものだったりするので
# 参照でごまかしたりしてくる
# なので1個づつ書いている
for id6 in id7(0,id2,1):
    id5.id8([])


id9=[]
id10=[]

for id6 in id7(0,id4,1):
    id0=input()
    id1=id0.split(" ")
    id5[id3(id1[0])-1].id8((id3(id1[1])-1,id3(id1[2])))

#print(tuuro)
#普通の経路探索のようなことをする
#永パ
id11=[None]*id2 #マイナス点のときもある
id11[0]=0
id12=[0]
id13=0
while id14(id12)>0:
    id13=id13+1
    id15=[]
    for id16 in id12:
        for id17 in id5[id16]:
            id18=id11[id16]+id17[1]
            if id11[id17[0]]==None or id18>id11[id17[0]]:
                id11[id17[0]]=id18
                id15.id8(id17[0])

    id12=id19(id20(id15))
    if id13==id2-1:
        id21=id11[id2-1] #cannot be None
    elif id13==2*id2-1:
        #period must be eqal or less than N
        if id11[id2-1]>id21:
            print("inf")
            break
        else:
            #関係の無い無限ループ
            print(id11[id2-1])
            break
else:
    print(id11[id2-1])