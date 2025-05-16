n = input()
S = [raw_input() for i in xrange(2)]

dp = [[[0]*3 for i in xrange(3)] for j in xrange(n)]

MOD = 10**9 + 7

if S[0][0] == S[1][0]:
    for i in xrange(3):
        dp[0][i][i] = 1
else:
    for i in xrange(3):
        for j in xrange(3):
            if i == j:
                continue
            dp[0][i][j] = 1

for i in xrange(1, n):
    if S[0][i-1] == S[0][i]:
        for p in xrange(3):
            for q in xrange(3):
                dp[i][p][q] = dp[i-1][p][q]
    else:
        if S[0][i-1] == S[1][i-1]:
            if S[0][i] == S[1][i]:
                # AB
                # AB
                for s in xrange(3):
                    for t in xrange(3):
                        if s == t:
                            continue
                        dp[i][s][s] += dp[i-1][t][t]
                        dp[i][s][s] %= MOD
            else:
                # AB
                # AC
                for u in xrange(3):
                    for s in xrange(3):
                        if u == s:
                            continue
                        for t in xrange(3):
                            if u == t or t == s:
                                continue
                            dp[i][s][t] += dp[i-1][u][u]
                            dp[i][s][t] %= MOD
        else:
            if S[0][i] == S[1][i]:
                # AC
                # BC
                for u in xrange(3):
                    for s in xrange(3):
                        if u == s:
                            continue
                        for t in xrange(3):
                            if u == t or t == s:
                                continue
                            dp[i][u][u] += dp[i-1][s][t]
                            dp[i][u][u] %= MOD
            else:
                # AC ps
                # BD qt
                for p in xrange(3):
                    for q in xrange(3):
                        if p == q:
                            continue
                        for s in xrange(3):
                            if p == s:
                                continue
                            for t in xrange(3):
                                if s == t or q == t:
                                    continue
                                dp[i][s][t] += dp[i-1][p][q]
ans = 0
for i in xrange(3):
    for j in xrange(3):
        ans += dp[n-1][i][j]
print ans % MOD