import sys

N = int(input())
stemp = input()
s = [True if stemp[i]== 'o' else False for i in range(N)]

T = [True, True] #Sheap, Sheap

for i in range(2,N+1):
    if s[i-1]^T[i-1]==True:
        T.append( not T[i-2])
    else:
        T.append( T[i-2])

if T[N] == T[0] and ((T[1]==T[N-1]) != (T[0] != s[0])):
    output = ['S' if T[i] == True else 'W' for i in range(N)]
    for i in range(N):
        print(output[i], end='')
    print()
    sys.exit()

T = [True, False] #Sheap, Wolf

for i in range(2,N+1):
    if s[i-1]^T[i-1]==True:
        T.append( not T[i-2])
    else:
        T.append( T[i-2])

if T[N] == T[0] and ((T[1]==T[N-1]) != (T[0] != s[0])):
    output = ['S' if T[i] == True else 'W' for i in range(N)]
    for i in range(N):
        print(output[i], end='')
    print()
    sys.exit()

T = [False, True] #Wolf, Sheap

for i in range(2,N+1):
    if s[i-1]^T[i-1]==True:
        T.append( not T[i-2])
    else:
        T.append( T[i-2])

if T[N] == T[0] and ((T[1]==T[N-1]) != (T[0] != s[0])):
    output = ['S' if T[i] == True else 'W' for i in range(N)]
    for i in range(N):
        print(output[i], end='')
    print()
    sys.exit()

T = [False, False]

for i in range(2,N+1):
    if s[i-1]^T[i-1]==True:
        T.append( not T[i-2])
    else:
        T.append( T[i-2])

if T[N] == T[0] and ((T[1]==T[N-1]) != (T[0] != s[0])):
    output = ['S' if T[i] == True else 'W' for i in range(N)]
    for i in range(N):
        print(output[i], end='')
    print()
    sys.exit()

print(-1)
