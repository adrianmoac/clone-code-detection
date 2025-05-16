import id0

id1=id2(id3())

id4=0

for id5 in id6(1, 20):
	id7=[0 for id8 in id6(id5)]

	id9=id5-1
	id10=0

	id11=0

	while id10<id9:
		id7[id11]=10**id9-10**id10
		id11+=1
		id10+=1
		id9-=1

	id12=1
	if id10==id9:
		id12=10

	id13=[0 for id8 in id6(20)]
	id14=[0 for id8 in id6(20)]

	for id8 in id6(0, 10):
		for id15 in id6(0, 10):
			id14[id8-id15]+=1
	for id8 in id6(1, 10):
		for id15 in id6(1, 10):
			id13[id8-id15]+=1

	def id16(id17, id18):
		if id17==id11:
			if id18==id1:
				return 1
			else:
				return 0
		elif id17==0:
			id19=0

			for id8 in id6(-9, 9+1):
				if id20(id18+id8*id7[id17]-id1)<=id7[id17]:
					id19+=id16(id17+1, id18+id8*id7[id17])*id13[id8]

			return id19
		else:
			id19=0

			for id8 in id6(-9, 9+1):
				if id20(id18+id8*id7[id17]-id1)<=id7[id17]:
					id19+=id16(id17+1, id18+id8*id7[id17])*id14[id8]

			return id19

	id4+=id12*id16(0, 0)

print id4