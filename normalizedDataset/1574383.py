id0=19
id1=[id2() for id3 in id4(id0)]

def id5(id6, id7): #limit: 0 or 1
  id8=[]
  
  # horizontal
  for id3 in id4(id0):
    id9=0
    for id10 in id4(id0):
      if id1[id3][id10]==id6:
        id9+=1
        if id9>=5:
          if id7==0 or id9==10: return False
          if id11(id8)==0:
            for id12 in id4(5):
              id8.id13((id10-id12,id3))
          elif id9==5:
            for id12 in id4(5):
              id14=(id10-id12,id3)
              if id14 in id8:
                id8=[id14]
                break
            else:
              return False
          elif id8[-1]==(id10-5,id3):
            id8.id15()
      else:
        id9=0
  # vertical
  for id3 in id4(id0):
    id9=0
    for id10 in id4(id0):
      if id1[id10][id3]==id6:
        id9+=1
        if id9>=5:
          if id7==0 or id9==10: return False
          if id11(id8)==0:
            for id12 in id4(5):
              id8.id13((id3,id10-id12))
          elif id9==5:
            for id12 in id4(5):
              id14=(id3,id10-id12)
              if id14 in id8:
                id8=[id14]
                break
            else:
              return False
          elif id8[-1]==(id3,id10-5):
            id8.id15()
      else:
        id9=0
  # diagonal (/)
  for id3 in id4(2*id0-1):
    id9=0
    id16=id17(0, id3-id0+1)
    for id10 in id4(id0-id18(id0-1-id3)):
      if id1[id16+id10][id3-id16-id10]==id6:
        id9+=1
        if id9>=5:
          if id7==0 or id9==10: return False
          if id11(id8)==0:
            for id12 in id4(5):
              id8.id13((id3-id16-id10+id12,id16+id10-id12))
          elif id9==5:
            for id12 in id4(5):
              id14=(id3-id16-id10+id12,id16+id10-id12)
              if id14 in id8:
                id8=[id14]
                break
            else:
              return False
          elif id8[-1]==(id3-id16-id10+5,id16+id10-5):
            id8.id15()
      else:
        id9=0
  # diagonal (\)
  for id3 in id4(2*id0-1):
    id9=0
    id16=id17(0, id3-id0+1)
    for id10 in id4(id0-id18(id0-1-id3)):
      if id1[id16+id10][id16+id10-id3+id0-1]==id6:
        id9+=1
        if id9>=5:
          if id7==0 or id9==10: return False
          if id11(id8)==0:
            for id12 in id4(5):
              id8.id13((id16+id10-id3+id0-1-id12,id16+id10-id12))
          elif id9==5:
            for id12 in id4(5):
              id14=(id16+id10-id3+id0-1-id12,id16+id10-id12)
              if id14 in id8:
                id8=[id14]
                break
            else:
              return False
          elif id8[-1]==(id16+id10-id3+id0-1-5,id16+id10-5):
            id8.id15()
      else:
        id9=0
  return True

def id19():
  id20=id21=0
  for id22 in id1:
    id20+=id22.id23("o")
    id21+=id22.id23("x")
  if not 0<=id20-id21<=1:
    return False

  # last turn is o
  if id20>id21:
    return id5("x",0) and id5("o",1)
  # last turn is x
  else:
    return id5("o",0) and id5("x",1)

print("YES" if id19() else "NO")