from id0 import id1
from id2 import id3

def id4():
  return id5(input())

def id6():
  return [id5(id7) for id7 in input().split()]

def id8(id9):
    id10=id11(id12(id9, 1,-1))
    id8=[]
    while id10:
        id13=id10.id14()
        id8.id15(id13)
        id10.id16(id11(id12(id13*2, id9+1, id13)))
    return id17(id8)

id18=id8(10**6)

def id19(id7):
  id20=id21()
  while id7>1:
    for id13 in id18:
      if id13>=id7**0.5+1:
        id20[id7]=id20.id22(id7, 0)+1
        id7=1
        break
      if id7%id13==0:
        id20[id13]=id20.id22(id13, 0)+1
        id7//=id13
        break
  return id20

def id23(id24):
  id20=1
  for id7 in id24:
    id20*=id7
  return id20

def id25(id9):
  id26=id27(id19(id9).id28())
  id20=[]
  for id29 in id3(*[id12(id30+1) for (id13, id30) in id26]):
    id20.id15(id23(id26[id31][0]**id29[id31] for id31 in id12(id32(id26))))
  return id17(id20)

def id33(id34, id9):
  return 0 if id9==0 else id33(id34, id9//id34)+id9%id34

id9=id4()
id35=id4()

if id9<id35:
  print(-1); id1()

if id9==id35:
  print(id35+1); id1()

for id7 in id25(id36(id9-id35)):
  id34=id7+1
  if id33(id34, id9)==id35:
    print(id34); id1()

print(-1)