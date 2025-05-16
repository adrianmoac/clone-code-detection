mod = 1000000007
N = int(input())
S = input()
T = input()
a = 1
b = 0 ###前が横だったら0 縦だったら1
i = 0
while i < N:
	if i == 0: ###初期処理
		if N == 1:
			a *= 3
			break
		if N == 2:
			a *= 6
			break
		else:
			if S[0] == S[1]:
				a *= 6
				i += 2
				b = 0
			else:
				a *= 3
				i += 1
				b = 1
	if i == N-1:
		if b == 0: ###前が横で次が縦
			a *= 1
			i += 1
			b = 1
			break
		if b == 1: ###前が縦で次も縦
			a *= 2
			i += 1
			b = 1
			break
	if S[i] == S[i+1]:
		if b == 0: ###前が横で次も横
			a *= 3
			i += 2
			b = 0
			continue
		if b == 1: ###前が縦で次が横
			a *= 2
			i += 2
			b = 0
			continue
	else:
		if b == 0: ###前が横で次が縦
			a *= 1
			i += 1
			b = 1
			continue
		if b == 1: ###前が縦で次も縦
			a *= 2
			i += 1
			b = 1
			continue
print(a % mod)

