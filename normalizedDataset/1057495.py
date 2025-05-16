id0, id1, id2, id3=map(id4, input().split())

id5=id2-id0
id6=id3-id1

id7=[]

if id6>0:
	id7.id8("U"*id6)
	if id5>0:
		id7.id8("R"*id5)
	else:
		id7.id8("L"*id5)


else:
	print("D"*id6)
	if id5>0:
		id7.id8("R"*id5)
	else:
		id7.id8("L"*id5)

id9="".id10(id7)
#ans2_list_="".join(ans2_list)

id11=[]

#ans_list=ans1_list_+ans2_list_

for id12 in id9:
	if id12=="U":
		id11.id8("D")
	elif id12=="D":
		id11.id8("U")
	elif id12=="R":
		id11.id8("L")
	elif id12=="L":
		id11.id8("R")

id7=id9+"".id10(id11)

id13=[]

if "".id10(id7)[0]=="U":
	id13.id8("L")
	id13.id8("U")
	id13.id8("".id10(id9))
	id13.id8("R")
	id13.id8("D")

elif "".id10(id7)[0]=="R":
	id13.id8("U")
	id13.id8("R")
	id13.id8("".id10(id9))
	id13.id8("D")
	id13.id8("L")

elif "".id10(id7)[0]=="D":
	id13.id8("R")
	id13.id8("D")
	id13.id8("".id10(id9))
	id13.id8("L")
	id13.id8("U")
elif "".id10(id7)[0]=="L":
	id13.id8("D")
	id13.id8("L")
	id13.id8("".id10(id9))
	id13.id8("U")
	id13.id8("R")

id14="".id10(id13)

id15=[]

id16=id7+id14

for id12 in id14:
	if id12=="U":
		id15.id8("D")
	elif id12=="D":
		id15.id8("U")
	elif id12=="R":
		id15.id8("L")
	elif id12=="L":
		id15.id8("R")


id17="".id10(id15)
id16="".id10(id16)+id17

id18=id16
print(id18)