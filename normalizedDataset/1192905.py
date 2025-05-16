import id0
from id1 import id2
id3=10**10
id4=id5(input())
id6=[]
id7=-id3
id8=id3
id9=-id3
id10=id3
id11=-id3
id12=id3
id13=-id3
id14=-id3

for id15 in id16(id4):
	id17, id18, id19=map(id5, input().split())
	id6.id20((id17,id18,id19))
	id7=id21(id7, id17)
	id8=id22(id8, id17)
	id9=id21(id9, id18)
	id10=id22(id10, id18)

id23=0
while id7-id8>10**(-5):
	id23=1
	id24=(id7+id8)/2
	id11=-10**10
	id12=10**10
	for id15 in id16(id4):
		id25=(id6[id15][0]-id24)*id6[id15][2]
		id11=id21(id11, id25)
		id12=id22(id12, id25)

	if id2(id11)>id2(id12):
		id8=id24
	else:
		id7=id24
id26=0
while id9-id10>10**(-5):
	id26=1
	id24=(id9+id10)/2
	id13=-10**10
	id14=10**10
	for id15 in id16(id4):
		id25=(id6[id15][1]-id24)*id6[id15][2]
		id13=id21(id13, id25)
		id14=id22(id14, id25)

	if id2(id13)>id2(id14):
		id10=id24
	else:
		id9=id24
if id23 and id26:
	print(id21(id2(id11), id2(id12), id2(id13), id2(id14)))
else:
	if id23 and not id26:
		print(id21(id2(id11), id2(id12)))
	elif id26 and not id23:
		print(id21(id2(id13), id2(id14)))
	else:
		print(0)