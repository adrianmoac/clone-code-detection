id0, id1, id2=map(lambda id3:id4(id3), input().split(" "))
id5, id6, id7, id8=map(lambda id3:id4(id3), input().split(" "))
def id9(id10, id11, id12, id13, id14):
if id14<id12:
id15=(id14-id12)**2-id2**2+(id11-id10)**2
id16=(id13-id12)**2-id2**2+(id11-id10)**2
elif ((id13+id14)/2<=id12) and id12<=id14:
id15=-id2**2+(id11-id10)**2
id16=(id13-id12)**2-id2**2+(id11-id10)**2
elif id13<=id12 and (id12<=(id13+id14)/2):
id15=-id2**2+(id11-id10)**2
id16=(id14-id12)**2-id2**2+(id11-id10)**2
elif id12<id13:
id15=(id13-id12)**2-id2**2+(id11-id10)**2
id16=(id14-id12)**2-id2**2+(id11-id10)**2
if id15<0 and 0<id16:
return True
else:
return False
def id17():
if (id5-id0)**2+(id6-id1)**2<=id2**2:
print("YES")
print("NO")
elif id5<id0 and id0<id7 and id6<id1 and id1<id8:
print("NO")
print("YES")
else:
print("YES")
print("YES")
if id7<id0-id2 or id0+id2<id5 or id8<id1-id2 or id1+id2<id6:
id17()
elif id9(id0, id5, id1, id6, id8):
print("YES")
print("YES")
elif id9(id1, id8, id0, id5, id7):
print("YES")
print("YES")
elif id9(id0, id7, id1, id6, id8):
print("YES")
print("YES")
elif id9(id1, id6, id0, id5, id7):
print("YES")
print("YES")
else:
id17()