MOD = 1000000007

N = int(input())
S = list(input())

s = 'S'
w = 'W'
c = 0
c1 = 0
c2 = 0

for i in [s, w]:
    if(c == 1): break
    for j in [s, w]:
        if (c == 1): break
        t = list()
        t.append(i)
        t.append(j)

        for k in range(1, N-1):
            if(S[k] == 'o'):
               if(t[k] == s):
                   t.append(t[k-1])
               else:
                    if(t[k-1] == s): t.append(w)
                    else: t.append(s)

            else:
                if (t[k] == w):
                    t.append(t[k - 1])
                else:
                    if (t[k - 1] == s):
                        t.append(w)
                    else:
                        t.append(s)

        c1 = 0
        if(t[0] == s):
            if(S[0] == 'o'):
                if(t[1] == t[N-1]):
                    c1 = 1
            else:
                if (t[1] != t[N - 1]):
                    c1 = 1
        else:
            if (S[0] == 'x'):
                if (t[1] == t[N - 1]):
                    c1 = 1
            else:
                if (t[1] != t[N - 1]):
                    c1 = 1
        c2 = 0
        if (t[N-1] == s):
            if (S[N-1] == 'o'):
                if (t[0] == t[N - 2]):
                    c2 = 1
            else:
                if (t[0] != t[N - 2]):
                    c2 = 1
        else:
            if (S[N-1] == 'x'):
                if (t[0] == t[N - 2]):
                    c2 = 1
            else:
                if (t[0] != t[N - 2]):
                    c2 = 1
        if(c1 == 1 & c2 == 1): c = 1

if(c == 1):
    print(''.join(t))
else:
    print('-1')