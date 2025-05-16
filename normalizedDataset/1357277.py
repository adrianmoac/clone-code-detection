def id0():
	id1=id2=0
	id3=id4=1000111000
	for id5 in id6(id7):
		id1=id8(id1, id9[id5])
		id3=id10(id3, id9[id5])
		id2=id8(id2, id11[id5])
		id4=id10(id4, id11[id5])
	return (id1-id3)*(id2-id4)

def id12(id3):
	id4=id10(id9)
	id2=id8(id11)
	id1=0
 
	for id5 in id6(id7):
		if id11[id5]<id3:
			return 2**60
		if id3<=id9[id5]:
			id1=id8(id1, id9[id5])
		else:
			id1=id8(id1, id11[id5])
	return (id1-id3)*(id2-id4)

def id13():
	id14=2**60
	for id3 in id9:
		id14=id10(id14, id12(id3))
	for id3 in id11:
		id14=id10(id14, id12(id3))
	return id14

def id15():
	id14=2**60
	id16=id9+id11
	id16.id17()
	id4=id10(id9)
	id2=id8(id11)
	id18=id10(id11)
 
	id19=0
	for id3 in id16:
		if id18<id3:
			break
		while id19<id7 and id20[id19][0]<id3:
			id19+=1
		id1=id8(id21[id19], id22[id19+1])
		id14=id10(id14, (id1-id3)*(id2-id4))
	return id14

id7=id23(id24())

id9=[0]*id7
id11=[0]*id7
id20=[(0,0)]*id7
id25=id26=0
for id5 in id6(id7):
	id9[id5],id11[id5]=map(id23, id24().split())
	id9[id5],id11[id5]=id10(id9[id5],id11[id5]),id8(id9[id5],id11[id5])
	id20[id5]=id9[id5],id11[id5]
	if id9[id5]<id9[id25]:
		id25=id5
	if id11[id26]<id11[id5]:
		id26=id5
id20.id17()
id21=[0]*(id7+2)
id22=[0]*(id7+2)
id27=id18=0
for id5 in id6(id7):
	id18=id8(id18, id20[id5][1])
	id21[id5+1]=id18

for id5 in id6(id7-1,-1,-1):
	id27=id8(id27, id20[id5][0])
	id22[id5+1]=id27

id28=id0()
if id25!=id26:
	id28=id10(id28, id15())
print id28