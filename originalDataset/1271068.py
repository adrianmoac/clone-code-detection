# ARC59 D input
nab = list(map(int, input().split()))

N = nab[0]
A = nab[1]
B = nab[2]
V = list(reversed(sorted(list(map(int, input().split())))))

# ARC59 D naive
def count(n):
    result = []
    prev = V[0]
    count = 1
    for i, v in enumerate(V[1:n]):
        if (v == prev):
            count += 1
        else:
            result.append(count)
            count = 1
        
        if(i == n-2):
            result.append(count)
        prev = v
        
    return result
        
def greedy(n):
    return sum(V[0:n])/n

def fact(n):
    res = 1
    for i in range(1,n+1):
        res *= i
    return res

def comb(p, u):
    nume = 1
    for i in range(u):
        nume *= (p-i)
    return int(nume / fact(u))


max_ave = -1
max_ave_comb = 0
counts = count(N)

for i in range(A, B+1):
    u = i # u is the number of items to pick
    ave = greedy(i)
    if (max_ave <= ave):
        for j in counts:
            if (u-j <= 0):
                if (max_ave != ave):
                    max_ave_comb = comb(j, u)
                else:
                    max_ave_comb += comb(j, u)
                break
            else:
                u -= j
        max_ave = ave
print(max_ave)
print(max_ave_comb)