# 結局は木+1辺
from id0 import id1
import id2 as id3

id4=id5(input())
id6=id7(map(lambda id8:id5(id8)-1,input().split()))
id9=[0]*id4
for id10 in id6:
  id9[id10]+=1

id11=id1(id7)

id12=[id10 for id10 in id13(id4) if id9[id10]==0]
id14=[None]*id4

while id12:
  id15=id12.id16()

  id17=id11[id15]
  del id11[id15]

  id3.id18(id17)
  id19=0
  while id17:
    id20=id3.id21(id17)
    if id19<id20:
      break
    else:
      id19+=(id19==id20)
  
  id14[id15]=id19
  id22=id6[id15]
  id11[id22].id23(id19)
  id9[id22]-=1
  if id9[id22]==0:
    id12.id23(id22)

# cycle check
try:
  id24=id9.id25(1)
except id26:
  print("POSSIBLE")
  id27()

def id28(id15):
  id17=id11[id15]
  del id11[id15]
  
  id3.id18(id17)
  id19=0
  while id17:
    id20=id3.id21(id17)
    if id19<id20:
      break
    else:
      id19+=(id19==id20)

  id29=id19+1
  while id17:
    id20=id3.id21(id17)
    if id29<id20:
      break
    else:
      id29+=(id29==id20)

  return (id19,id29)


id30,id31=id28(id24)
id32=[]
id15=id6[id24]
while id15!=id24:
  id32.id23(id28(id15))
  id15=id6[id15]


del id4,id6,id9,id11,id12,id14


# 可能な初期値をそれぞれシミュレート
# 1
id15=id30
for id33 in id32:
  if id33[0]==id15:
    id15=id33[1]
  else:
    id15=id33[0]
if id15!=id30:
  print("POSSIBLE")
  id27()

# 2
id15=id31
for id33 in id32:
  if id33[0]==id15:
    id15=id33[1]
  else:
    id15=id33[0]
if id15==id30:
  print("POSSIBLE")
  id27()

print("IMPOSSIBLE")