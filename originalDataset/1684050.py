H, W = map(int, input().split())
S = {}
for _ in range(H):
    S[_] = input()
    
def change(S_str, x, j):
    s_list = list(S_str)
    s_list[j] = str(x.count('#'))
    S_str = "".join(s_list)
    return S_str

for i in range(H):
    for j in range(W):
        s = S[i][j]
        if s == '.':
            if H == 1 and W == 1:
                S[i] = '0'
            elif H == 1 and j == 0:
                x = S[i][j+1]
                S[i] = change(S[i], x, j)
            elif H == 1 and j == W-1:
                x = S[i][j-1]
                S[i] = change(S[i], x, j)
            elif H == 1:
                x = S[i][j-1] + S[i][j+1]
                S[i] = change(S[i], x, j)
            elif W == 1 and i == 0:
                x = S[i+1][j]
                S[i] = change(S[i], x, j)
            elif W == 1 and i == W-1:
                x = S[i-1][j]
                S[i] = change(S[i], x, j)
            elif W == 1:
                x = S[i-1][j] + S[i+1][j]
                S[i] = change(S[i], x, j)
            elif i == 0 and j == 0:
                x = S[i][j+1] + S[i+1][j] + S[i+1][j+1]
                S[i] = change(S[i], x, j)
            elif i == 0 and j == W-1:
                x = S[i][j-1] + S[i+1][j-1] + S[i+1][j]
                S[i] = change(S[i], x, j)
            elif i == 0:
                x = S[i][j-1] + S[i][j+1] + S[i+1][j-1] + S[i+1][j] + S[i+1][j+1]
                S[i] = change(S[i], x, j)
            elif i == H-1 and j == 0:
                x = S[i][j+1] + S[i-1][j] + S[i-1][j+1]
                S[i] = change(S[i], x, j)
            elif i == H-1 and j == W-1:
                x = S[i][j-1] + S[i-1][j-1] + S[i-1][j]
                S[i] = change(S[i], x, j)
            elif i == H-1:
                x = S[i][j-1] + S[i][j+1] + S[i-1][j-1] + S[i-1][j] + S[i-1][j+1]
                S[i] = change(S[i], x, j)
            elif j == 0:
                x = S[i-1][j] + S[i-1][j+1] + S[i][j+1] + S[i+1][j] + S[i+1][j+1]
                S[i] = change(S[i], x, j)
            elif j == W-1:
                x = S[i-1][j-1] + S[i-1][j] + S[i][j-1] + S[i+1][j-1] + S[i+1][j]
                S[i] = change(S[i], x, j)
            else:
                x = S[i-1][j-1] + S[i-1][j] + S[i-1][j+1] + S[i][j-1] + S[i][j+1] + S[i+1][j-1] + S[i+1][j] + S[i+1][j+1]
                S[i] = change(S[i], x, j)
                
for k in range(H):
    print(S[k])