import id0 as id1
import id2

id3=id4(input())
id5=id6(map(id4,input().split()))

id7=id5[0]
id8=id5[0]
id9=0

if id8==0:
	id9+=1
	id7=-1 
	id8=id7



for id10 in id5[1:]:
	id8+=id10
	if id7>0 and id8>=0:
		id9+=id8+1
		id8=-1
		id7=-1
	elif id7<0 and id8<=0:
		id9+=-id8+1
		id8=1
		id7=1
	else:
		id7+=id10




id11=id5[0]
id12=id5[0]
id13=0

if id12==0:
	id13+=1
	id11=1 
	id12=1
else:
	id13+=id14(id12)+1
	id11=-id4(id1.id15(id5[0]))
	id12=-id4(id1.id15(id5[0]))


for id16 in id5[1:]:
	id12+=id16
	if id11>0 and id12>=0:
		id13+=id12+1
		id12=-1
		id11=-1
	elif id11<0 and id12<=0:
		id13+=-id12+1
		id12=1
		id11=1
	else:
		id11+=id16

print( id17([id9,id13]) )