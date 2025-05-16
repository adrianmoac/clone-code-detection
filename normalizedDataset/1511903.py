import id0
id1=0
id2=False
def id3():
	id1=id4(input())
def id5(id6):
	return ((id6<=id1 and id7(id6)<=id7(id1)) or (id6>id1 and id7(id6)>id7(id1)))

def id8(id6):
 # print(n, N, test_eval(n))
	if id2:
		return id5(id6)
	print("? "+id7(id6))
	id0.id9.id10()
	return input()=="Y"

def id11():
	id12=1
	while not id8(10**id12-1):
		id12+=1
	if id12==1:
		while not id8((10**id12-1)*10**9):
			id12+=1
		while not id8(10**id12-1):
			id12+=1
	return id12

def id13(id14):
	id15=id16(id7(id14)) if id14!=0 else 0
	def id17(id18):
		return id8(id14*10+id18)
	id19=5
	id20=id17(id19)
	if id20:
		id19=7
		id20=id17(id19)
		if id20:
			id19=8
			id20=id17(id19)
			if id20:
				id19=9
				id20=id17(id19)
				return 9 if id20 else 8
			else:
				return 7
		else:
			id19=6
			id20=id17(id19)
			return 6 if id20 else 5
	else:
		id19=2
		id20=id17(id19)
		if id20:
			id19=3
			id20=id17(id19)
			if id20:
				id19=4
				id20=id17(id19)
				return 4 if id20 else 3
			else:
				return 2
		else:
			id19=1
			id20=id17(id19)
			return 1 if id20 else 0
if id2:
	id3()
id21=id11()
# print(nd)
id22=0
for id23 in id24(id21-1):
	id22=id22*10+id13(id22)
id25=[False]*10
id23=0
if id21==1:
	id23=1
while not id8((id22*10+id23)*10):
	id23+=1
id22=id22*10+id23
print("!"+id7(id22))