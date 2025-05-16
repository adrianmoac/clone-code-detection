id0=id1().split(" ")
id2=id3(id0[0])
id4=id3(id0[1])

id5=[]

for id6 in id7(id2):
	id5.id8(id1())


id9=[]

for id6 in id7(id2):
	id10=""
	for id11 in id7(id4):
		if id5[id6][id11]=="#":
			id12=False
			for id13 in id7(3):
				for id14 in id7(3):

					if (id11+(id14-1)>=0) and (id11+(id14-1)<id4) and (id6+(id13-1)>=0) and (id6+(id13-1)<id2) and (id5[id6+id13-1][id11+id14-1]=="."):
						id12=True
			if id12==True:
				id10+="."
			else:
				id10+="#"

		else:
			id10+="."
	id9.id8(id10)


##############################


id15=[]

for id6 in id7(id2):
	id10=""
	for id11 in id7(id4):
		if id9[id6][id11]==".":
			id12=False
			for id13 in id7(3):
				for id14 in id7(3):
					if (id11+(id13-1)>=0) and (id11+(id13-1)<id4) and (id6+(id14-1)>=0) and (id6+(id14-1)<id2) and (id9[id6+(id14-1)][id11+(id13-1)]=="#"):
						id12=True
						break
			if id12==True:
				id10+="#"
			else:
				id10+="."

		else:
			id10+="#"
	id15.id8(id10)

#################################

id12=True
for id6 in id7(id2):
	for id11 in id7(id4):
		if id5[id6][id11]!=id15[id6][id11]:
			id12=False
			break

if id12==True:
	print "possible"
	for id6 in id7(id2):
		print id9[id6]
else:
	print "impossible"


