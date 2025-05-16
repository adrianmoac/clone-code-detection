id0,id1=map(id2, input().split())

from id3 import id4
id5=[]

for id6 in id7(id1):
  id8,id9,id10=map(id2, input().split())
  id8,id9=id8-1, id9-1
  id5+=[(id8,id9,id10)]

def id11(id12, id13):
  id14=id15()
  id14.id16(id13)
  id17=[id13]
  while id17:
    id18=id17.id19()
    for id20 in id12[id18]:
      if id20 not in id14:
        id14.id16(id20)
        id17.id21(id20)
  return id14

def id22(id5):
  id12=id4(id23)
  for id8,id9,id10 in id5:
    id12[id8].id21(id9)
  return id12

def id24(id5):
  id12=id4(id23)
  for id8,id9,id10 in id5:
    id12[id9].id21(id8)
  return id12

def id25(id14, id5):
  id26={id18:id6 for id6,id18 in id27(id28(id14))}
  return id29(id14), [(id26[id8],id26[id9],id10) for id8,id9,id10 in id5 if id8 in id14 and id9 in id14]

# only vertices that are reachable from 1 or N
id0,id5=id25(id11(id22(id5), 0), id5)
id0,id5=id25(id11(id24(id5), id0-1), id5)
id30=[id31("-inf")]*id0
id30[0]=0


id6=0
id32=True
while id32:
  if id6==id0:
    print("inf")
    break

  id32=False
  for id8,id9,id33 in id5:
    if id30[id9]<id30[id8]+id33:
      id30[id9]=id30[id8]+id33
      id32=True
  id6+=1
else:
  print(id30[id0-1])