H, W = map(int, input().split())
S = []
T = []
for i in range(H):
    S.append(input())
    T.append([0 for j in range(W)])
if H == 1 and W == 1:
    if S[0][0] == "#":
        T[0][0] = "#"
    else:
        T[0][0] = 0
elif H == 1:
    for j in range(W):
        if S[0][j] == "#":
            T[0][j] = "#"
        elif S[0][j] == ".":
            if j == 0:
                if S[0][j + 1] == "#":
                    T[0][j] += 1
            elif j == W - 1:
                if S[0][j - 1] == "#":
                    T[0][j] += 1
            else:
                if S[0][j - 1] == "#":
                    T[0][j] += 1
                if S[0][j + 1] == "#":
                    T[0][j] += 1
elif W == 1:
    for i in range(H):
        if S[i][0] == "#":
            T[i][0] = "#"
        elif S[i][0] == ".":
            if i == 0:
                if S[i + 1][0] == "#":
                    T[i][0] += 1
            elif i == H - 1:
                if S[i - 1][0] == "#":
                    T[i][0] += 1
            else:
                if S[i - 1][0] == "#":
                    T[i][0] += 1
                if S[i + 1][0] == "#":
                    T[i][0] += 1
else:
    for i in range(H):
        for j in range(W):
            if S[i][j] == "#":
                T[i][j] = "#"
            elif S[i][j] == ".":
                if i == 0 and j == 0:
                    if S[i + 1][j] == "#":
                        T[i][j] += 1
                    if S[i][j + 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j + 1] == "#":
                        T[i][j] += 1
                elif i == 0 and j == W - 1:
                    if S[i + 1][j] == "#":
                        T[i][j] += 1
                    if S[i][j - 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j - 1] == "#":
                        T[i][j] += 1
                elif i == H - 1 and j == 0:
                    if S[i][j + 1] == "#":
                        T[i][j] += 1
                    if S[i - 1][j] == "#":
                        T[i][j] += 1
                    if S[i - 1][j + 1] == "#":
                        T[i][j] += 1
                elif i == H - 1 and j == W - 1:
                    if S[i - 1][j] == "#":
                        T[i][j] += 1
                    if S[i][j - 1] == "#":
                        T[i][j] += 1
                    if S[i - 1][j - 1] == "#":
                        T[i][j] += 1
                elif i == 0:
                    if S[i][j - 1] == "#":
                        T[i][j] += 1
                    if S[i][j + 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j - 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j] == "#":
                        T[i][j] += 1
                    if S[i + 1][j + 1] == "#":
                        T[i][j] += 1
                elif j == 0:
                    if S[i - 1][j] == "#":
                        T[i][j] += 1
                    if S[i + 1][j] == "#":
                        T[i][j] += 1
                    if S[i - 1][j + 1] == "#":
                        T[i][j] += 1
                    if S[i][j + 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j + 1] == "#":
                        T[i][j] += 1
                elif i == H - 1:
                    if S[i - 1][j - 1] =="#":
                        T[i][j] += 1
                    if S[i - 1][j] == "#":
                        T[i][j] += 1
                    if S[i - 1][j + 1] == "#":
                        T[i][j] += 1
                    if S[i][j - 1] == "#":
                        T[i][j] += 1
                    if S[i][j + 1] == "#":
                        T[i][j] += 1
                elif j == W - 1:
                    if S[i - 1][j - 1] == "#":
                        T[i][j] += 1
                    if S[i][j - 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j - 1] == "#":
                        T[i][j] += 1
                    if S[i - 1][j] == "#":
                        T[i][j] += 1
                    if S[i + 1][j] == "#":
                        T[i][j] += 1
                else:
                    if S[i - 1][j - 1] == "#":
                        T[i][j] += 1
                    if S[i - 1][j] == "#":
                        T[i][j] += 1
                    if S[i - 1][j + 1] == "#":
                        T[i][j] += 1
                    if S[i][j - 1] == "#":
                        T[i][j] += 1
                    if S[i][j + 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j - 1] == "#":
                        T[i][j] += 1
                    if S[i + 1][j] == "#":
                        T[i][j] += 1
                    if S[i + 1][j + 1] == "#":
                        T[i][j] += 1
s = ""
for i in range(H):
    for j in range(W):
        s += str(T[i][j])
    print(s)
    s = ""
