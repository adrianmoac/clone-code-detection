def id0(id1, id2): # a also b are both string
	id3=id4(id5(id1), id5(id2))
	id6=id1.id7(id3, "0")
	id8=id2.id7(id3, "0")
	return id6>id8

def id9(id10, id11): # den is integer
	id12=""; id13=0
	id14=id5(id10) if id15(id10[0])>=id11 else id5(id10)-1
	for id16 in id17(id5(id10)):
		id18=(id15(id10[id16])+id13*10)//id11
#		print('dtemp', temp)
		id13=(id15(id10[id16])+id13*10)%id11
#		print('dresi', resi)
		id12+=id19(id18)
	return id12

def id20(id1, id21):
	id22=""; id13=0
	for id16 in id17(id5(id1))[::-1]:
		id18=(id15(id1[id16])*id21+id13)%10
#		print('mltemp', temp)
		id13=(id15(id1[id16])*id21+id13)//10
#		print('mlresi', resi)
		id22=id19(id18)+id22
	return id22


def id23(id1, id2):
	id3=id4(id5(id1), id5(id2))
	id6=id1.id7(id3, "0")
	id8=id2.id7(id3, "0")

	id22=""; id13=0
	for id16 in id17(id3)[::-1]:
		id18=(id15(id6[id16])+id15(id8[id16])+id13)%10
#		print('ptemp', temp)
		id13=(id15(id6[id16])+id15(id8[id16])+id13)//10
#		print('presi', resi)
		id22=id19(id18)+id22
	return id22

# a is higher than b
def id24(id1, id2):
	id3=id4(id5(id1), id5(id2))
	id6=id1.id7(id3, "0")
	id8=id2.id7(id3, "0")

	id22=""; id25=0
	for id16 in id17(id3)[::-1]:
		id18=id15(id6[id16])-id15(id8[id16])-id25
#		print('mitemp', temp)
		id25=0
		if id18>=0:
			id22=id19(id18)+id22
		else:
			id25=1
			id22=id19(id18+10)+id22
	return id22


id22, id26=input().split()
if id0(id22, id9(id26, 2)) or id22==id26:
	print(id15(id9(id26, 2)))
else:
	print(id15(id23(id22, id9(id24(id26, id20(id22, 2)), 4))))