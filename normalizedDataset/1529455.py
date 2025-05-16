id0=1000000007
id1=id2(input())
id3=input()
id4=input()
id5=1
id6=0 ###前が横だったら0 縦だったら1
id7=0
while id7<id1:
	if id7==0: ###初期処理
		if id1==1:
			id5*=3
			break
		if id1==2:
			id5*=6
			break
		else:
			if id3[0]==id3[1]:
				id5*=6
				id7+=2
				id6=0
			else:
				id5*=3
				id7+=1
				id6=1
	if id7==id1-1:
		if id6==0: ###前が横で次が縦
			id5*=1
			id7+=1
			id6=1
			break
		if id6==1: ###前が縦で次も縦
			id5*=2
			id7+=1
			id6=1
			break
	if id3[id7]==id3[id7+1]:
		if id6==0: ###前が横で次も横
			id5*=3
			id7+=2
			id6=0
			continue
		if id6==1: ###前が縦で次が横
			id5*=2
			id7+=2
			id6=0
			continue
	else:
		if id6==0: ###前が横で次が縦
			id5*=1
			id7+=1
			id6=1
			continue
		if id6==1: ###前が縦で次も縦
			id5*=2
			id7+=1
			id6=1
			continue
print(id5%id0)
