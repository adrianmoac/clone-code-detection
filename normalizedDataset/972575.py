from id0 import id1, id2
from id3 import id4
from id5 import*from id6 import id7
from id8 import id8

def id9():
  return id10(input())

def id11():
  return [id10(id12) for id12 in input().split()]

def id13(id12):
  if id12=="No":
    return "No"
  elif id12=="Any":
    return "Any"
  else:
    (id14, id15, id16)=id12
    return (id14-1, id15+1, (id16+1)%2)

def id17(id12, id18):
  if id12=="No" or id18=="No":
    return "No"
  elif id18=="Any":
    return id12
  elif id12=="Any":
    return id18
  else:
    (id19, id20, id21)=id12
    (id22, id23, id24)=id18
    if id21!=id24 or id20<id22 or id23<id19:
      return "No"
    else:
      return (id25(id19, id22), id26(id20, id23), id21)

id2(1000000)

id27=id9()

id28=[[] for id29 in id30(id27)]

for id29 in id30(id27-1):
  (id31, id32)=id11()
  (id31, id32)=(id31-1, id32-1)
  id28[id31].id33(id32)
  id28[id32].id33(id31)

id34=id9()
id35=["Any"]*id27

for id29 in id30(id34):
  (id36, id37)=id11()
  id36=id36-1
  id35[id36]=(id37, id37, id37%2)

id38=[[] for id29 in id30(id27)]
id39=[0]*id27

id39[0]=None
def id40(id41):
  id38[id41]=id42(id28[id41])
  if id41!=0:
    id38[id41].id43(id39[id41])
  for id29 in id38[id41]:
    id39[id29]=id41
    id40(id29)
    # print("i={0}, d[i]={1} ".format(i, d[i]))
  id35[id41]=id4(id17, (id13(id35[id29]) for id29 in id38[id41]), id35[id41])

id40(0)

id44=[0]*id27
def id45(id41, id46=None):
  if id35[id41]=="No":
    print("No"); id1()
  elif id35[id41]=="Any":
    id44[id41]=id46+1
  else:
    (id14, id15, id16)=id35[id41]
    if id46==None:
      if id14%2==id16:
        id44[id41]=id14
      else:
        id44[id41]=id14+1
    else:
      if id14<=id46-1<=id15:
        id44[id41]=id46-1
      elif id14<=id46+1<=id15:
        id44[id41]=id46+1
      else:
        print("No"); id1()
  for id29 in id38[id41]:
    id45(id29, id44[id41])

id45(0)

print("Yes")
for id29 in id30(id27):
  print(id44[id29])