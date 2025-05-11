import id0
id1=id0.id2.id1
id3=id0.id4.id3
id5=id0.id4.id5
def id6(id7):
id3("?%d\n"%id7)
id5()
return id1().id8()=="Y"
def id9(id7):
id3("!%d\n"%id7)
id5()
id10=None
for id11 in id12(10):
if not id6(10**id11):
id10=id11
break
else:
for id11 in id12(10):
if id6(10**id11+1):
id13=10**id11
break
id9(id13)
id14(0)
def id15(id13, id11):
if id11==id10-1:
return not id6(id16("".id17(map(id18, id13)))*10)
return id6(id16("".id17(map(id18, id13))))
id13=[]
for id11 in id12(id10):
id13.id19(0)
id20=(id11<1)-1; id21=10
while id20+1<id21:
id22=(id20+id21)/2
id13[id11]=id22
if id15(id13, id11):
id20=id22
else:
id21=id22
if id11==id10-1:
id13[id11]=id20+1
else:
id13[id11]=id20
id23=id16("".id17(map(id18, id13)))
id9(id23)