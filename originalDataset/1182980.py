N,A,B = list(map(int,input().split()))
l=list(map(int,input().split()))

def nCr(n, r):
    """
    Calculate the number of combination (nCr = nPr/r!).
    The parameters need to meet the condition of n >= r >= 0.
    It returns 1 if r == 0, which means there is one pattern
    to choice 0 items out of the number of n.
    """

    # 10C7 = 10C3
    r = min(r, n-r)

    # Calculate the numerator.
    numerator = 1
    for i in range(n, n-r, -1):
        numerator *= i

    # Calculate the denominator. Should use math.factorial?
    denominator = 1
    for i in range(r, 1, -1):
        denominator *= i

    return numerator // denominator

l.sort(reverse = True)
masd = {}
for i in l:
	masd[i] = 0
for i in l:
	masd[i] += 1

res = 0

maxave = 0

task = []

for i in range(A,B+1):
	if maxave < sum(l[:i])/i:
		maxave = sum(l[:i])/i
		task = [i]
	elif maxave == sum(l[:i])/i:
		task.append(i)

for i in task:
	c = 1
	d = {}
	for j in l[:i]:
		d[j] = 0
	for j in l[:i]:
		d[j] += 1

	for j in d.keys():
		c *= nCr(masd[j],d[j])
	res += c

print(maxave)
print(res)








