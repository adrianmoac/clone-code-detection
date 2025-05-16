id0, id1=map(id2, input().split())
id3=[id2(id4) for id4 in input().split()]
id5=[id2(id4) for id4 in id6(10)]
id7=id8(id0)
id7=id9(id7)

#print(lis_n)

# 使用可能な数一覧
for id4 in id3:
    id5.id10(id4)

#print(ablenum)

id11=-1

# max(ablenum)より大きい桁があるかどうか
for id4 in id6(id12(id7)):
    id13=id12(id7)-id4-1
    if(id2(id7[id13])>id14(id5)):
        id11=id13
        break

#  max(ablenum)より大きい桁があれば
if(id11!=-1):
    id15=1
    #  桁を増やす必要があるかどうか確認
    for id4 in id6(id11-1, 0):
        # nの桁より大きい数字がablenumに存在していれば桁を増やす必要はない
        if(id2(id7[id4])<id14(id5)):
            id15=0
            break
else:
    id15=0

#print("bigdigit:{0} increace:{1}".format(flag_bigdigit, flag_increaseDights))

id16=""
# 桁を増やす必要があるならば
if(id15==1):
    for id4 in id6(id12(id7)+1):
        # 一桁目は0以外の最も小さな数
        if(id4==0):
            id17=id18(id5)
            if(id17==0):
                id17=id5[1]
            id16+=id8(id17)
        # 2桁目以降は最も小さい数
        else:
            id17=id18(id5)
            id16+=id8(id17)
# 桁を増やす必要がなければ、各桁の数字以上の最も小さい数を使う
else:
    id19=0
    for id4 in id6(id12(id7)):
        if(id19==0):
            id17=id18(id5)
            # その桁以上の数になるまで大きくする
            id20=0
            while id17<id2(id7[id4]):
                #print("mnum:{0} j:{1}".format(mnum, j))
                id20+=1
                id17=id5[id20]
            if(id17>id2(id7[id4])):
                id19=1
            id16+=id8(id17)
        else:
            id17=id18(id5)
            id16+=id8(id17)

print(id16)