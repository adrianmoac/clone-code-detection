import math

diff = int(raw_input())

res = 0

for digits in range(1, 20):
	A = [0 for i in range(digits)]

	r = digits - 1
	l = 0

	ite = 0

	while l < r:
		A[ite] = 10**r - 10**l
		ite += 1
		l += 1
		r -= 1

	bonus = 1
	if l == r:
		bonus = 10

	ways_in_pos_0 = [0 for i in range(20)]
	ways_in_other = [0 for i in range(20)]

	for i in range(0, 10):
		for j in range(0, 10):
			ways_in_other[i - j] += 1
	for i in range(1, 10):
		for j in range(1, 10):
			ways_in_pos_0[i - j] += 1

	def recurse(pos, made):
		if pos == ite:
			if made == diff:
				return 1
			else:
				return 0
		elif pos == 0:
			curr = 0

			for i in range(-9, 9 + 1):
				if abs(made + i * A[pos] - diff) <= A[pos]:
					curr += recurse(pos + 1, made + i * A[pos]) * ways_in_pos_0[i]

			return curr
		else:
			curr = 0

			for i in range(-9, 9 + 1):
				if abs(made + i * A[pos] - diff) <= A[pos]:
					curr += recurse(pos + 1, made + i * A[pos]) * ways_in_other[i]

			return curr

	res += bonus * recurse(0, 0)

print res