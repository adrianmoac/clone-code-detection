#-*-coding: utf-8-*-x1, y1, r=map(lambda x:int(x), input().split(" "))
id0, id1, id2, id3=map(lambda id4:id5(id4), input().split(" "))

# 接点の有無
def id6(id7, id8, id9, id10, id11):

  if id11<id9:
    id12=(id11-id9)**2-id13**2+(id8-id7)**2
    if id12>=0:
      return False
    id14=(id10-id9)**2-id13**2+(id8-id7)**2
  elif ((id10+id11)/2<=id9) and id9<=id11:
    id12=-id13**2+(id8-id7)**2
    if id12>=0:
      return False
    id14=(id10-id9)**2-id13**2+(id8-id7)**2
  elif id10<=id9 and (id9<=(id10+id11)/2):
    id12=-id13**2+(id8-id7)**2
    if id12>=0:
      return False
    id14=(id11-id9)**2-id13**2+(id8-id7)**2
  elif id9<id10:
    id12=(id10-id9)**2-id13**2+(id8-id7)**2
    if id12>=0:
      return False
    id14=(id11-id9)**2-id13**2+(id8-id7)**2

  if id12<0 and 0<id14:
    return True
  else:
    return False


def id15():
  #接点なし
  if (id0-id16)**2+(id1-id17)**2<=id13**2:
    # 円の中に四角
    print("YES")
    print("NO")
  elif id0<id16 and id16<id2 and id1<id17 and id17<id3:
    # 四角の中に円
    print("NO")
    print("YES")
  else:
    # 四角の外に円
    print("YES")
    print("YES")


if id2<id16-id13 or id16+id13<id0 or id3<id17-id13 or id17+id13<id1:
  id15()
#接点あり
elif id6(id16, id0, id17, id1, id3):
  print("YES")
  print("YES")
elif id6(id17, id3, id16, id0, id2):
  print("YES")
  print("YES")
elif id6(id16, id2, id17, id1, id3):
  print("YES")
  print("YES")
elif id6(id17, id1, id16, id0, id2):
  print("YES")
  print("YES")
# 接点なし
else:
  id15()