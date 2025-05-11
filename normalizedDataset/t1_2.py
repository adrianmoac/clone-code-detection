from id0 import id1
class id2:
def id3(id4,id5):
id4.id6=id7(id5)
id4.id8=id5
id4.id9=[1]*id5
id4.id10=[0]*id5
def id11(id4,id12):
if id4.id6[id12]==id12:
return id12
else:
id4.id6[id12]=id4.id11(id4.id6[id12])
return id4.id6[id12]
def id13(id4,id12,id14):
id12=id4.id11(id12)
id14=id4.id11(id14)
if id12==id14:
return
if id4.id10[id12]<id4.id10[id14]:
id4.id6[id12]=id14
id4.id8-=1
id4.id9[id14]+=id4.id9[id12]
else:
id4.id6[id14]=id12
id4.id8-=1
id4.id9[id12]+=id4.id9[id14]
if id4.id10[id12]==id4.id10[id14]:
id4.id10[id12]+=1
def id15(id4,id12,id14):
if id4.id11(id12)==id4.id11(id14):
return True
else:
return False
def id16(id4):
return id4.id8
def id17(id4,id12):
return id4.id9[id4.id11(id12)]
id18,id19,id20=map(id21,id22().split())
id23=id2(id18)
id24=id2(id18)
for id25 in id26(id19):
id27,id28=map(id21,id22().split())
id27-=1;id28-=1
id23.id13(id27,id28)
for id25 in id26(id20):
id27,id28=map(id21,id22().split())
id27-=1;id28-=1
id24.id13(id27,id28)
id29=id1(id21)
for id25 in id26(id18):
id29[(id23.id11(id25),id24.id11(id25))]+=1
id30=[0]*id18
for id25 in id26(id18):
id30[id25]+=id29[(id23.id11(id25),id24.id11(id25))]
print (" ").id31(map(id32,id30))