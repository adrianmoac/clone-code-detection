sx, sy, tx, ty = list(map(int, input().split()))

vec = []
x, y = sx, sy
for i in range(ty - sy - 1):
    vec.append("U")
    y += 1

for i in range(tx - sx - 1):
    vec.append("R")
    x += 1

for i in range(ty - y):
    vec.append("U")
    y += 1

for i in range(tx - x):
    vec.append("R")
    x += 1

vec.append("R")
x += 1

for i in range(ty - sy + 1):
    vec.append("D")
    y -= 1

for i in range(x - sx):
    vec.append("L")
    x -= 1

vec.append("U")
y += 1
vec.append("L")
x -= 1

for i in range(ty + 1 - y):
    vec.append("U")
    y += 1

for i in range(tx - x):
    vec.append("R")
    x += 1

vec.append("D")
y -= 1

vec.append("D")
y -= 1

for i in range(ty - sy - 1):
    vec.append("D")
    y -= 1

for i in range(tx - sx - 1):
    vec.append("L")
    x -= 1

for i in range(y - sy):
    vec.append("D")
    y -= 1

for i in range(x - sx):
    vec.append("L")
    x -= 1

# print(vec)
# print(x, y)
for v in vec:
    print(v, end="")