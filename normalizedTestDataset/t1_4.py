class id0:
	"""Union-Find, 
	http://www.slideshare.net/chokudai/union-find-49066733"""

	def id1(id2, id3):
		id2.id4=[id5 for id5 in id6(id3)]

	def id7(id2, id8):
		if(id2.id4[id8]==id8):
			return id8
		else:
			id2.id4[id8]=id2.id7(id2.id4[id8])
			return id2.id4[id8]

	def id9(id2, id8, id10):
		return id2.id7(id8)==id2.id7(id10)

	def id11(id2, id8, id10):
		id8=id2.id7(id8)
		id10=id2.id7(id10)
		# if x==y:
		# 	return
		id2.id4[id8]=id10
		return

id3, id12, id13=map(lambda id8:id14(id8), input().split())
id15=[0]*id12
id16=[0]*id12
id17=[0]*id13
id18=[0]*id13
for id5 in id6(id12):
	id15[id5], id16[id5]=map(lambda id8:id14(id8), input().split())
for id5 in id6(id13):
	id17[id5], id18[id5]=map(lambda id8:id14(id8), input().split())

id19=id0(id3)
id20=id0(id3)

for id5 in id6(id12):
	id19.id11(id15[id5]-1, id16[id5]-1)
for id5 in id6(id13):
	id20.id11(id17[id5]-1, id18[id5]-1)

id21=[id19.id7(id5) for id5 in id6(id3)]
id22=[id20.id7(id5) for id5 in id6(id3)]

id23=[(id21[id5], id22[id5]) for id5 in id6(id3)]
id24=id23
id23=id25(id23)

id26={}

id27=0
id28=1
id29=id23[0]
for id5 in id6(1, id3):
	if id23[id5]==id29:
		id28=id28+1
	else:
		id26[id29]=id28
		id29=id23[id5]
		id28=1
id26[id29]=id28

for id5 in id6(id3):
	id29=id24[id5]
	print(id26[id29], id30=" ")