id0=id1(input())
id2=id3(input())
id4=id3(input())
id5, id6=0, 0
id7=1

while (id6<id8(id2)-1):
	if(id5==0):
		if(id2[id6]==id2[id6+1]):
			id7=id7*6
			id5=1
			id6+=2
  
		else:
			id7=id7*3
			id5=2
			id6+=1

			if(id6==id8(id2)-1):
				id7=id7*2

		continue

	if(id5==1):
		if(id2[id6]==id2[id6+1]):
			id7=id7*3
			id5=1
			id6+=2

		else:
			id7=id7*1
			id5=2
			id6+=1

			if(id6==id8(id2)-1):
				id7=id7*2


		continue

	if(id5==2):
		if(id2[id6]==id2[id6+1]):
			id7=id7*2
			id5=1
			id6+=2

		else:
			id7=id7*2
			id5=2
			id6+=1

			if(id6==id8(id2)-1):
				id7=id7*2

		continue


if(id8(id2)==1):
	print(3)

else:
	print(id7%1000000007)