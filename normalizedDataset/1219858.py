#!/usr/bin/env python
#-*-coding: utf-8-*-import sys

id0=id1.id2.id3()

id4=id5(id0)
id6=[]

if id4==0:
	print("")
	id7()

for id8 in id9(id4):
	id0=id1.id2.id3()
	id6.id10(id0)

id11=[]
id12={}
id13=0
for id14 in id6:
	id15={}
	if id16(id14)>id13 :
		id13=id16(id14)
	for id17 in id14:
		if not id17 in id15:
			id15[id17]=0
		if id15[id17]==0:
			if not id17 in id12:
				id12[id17]=0
			id12[id17]+=1
			id15[id17]=0
		id15[id17]+=1

	id18(id15.id19(), id20=lambda id21:id21[1], id22=True)
	id11.id10(id15)

id23=[]
id24=["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

id8=0
id25={}
for id26 in id24:
	if id26 in id12 and id12[id26]==id4:
		id25[id26]=0
		id27=id13
		for id28 in id11:
			if id28[id26]<id27 :
				id27=id28[id26]
		id25[id26]=id27

id29=""

for id8 in id9(id16(id24)):
	if not id24[id8] in id25:
		continue
	for id30 in id9(id25[id24[id8]]):
		id29+=id24[id8]

print(id29)