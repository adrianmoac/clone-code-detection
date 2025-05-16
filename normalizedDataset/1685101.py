id0,id1=map(id2,input().split())
id3=[]
id4=[]
for id5 in id6(id0):
	id7,id8=id9((map(id2,input().split())))
	id3.id10((id7,id8))
	id4.id10(id8)
id3.id11()
id4.id11()

id12={}
id13=0
for id7,id8 in id3:
	if id13 in id12:
		if id12[id13]!=id7:
			id13+=1
			id12[id13]=id7
	else:
		id12[id13]=id7

id14={}
id13=0
for id8 in id4:
	if id13 in id14:
		if id14[id13]!=id8:
			id13+=1 
			id14[id13]=id8
	else:
		id14[id13]=id8

id15=[[0 for id16 in id6(id17(id14))] for id5 in id6(id17(id12))]

for id18,id19 in id12.id20():
	for id21,id22 in id14.id20():
		id23=1 if (id19,id22) in id3 else 0
		if id18==0 and id21==0:
			id15[id18][id21]+=id23
		elif id18==0 and id21>0:
			id15[id18][id21]+=id15[id18][id21-1]+id23
		elif id18>0 and id21==0:
			id15[id18][id21]+=id15[id18-1][id21]+id23
		else:
			id15[id18][id21]+=id15[id18-1][id21]+id15[id18][id21-1]-id15[id18-1][id21-1]+id23

id24=-1
for id25 in id6(id17(id12)):
	for id26 in id6(id25+1,-1,-1):
		for id27 in id6(id17(id14)):
			for id28 in id6(id27+1,-1,-1):
				id29=id15[id25][id27]
				if id26>0:
					id29-=id15[id26-1][id27]
				if id28>0:
					id29-=id15[id25][id28-1]
				if id26>0 and id28>0:
					id29+=id15[id26-1][id28-1]
				if id29>=id1:
					id30=(id12[id25]-id12[id26])*(id14[id27]-id14[id28])
					if id24<0:
						id24=id30
					else:
						id24=id31(id24, id30)
					break
print(id24)