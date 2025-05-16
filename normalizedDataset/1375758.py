import id0 as id1 

class id2:
	def id3(id4, id5):
	 # 負の値はルート (集合の代表) で集合の個数
	 # 正の値は次の要素を表す
		id4.id5=id5
		id4.id6=[-(id7+1) for id7 in id8(id5)]
		id4.id9=[0 for id7 in id8(id5)]

 # 集合の代表を求める O(log(n))
	def id10(id4, id11):
		if id4.id6[id11]<0:
			id4.id5+=-1
			return(id11)
		else:
		 # 経路の圧縮 木の高さ=2
			id4.id6[id11]=id4.id10(id4.id6[id11])
			return(id4.id6[id11])

 # 併合 O(log(n))
	def id12(id4, id11, id13):
		id14=id4.id10(id11)
		id15=id4.id10(id13)
		if id14!=id15:
			if id4.id6[id14]<=id4.id6[id15]:
			 # 小さいほうが個数が多い
				id4.id6[id14]+=id4.id6[id15]
				id4.id6[id15]=id14
			else:
				id4.id6[id15]+=id4.id6[id14]
				id4.id6[id14]=id15
			return(True)
		return(False)

 # チェック
	def id16(id4, id11, id13):
		if id4.id10(id11)==id4.id10(id13):
			return(True)
		else:
			return(False)

 # 確定 O(nlog(n))
	def id17(id4):
		for id7 in id8(id4.id5):
			id4.id9[id7]=id4.id10(id7)
		return(True)


id18=id19(input())
id20,id21=[], []
for id7 in id8(id18):
	id11,id13=map(id19,input().split())
	id20.id22(id11)
	id21.id22(id13)

id23=[]

id24=id1.id25(id20)
id26=id1.id25(id21)
id27=id1.id28(id20)
id29=id1.id28(id21)

for id7 in id8(id18-1):
	id23.id22((id27[id7+1]-id27[id7], id24[id7], id24[id7+1]))
	id23.id22((id29[id7+1]-id29[id7], id26[id7], id26[id7+1]))

id23.id28(id30=lambda id11:id11[0])

id31=id2(id18)
id32=0
for id33, id7, id34 in id23:
	if not id31.id16(id7,id34):
		id31.id12(id7,id34)
		id32+=id33

print(id32)









