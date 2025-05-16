#-*-coding: utf-8-*-import sys


id0=input()


id1=[[] for id2 in id3(id0+1)]

#隣接リスト
for id2 in id3(id0-1):
	id4,id5,id6=id7(map(id8,id9().split()))
	id1[id4].id10((id5,id6))
	id1[id5].id10((id4,id6))

#print a
 

id11,id12=id7(map(id8,id9().split()))


id13=[]
for id2 in id3(id11):
	id13.id10(map(id8, id9().split()))
#print b



#訪問判別フラグ
id14=(id0+1)*[0]

#Stack
id15=[]

#距離
id16=[0 for id2 in id3(id0+1)]

#先頭から深さ優先探索
id15.id10(id12)
id17=0
id18=0
while id19(id15)!=0:
	id18=id15.id20()
 
	if id14[id18]==0:
		id14[id18]=1

		for id21,id22 in id1[id18]:
			if id14[id21]==0:
				id15.id10(id21)
				id16[id21]=id16[id18]+id22
				#print dist

#print dist



for id4 in id3(id19(id13)):

	print id16[ id13[id4][0] ]+id16[ id13[id4][1] ]