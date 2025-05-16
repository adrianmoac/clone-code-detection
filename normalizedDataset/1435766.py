#-*-coding: utf-8-*-#Python
import id0

id1=input()
id2=[[] for id3 in id4(id1+1)]

#隣接リスト
for id3 in id4(id1-1):
    id5,id6=id7(map(id8,id9().split()))
    id2[id5].id10(id6)
    id2[id6].id10(id5)

#print adj

#訪問判別フラグ
id11=(id1+1)*[0]

#Stack
id12=[]

#距離
id13=(id1+1)*[0]


#先頭から深さ優先探索
id12.id10(1)
while id14(id12)!=0:
 #print S
	id15=id12.id16()
	#print v
 
	if id11[id15]==0:
		id11[id15]=1
		#print F
		for id17 in id2[id15]:
		 #print "u::"+str(u)
			if id11[id17]==0:
				id12.id10(id17)
				id13[id17]=id13[id15]+1
				#print S

#print dist



#訪問判別フラグ
id11=(id1+1)*[0]

#Stack
id12=[]

#距離
id18=(id1+1)*[0]

#最後から深さ優先探索
id12.id10(id1)
while id14(id12)!=0:
 #print S
	id15=id12.id16()
	#print v
 
	if id11[id15]==0:
		id11[id15]=1
		#print F
		for id17 in id2[id15]:
		 #print "u::"+str(u)
			if id11[id17]==0:
				id12.id10(id17)
				id18[id17]=id18[id15]+1
				#print S

#print dist2



id19=0
id20=0
for id21 in id4(1,id1+1):
	if id13[id21]<=id18[id21]:
		id19+=1
	else:
		id20+=1


if id19>id20:
	print "Fennec"
else:
	print "Snuke"