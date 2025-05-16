n = int(raw_input())
d = {}
for _ in range(n-1):
  v,u = map(int, raw_input().split())
  if v in d:
    d[v].append(u)
  else:
    d[v] = [u]

  if u in d:
    d[u].append(v)
  else:
    d[u] = [v]

# -1: not yet, 0: fennec, 1: sunuke
visited = [-1] * (n+1)
visited[1] = 0
visited[n] = 1

# 0 == fennec, 1 == sunuke
q = [(1,1), (n,n)]

# 0: fennec
# 1: sunuke
count = [1,1]

while len(q) > 0:
  cur, prev = q.pop(0)

  for v in d[cur]:
    if v == prev: continue
    if visited[v] != -1: continue

    chara = visited[prev]
    visited[v] = chara
    count[chara] += 1

    q.append([v, cur])


if count[0] > count[1]:
  print 'Fennec'
else:
  print 'Snuke'

# TLE
# while len(q) > 0:
#   cur, prev, sunuke = q.pop(0)
#   # print cur,prev,sunuke

#   if visited[cur]:
#     continue

#   visited[cur] = True
#   if sunuke:
#     count_s += 1
#   else:
#     count_f += 1

#   for v in d[cur]:
#     q.append([v, cur, sunuke])

# if count_f > count_s:
#   print 'Fennec'
# else:
#   print 'Snuke'