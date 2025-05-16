

id0,id1=map(id2, input().split())

from id3 import id4
id5=id4(id6)
id7=id4(id6)
id8=[]
for id9 in id10(id1):
  id11,id12,id13=map(id2, input().split())
  id11,id12=id11-1, id12-1
  id8+=[(id11,id12,id13)]
  id5[id11].id14(id12)
  id7[id12].id14(id11)

# only vertices that are reachable from 1 or N
id15=id16()
id15.id17(0)
id18=[0]
while id18:
  id19=id18.id20()
  for id21 in id5[id19]:
    if id21 not in id15:
      id15.id17(id21)
      id18.id14(id21)

id22=id16()
id22.id17(id0-1)
id18=[id0-1]
while id18:
  id19=id18.id20()
  for id21 in id7[id19]:
    if id21 not in id22:
      id22.id17(id21)
      id18.id14(id21)

id23=id15&id22

id8=[(id11,id12,id13) for id11,id12,id13 in id8 if id11 in id23 and id12 in id23]
id24=[id25("-inf")]*id0
id24[0]=0

id26=True
id9=0

id27=False

while id26:
  if id9==id28(id23):
    id27=True
    break

  id26=False
  for id11,id12,id29 in id8:
    if id24[id12]<id24[id11]+id29:
      id24[id12]=id24[id11]+id29
      id26=True
  id9+=1

if id27:
  print("inf")
else:
  print(id24[id0-1])