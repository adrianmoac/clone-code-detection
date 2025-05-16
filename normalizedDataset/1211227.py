id0=id1(input())
id2=id1(input())

# S=list("BBAAABA")
# T=list("BBBA")

id3=id4(input())

id5=[]
for id6 in id7(id3):
	id5.id8(id1(map(id4,input().split(" "))))


id9=[0 for id6 in id7(id10(id0))]
id11=[0 for id6 in id7(id10(id0))]

id12=[0 for id6 in id7(id10(id2))]
id13=[0 for id6 in id7(id10(id2))]

if id0[0]=="A":
	id9[0]=1
else:
	id11[0]=1

if id2[0]=="A":
	id12[0]=1
else:
	id13[0]=1

for id6 in id7(1,id10(id0)):
	if id0[id6]=="A":
		id9[id6]=id9[id6-1]+1
		id11[id6]=id11[id6-1]
	else:
		id9[id6]=id9[id6-1]
		id11[id6]=id11[id6-1]+1

for id6 in id7(1,id10(id2)):
	if id2[id6]=="A":
		id12[id6]=id12[id6-1]+1
		id13[id6]=id13[id6-1]
	else:
		id12[id6]=id12[id6-1]
		id13[id6]=id13[id6-1]+1


def id14(id5,id15,id16):
	if id15==0:
		return(id5[id16])
	else:
		return(id5[id16]-id5[id15-1])

for id15,id16,id17,id18 in id5:
	id19=id14(id9,id15-1,id16-1)
	id20=id14(id11,id15-1,id16-1)
	id21=id14(id12,id17-1,id18-1)
	id22=id14(id13,id17-1,id18-1)


	if (id19+id20*2)%3==(id21+id22*2)%3:
		print("YES")
	else:
		print("NO")


















