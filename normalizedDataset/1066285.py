# prime_number?

id0=id1(input())

from id2 import id3
from id4 import id5

def id6(id7): # O(sqrt(n))
	id8=id1(id3(id0))
	for id9 in id10(2,id8+1):
		if id7%id9==0:
			return(False)
	return(True)

def id11(id7, id0=1): # O(k+n)未満 (ミラー・ラビンテスト)
	id12=id7
	if id12==2:
		return(True)
	if id12==1 or id12&1==0:
		return(False)
	id13=(id12-1)>>1
	while id13&1==0:
		id13>>=1
	for id9 in id10(id0):
		id14=id5(1,id12-1)
		id15=id13
		id16=id17(id14,id15,id12)
		while id15!=id12-1 and id16!=1 and id16!=id12-1: 
			id16=id17(id16,2,id12)
			id15<<=1
		if id16!=id12-1 and id15&1==0:
			return(False)
	return(True)

def id18(id7, id19=True):
	id8=id1(id3(id0))
	id20=[]
	id21=[]
	for id9 in id10(1,id8+1):
		if id7%id9==0:
			id20.id22(id9)
			if id9<id8:
				id21.id22(id1(id7/id9))
	if id19:
		id20.id23(id24(id21))
		return(id20)
	else:
		id20.id23(id21)
		return(id20)

def id25(id7):
	id8=id1(id3(id0))
	id20=[]
	id9=2
	while id9<id8+1:
		if id7%id9==0:
			id26=0
			while(id7%id9==0):
				id26+=1
				id7=id7/id9
			id20.id22([id9,id26])
			id8=id1(id3(id0))
		id9+=1
	if id7!=1:
		id20.id22([id1(id7),1])
	return(id20)

id20={}
for id9 in id10(id0+1):
	if id11(id9):
		id20[id9]=0

for id9 in id10(1,id0+1):
	for id26 in id25(id9):
		id20[id26[0]]+=id26[1]

id13=1
for id9 in id20.id27():
	id13*=id9+1

id13%=10**9+7
print(id13)









