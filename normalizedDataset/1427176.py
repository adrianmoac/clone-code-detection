id0=id1(id2())
id3={}
for _ in id4(id0-1):
  id5,id6=map(id1, id2().split())
  if id5 in id3:
    id3[id5].id7(id6)
  else:
    id3[id5]=[id6]

  if id6 in id3:
    id3[id6].id7(id5)
  else:
    id3[id6]=[id5]

#-1: not yet, 0: fennec, 1: sunuke
id8=[-1]*(id0+1)
id8[1]=0
id8[id0]=1

# 0==fennec, 1==sunuke
id9=[(1,1), (id0,id0)]

# 0: fennec
# 1: sunuke
id10=[1,1]

while id11(id9)>0:
  id12, id13=id9.id14(0)

  for id5 in id3[id12]:
    if id5==id13: continue
    if id8[id5]!=-1: continue

    id15=id8[id13]
    id8[id5]=id15
    id10[id15]+=1

    id9.id7([id5, id12])


if id10[0]>id10[1]:
  print "Fennec"
else:
  print "Snuke"

# TLE
# while len(q)>0:
#   cur, prev, sunuke=q.pop(0)
#   # print cur,prev,sunuke

#   if visited[cur]:
#     continue

#   visited[cur]=True
#   if sunuke:
#     count_s+=1
#   else:
#     count_f+=1

#   for v in d[cur]:
#     q.append([v, cur, sunuke])

# if count_f>count_s:
#   print 'Fennec'
# else:
#   print 'Snuke'