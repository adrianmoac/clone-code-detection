
id0,id1=map(id2,input().split())

class id3(id4):
	"""
	ベルマンフォード法, O(EV)
	ステータス:distance(list),prev(list),length(int)
	edge=[i, j, cost] のリスト
	"""
	def id5(id6, id7, id8, id9):
		id6.id8=id8
		id6.id9=id9
		id6.id10=[id11("inf") for id12 in id13(id6.id9)]
		id6.id10[id8]=0
		id6.id14=[0 for id12 in id13(id6.id9)]
		id6.id14[id8]=-1
		id6.id15=True
		def id16():
			for id17 in id7:
				id18=id6.id10[id17[0]]+id17[2]
				if id18<id6.id10[id17[1]]:
					id6.id10[id17[1]]=id18 
					id6.id14[id17[1]]=id17[0]
		for id17 in id13(id9-1):
			id16()
		id19=id6.id10[-1]
		for id17 in id13(id9-1):
			id16()
		if id19!=id6.id10[-1]:
			id6.id15=False

	def id20(id6,id21):
		id20=[]
		while(True):
			id20.id22(id6.id14[id21])
			id21=id6.id14[id21]
			if id21==id6.id8:
				break
		id20.id23()
		return(id20)

id24=[]
for id17 in id13(id1):
	id25,id26,id27=map(id2,input().split())
	id24.id22([id25-1,id26-1,-id27])

id28=id3(id24,0,id0)
if (not id28.id15):
	print("inf")
else:
	print(-id28.id10[-1])













