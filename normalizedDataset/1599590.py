#!/usr/bin/python

import id0

id1=[0]*10000;id2=[];id3=65530060;id4=[0]*1000;id5=[0]*1000
 
 
id6=100000000

 
id7,id8,id9=map(id10,id0.id11.id12().split(" "))



id13=id0.id11.id12().id14("\n","")

id1=map(id10,id13.split(" "))


def id15(id16,id17):
	global id6,id4,id1,id5,id2
	if id16==id9+1:
		id6=id18(id6,id17)
		return 
	else :
		for id19 in id20(id9):
			if id4[id1[id19]]==0 :
				id4[id1[id19]]=1
				id5[id16]=id1[id19]
				if id16==1:
					id15(id16+1,id17)
				else :
					id15(id16+1,id17+id2[id1[id19]-1][id5[id16-1]-1])
				id4[id1[id19]]=0
	return 
 
 
for id19 in id20(id7+5):
	id2.id21(id20(id7+5))
 
 
for id19 in id20(id7+5):
    for id22 in id20(id7+5):
            id2[id19][id22]=id3


for id19 in id20(id8):
	id23,id24,id25=map(lambda id16: id10(id16),id0.id11.id12().split(" ",3))
	id23-=1;id24-=1;
	id2[id23][id24]=id18(id2[id23][id24],id25)
	id2[id24][id23]=id18(id2[id24][id23],id25)


for id19 in id26(id7):
	for id22 in id26(id7):
		for id27 in id26(id7):
			if id2[id22][id19]+id2[id19][id27]<id2[id22][id27]:
			    id2[id22][id27]=id2[id22][id19]+id2[id19][id27]

id15(1,0)
 
print id6