id0,id1,id2,id3=id4(map(id5,input().split()))
id6=id5(input())
id7=[]
for id8 in id9(id6):
	id7.id10(id4(map(id5,input().split())))

# xs,ys,xt,yt=[-1000000000,-1000000000, 1000000000, 1000000000]
# N=1
# a=[[-1000000000, 1000000000, 1]]

class id11(id12):
	"""
	ダイクストラ法,(N^2)
	ステータス:distance(list),prev(list),size(int)
	distancemap[i][j]->Distance of edge i to j
	"""
	def id13(id14, id15, id16):
		id14.id16=id16
		id14.id17=id18(id15)
		id14.id19=[id20("inf") for id21 in id9(id14.id17)]
		id14.id19[id16]=0
		id14.id22=[0 for id21 in id9(id14.id17)]
		id14.id22[id16]=-1
		id23=id4(id9(id14.id17))
		id23.id24(id16)
		id25=id16
		while(id23!=[]):
			id26=0
			id27=id20("inf")
			for id8 in id23:
				id28=id15[id25][id8]+id14.id19[id25]
				id14.id19[id8]=id29(id28, id14.id19[id8])
				if id14.id19[id8]<=id27:
					id27=id14.id19[id8]
					id26=id8
			id23.id24(id26)
			id14.id22[id26]=id25
			id25=id26

	def id30(id14,id31):
		id30=[]
		while(True):
			id30.id10(id14.id22[id31])
			id31=id14.id22[id31]
			if id31==id14.id16:
				break
		id30.id32()
		return(id30)

import id33
def id34(id0,id1,id2,id3,id6,id7):
	id7.id35(0,[id0,id1,0])
	id7.id10([id2,id3,0])
	def id19(id8,id36):
		id37=id7[id8][0]
		id38=id7[id8][1]
		id39=id7[id8][2]
		id40=id7[id36][0]
		id41=id7[id36][1]
		id42=id7[id36][2]
		id43=id33.id44((id37-id40)*(id37-id40)+(id38-id41)*(id38-id41))-id39-id42
		if id43<0:
			id43=0
		return(id43)
	id15=[[0 for id21 in id9(id6+2)] for id21 in id9(id6+2)]
	for id8 in id9(id6+2):
		for id36 in id9(id6+2):
			if id8>id36:
				id15[id8][id36]=id15[id36][id8]
			else:
				id15[id8][id36]=id19(id8,id36)

	id43=id11(id15, 0)
	return(id43.id19.id45())

print(id34(id0, id1, id2, id3, id6, id7))