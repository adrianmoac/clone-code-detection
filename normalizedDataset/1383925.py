id0=id1(input())


class id2:
  def id3(id4, id5):
    id4.id6=id7(id8(id5))
    id4.id9=[0]*id5
  
  def id10(id4, id11):
    if id4.id6[id11]==id11:
      return id11
    else:
      id4.id6[id11]=id4.id10(id4.id6[id11])
      return id4.id6[id11]

  def id12(id4, id11, id13):
    id14=id4.id10(id11)
    id15=id4.id10(id13)
    if id4.id9[id14]>id4.id9[id15]:
      id4.id6[id15]=id14
    elif id4.id9[id14]<id4.id9[id15]:
      id4.id6[id14]=id15
    elif id14!=id15:
      id4.id6[id15]=id14
      id4.id9[id14]+=1


id16,id17=[],[]
for id18 in id8(id0):
  id11,id13=map(id1, input().split())
  id16.id19((id11,id18))
  id17.id19((id13,id18))

id16.id20()
id17.id20()

def id21(id22):
  id23=id24(id22)
  id25=id24(id22)
  id26(id25)

  id27=[]

  for id28,id29 in id30(id23, id25):
    id31, id32=id28
    id33, id34=id29
    id35=id36(id31-id33)
    id27.id19((id35,id32,id34))
  return id27

id37=id21(id16)
id38=id21(id17)

id27=id37+id38
id27.id20()

id39=0
id40=id2(id0)
id41=1

for id35,id18,id42 in id27:
  if id40.id10(id18)!=id40.id10(id42):
    id40.id12(id18,id42)
    id39+=id35
    id41+=1
    if id41>=id0:
      break

print(id39)