S = list(input())
T = list(input())

# S=list("BBAAABA")
# T=list("BBBA")

q = int(input())

l = []
for i in range(q):
	l.append(list(map(int,input().split(" "))))


sta = [0 for i in range(len(S))]
stb = [0 for i in range(len(S))]

tta = [0 for i in range(len(T))]
ttb = [0 for i in range(len(T))]

if S[0] == "A":
	sta[0] = 1
else:
	stb[0] = 1

if T[0] == "A":
	tta[0] = 1
else:
	ttb[0] = 1

for i in range(1,len(S)):
	if S[i] == "A":
		sta[i] = sta[i-1]+1
		stb[i] = stb[i-1]
	else:
		sta[i] = sta[i-1]
		stb[i] = stb[i-1]+1

for i in range(1,len(T)):
	if T[i] == "A":
		tta[i] = tta[i-1]+1
		ttb[i] = ttb[i-1]
	else:
		tta[i] = tta[i-1]
		ttb[i] = ttb[i-1]+1


def get(l,a,b):
	if a == 0:
		return(l[b])
	else:
		return(l[b]-l[a-1])

for a,b,c,d in l:
	sa = get(sta,a-1,b-1)
	sb = get(stb,a-1,b-1)
	ta = get(tta,c-1,d-1)
	tb = get(ttb,c-1,d-1)


	if (sa+sb*2)%3 == (ta+tb*2)%3:
		print("YES")
	else:
		print("NO")



















