N = int(input())
s = input()
S = ['SSS', 'SSW', 'SWW', 'WWW', 'WWS', 'WSS', 'SWS', 'WSW']
ans = []
for n in range(4):
    ans = []
    if len(s) == 3:
        print(-1)
        exit()
    elif s[1] == 'o' and n == 0:
        ans.append('S')
        ans.append('S')
    elif s[1] == 'x' and n == 0:
        ans.append('W')
        ans.append('S')
    elif s[1] == 'o' and n == 1:
        ans.append('S')
        ans.append('W')
    elif s[1] == 'x' and n == 1:
        ans.append('S')
        ans.append('W')
    elif s[1] == 'o' and n == 2:
        ans.append('W')
        ans.append('S')
    elif s[1] == 'x' and n == 2:
        ans.append('W')
        ans.append('W')
    elif s[1] == 'o' and n == 3:
        ans.append('W')
        ans.append('W')
    elif s[1] == 'x' and n == 3:
        ans.append('S')
        ans.append('S')

    for i in range(1, N):
        if ans[i - 1] == 'S':
            if ans[i] == 'S':
                if s[i] == 'o':
                    ans.append('S')
                else:
                    ans.append('W')
            else:
                if s[i] == 'o':
                    ans.append('W')
                else:
                    ans.append('S')
        else:
            if ans[i] == 'S':
                if s[i] == 'o':
                    ans.append('W')
                else:
                    ans.append('S')
            else:
                if s[i] == 'o':
                    ans.append('S')
                else:
                    ans.append('W')
    if ans[N-1] == 'S' and ans[N] == ans[0]:
        if ans[0] == 'S':
            if s[0] == 'o' and ans[1] == 'S':
                break
            elif s[0] == 'x' and ans[1] == 'W':
                break
        else:
            if s[0] == 'o' and ans[1] == 'W':
                break
            elif s[0] == 'x' and ans[1] == 'S':
                break
    elif ans[N-1] == 'W' and ans[N] == ans[0]:
        if ans[0] == 'S':
            if s[0] == 'o' and ans[1] == 'W':
                break
            elif s[0] == 'x' and ans[1] == 'S':
                break
        else:
            if s[0] == 'o' and ans[1] == 'S':
                break
            elif s[0] == 'x' and ans[1] == 'W':
                break
    if n == 3:
        print(-1)
        exit()
ans.pop()
ans = ''.join(ans)
print(ans)
