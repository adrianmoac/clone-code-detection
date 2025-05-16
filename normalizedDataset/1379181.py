id0, id1, id2=map(id3, id4().split())
id5=[]
id6=[]
id7=[]
id8=[]
for id9 in id10(id2): 
  id11, id12, id13, id14=map(id3, id4().split())
  id5.id15(id11)
  id6.id15(id12)
  id7.id15(id13)
  id8.id15(id14)

id16=[]
id17=[]
id18=[]
id19=[]

def id20(id21, id22, id9):
  if id21==0:
    id16.id15((id9, id22))
  elif id21==id0:
    id17.id15((id9, id22))
  elif id22==0:
    id18.id15((id9, id21))
  elif id22==id1:
    id19.id15((id9, id21))


for id9 in id10(id2):
  id20(id5[id9], id6[id9], id9)
  id20(id7[id9], id8[id9], id9)

id16=id23(id16, id24=lambda id21 : id21[1])    
id19=id23(id19, id24=lambda id21 : id21[1])
id17=id23(id17, id24=lambda id21 : id21[1], id25=True)
id18=id23(id18, id24=lambda id21 : id21[1], id25=True)

id26=[]
id26.id27(id16)
id26.id27(id19)
id26.id27(id17)
id26.id27(id18)

id26=map(lambda id21 : id21[0], id26)

id28={}
for id9 in id26:
  if not id9 in id28:
    id28[id9]=0
  id28[id9]+=1

id26=id29(lambda id21 : id28[id21]==2, id26)

id30=[]
for id9 in id26:
  if id31(id30)==0 or id30[-1]!=id9:
    id30.id15(id9)
  else:
    id30.id32()

if id31(id30)==0:
  print("YES")
else:
  print("NO")