N = int(input())
s = list(input())
S = [0]*N
for i in range(N):
    if s[i]=='o':
        S[i]=1
    else:
        S[i]=-1

P = [[1]*N,[1]*N,[-1]*N,[-1]*N]

if S[0]==1:
    P[0][1]=1
    P[0][N-1]=1
    P[1][1] = -1
    P[1][N - 1] = -1
    P[2][1] = 1
    P[2][N - 1] = -1
    P[3][1] = -1
    P[3][N - 1] = 1
else:
    P[0][1] = 1
    P[0][N - 1] = -1
    P[1][1] = -1
    P[1][N - 1] = 1
    P[2][1] = 1
    P[2][N - 1] = 1
    P[3][1] = -1
    P[3][N - 1] = -1

result = -1
for i in range(1,N-1):
    if i == N-2:
        for j in range(4):
            if S[i] * P[j][i] == 1:
                if P[j][i + 1] == P[j][i - 1]:
                    if S[i+1] * P[j][i+1] == 1:
                        if P[j][0] == P[j][i]:
                            result = j
                            break
                    else:
                        if P[j][0] == - P[j][i]:
                            result = j
                            break
            else:
                if P[j][i + 1] == - P[j][i - 1]:
                    if S[i+1] * P[j][i+1] == 1:
                        if P[j][0] == P[j][i]:
                            result = j
                            break
                    else:
                        if P[j][0] == - P[j][i]:
                            result = j
                            break
    for j in range(4):
        if S[i]*P[j][i]==1:
            P[j][i+1]=P[j][i-1]
        else:
            P[j][i + 1] = - P[j][i - 1]

if result == -1:
    print(result)
else:
    for i in range(N):
        if P[result][i]==1:
            print('S',end="")
        else:
            print('W',end="")
