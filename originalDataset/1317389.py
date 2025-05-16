import math
import sys
 
T = list(map(int, input().split()))
S = T[0] * T[1]
 
if ((T[0] % 3 == 0) or (T[1] % 3 == 0)):
    print(0)
    sys.exit()
 
minS = 1000000000000
for i in range(1, math.ceil(T[0]/2)+1):
    A = i * T[1]
    F = math.floor(T[1] / 2) * (T[0] - i)
    C = S - (A + F)
    if (F == C):
        minS = min(minS, abs(A - F))
    else:
        if (A > C):
            minS = min(minS, abs(A - F))
        elif(C >= A and A >= F):
            minS = min(minS, abs(C - F))
        else:
            minS = min(minS, abs(C - A))
    A = i * T[1]
    F = math.floor((T[0] - i) / 2) * T[1]
    C = S - (A + F)
    if (F == C):
        minS = min(minS, abs(A - F))
    else:
        if (A > C):
            minS = min(minS, abs(A - F))
        elif(C >= A and A >= F):
            minS = min(minS, abs(C - F))
        else:
            minS = min(minS, abs(C - A))
 
for i in range(1, math.ceil(T[1]/2) + 1):
    A = i * T[0]
    F = math.floor(T[0] / 2) * (T[1] - i)
    C = S - (A + F)
    if (F == C):
        minS = min(minS, abs(A - F))
    else:
        if (A > C):
            minS = min(minS, abs(A - F))
        elif(C >= A and A >= F):
            minS = min(minS, abs(C - F))
        else:
            minS = min(minS, abs(C - A))
    A = i * T[0]
    F = math.floor((T[1] - i) / 2) * T[0]
    C = S - (A + F)
    if (F == C):
        minS = min(minS, abs(A - F))
    else:
        if (A > C):
            minS = min(minS, abs(A - F))
        elif(C >= A and A >= F):
            minS = min(minS, abs(C - F))
        else:
            minS = min(minS, abs(C - A))
 
print(minS)