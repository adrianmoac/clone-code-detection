class id0:
	"""Union-Find, 
	http://www.slideshare.net/chokudai/union-find-49066733"""

	def id1(id2, id3):
		id2.id4=[id5 for id5 in id6(id3)]
		id2.id7=[0 for id5 in id6(id3)]

	def id8(id2, id9):
		if(id2.id4[id9]==id9):
			return id9
		else:
			id2.id4[id9]=id2.id8(id2.id4[id9])
			return id2.id4[id9]

	def id10(id2, id9, id11):
		return id2.id8(id9)==id2.id8(id11)

	def id12(id2, id9, id11):
		id9=id2.id8(id9)
		id11=id2.id8(id11)
		if id9==id11:
			return
		if id2.id7[id9]<id2.id7[id11]:
			id2.id4[id9]=id11
		else:
			id2.id4[id11]=id9
			if id2.id7[id9]==id2.id7[id11]:
				id2.id7[id9]=id2.id7[id9]+1
		return

id3, id13, id14=map(lambda id9:id15(id9), input().split())
id16=[0]*id13
id17=[0]*id13
id18=[0]*id14
id19=[0]*id14
for id5 in id6(id13):
	id16[id5], id17[id5]=map(lambda id9:id15(id9), input().split())
for id5 in id6(id14):
	id18[id5], id19[id5]=map(lambda id9:id15(id9), input().split())

id20=id0(id3)
id21=id0(id3)

for id5 in id6(id13):
	id20.id12(id16[id5]-1, id17[id5]-1)
for id5 in id6(id14):
	id21.id12(id18[id5]-1, id19[id5]-1)

id22=[id20.id8(id5) for id5 in id6(id3)]
id23=[id21.id8(id5) for id5 in id6(id3)]

id24=[(id22[id5], id23[id5]) for id5 in id6(id3)]
id25=id24
id24=id26(id24)

id27={}

id28=0
id29=1
id30=id24[0]
for id5 in id6(1, id3):
	if id24[id5]==id30:
		id29=id29+1
	else:
		id27[id30]=id29
		id30=id24[id5]
		id29=1
id27[id30]=id29

for id5 in id6(id3):
	id30=id25[id5]
	print(id27[id30], id31=" ")