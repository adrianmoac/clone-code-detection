R, C, n = map(int, raw_input().split())
x1 = []
y1 = []
x2 = []
y2 = []
for i in xrange(n): 
  xx1, yy1, xx2, yy2 = map(int, raw_input().split())
  x1.append(xx1)
  y1.append(yy1)
  x2.append(xx2)
  y2.append(yy2)

t = []
b = []
l = []
r = []

def add(x, y, i):
  if x == 0:
    t.append((i, y))
  elif x == R:
    b.append((i, y))
  elif y == 0:
    l.append((i, x))
  elif y == C:
    r.append((i, x))


for i in xrange(n):
  add(x1[i], y1[i], i)
  add(x2[i], y2[i], i)

t = sorted(t, key=lambda x : x[1])    
r = sorted(r, key=lambda x : x[1])
b = sorted(b, key=lambda x : x[1], reverse=True)
l = sorted(l, key=lambda x : x[1], reverse=True)

lis = []
lis.extend(t)
lis.extend(r)
lis.extend(b)
lis.extend(l)

lis = map(lambda x : x[0], lis)

cnt = {}
for i in lis:
  if not i in cnt:
    cnt[i] = 0
  cnt[i] += 1

lis = filter(lambda x : cnt[x] == 2, lis)

stk = []
for i in lis:
  if len(stk) == 0 or stk[-1] != i:
    stk.append(i)
  else:
    stk.pop()

if len(stk) == 0:
  print("YES")
else:
  print("NO")
