id0=10**9+7
id1=[id2(id3)-1 for id3 in input().split()]
id4=[id2(id3)   for id3 in input().split()]
id5=[id2(id3)   for id3 in input().split()]
id4.id6()
id5.id6()

id7=[id4[id3+1]-id4[id3] for id3 in id8(id1[0])]
id9=[id5[id3+1]-id5[id3] for id3 in id8(id1[1])]

id10=[0 for id3 in id8(id1[0])]
id11=[0 for id3 in id8(id1[1])]

if id1[0]%2==0:
	for id3 in id8(id1[0]):
		id12=id13(id3,id1[0]-id3-1)
		id12+=1
		id10[id3]+=id2(id12*(id12+1)/2)
		#print(usingX)
		id10[id3]+=id12*id2(id1[0]/2-id12)
		#print(usingX)
		id10[id3]*=2
		#print()
else:
	for id3 in id8(id1[0]):
		id12=id13(id3,id1[0]-id3-1)
		id12+=1
		id10[id3]+=id2(id12*(id12+1)/2)
		id10[id3]+=id12*id2((id1[0]-1)/2-id12)
		id10[id3]*=2
  
		id10[id3]+=id12
 #temp=int((L[0]-1)/2)
 #usingX[temp]-=(temp+1)*2


if id1[1]%2==0:
	for id3 in id8(id1[1]):
		id12=id13(id3,id1[1]-id3-1)
		id12+=1
		id11[id3]+=id2(id12*(id12+1)/2)
		#print(usingY)
		id11[id3]+=id12*id2(id1[1]/2-id12)
		#print(usingY)
		id11[id3]*=2
		#print()
else:
	for id3 in id8(id1[1]):
		id12=id13(id3,id1[1]-id3-1)
		id12+=1
		id11[id3]+=id2(id12*(id12+1)/2)
		id11[id3]+=id12*id2((id1[1]-1)/2-id12)
		id11[id3]*=2
  
		id11[id3]+=id12
 #temp=int((L[1]-1)/2)
 #usingY[temp]-=(temp+1)*2	

#print(usingX)
#print(usingY)
for id3 in id8(id1[0]):
	id7[id3]*=id10[id3]
for id14 in id8(id1[1]):
	id9[id14]*=id11[id14]
id15=id16(id7)*id16(id9)
print(id15%id0)