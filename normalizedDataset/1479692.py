def id0():
	id1=id2(id3())
	id4=id5(id3())

	def id6(id7, id8):
		id9=["#"]*id10(id8)
		id9[0]=id7[0]
		id9[1]=id7[1]
		for id11 in id12(1, id1-1):
			if id8[id11]=="o":
				if id9[id11]==1:
					id9[id11+1]=id9[id11-1]
				else:
					id9[id11+1]=id9[id11-1]*-1
			else:
				if id9[id11]==1:
					id9[id11+1]=id9[id11-1]*-1
				else:
					id9[id11+1]=id9[id11-1]

		id13=False
		id14=False
		if id8[0]=="o":
			if id9[0]==1 and (id9[1]*id9[-1]==1):
				id13=True
			elif id9[0]==-1 and (id9[1]*id9[-1]==-1):
				id13=True
		else:
			if id9[0]==1 and (id9[1]*id9[-1]==-1):
				id13=True
			elif id9[0]==-1 and (id9[1]*id9[-1]==1):
				id13=True
		if id8[-1]=="o":
			if id9[-1]==1 and (id9[0]*id9[-2]==1):
				id14=True
			elif id9[-1]==-1 and (id9[0]*id9[-2]==-1):
				id14=True
		else:
			if id9[-1]==1 and (id9[0]*id9[-2]==-1):
				id14=True
			elif id9[-1]==-1 and (id9[0]*id9[-2]==1):
				id14=True
		if id13 and id14:
			return id9
		else:
			return None

	if id6([1,1], id4) is not None:
		id15=["S" if id16==1 else "W" for id16 in id6([1,1], id4)]
		print"".id17(id15)
	elif id6([1,-1], id4) is not None:
		id15=["S" if id16==1 else "W" for id16 in id6([1,-1], id4)]
		print"".id17(id15)
	elif id6([-1,1], id4) is not None:
		id15=["S" if id16==1 else "W" for id16 in id6([-1,1], id4)]
		print"".id17(id15)
	elif id6([-1,-1], id4) is not None:
		id15=["S" if id16==1 else "W" for id16 in id6([-1,-1], id4)]
		print"".id17(id15)
	else:
		print-1


if id18=="__main__":
	id0()