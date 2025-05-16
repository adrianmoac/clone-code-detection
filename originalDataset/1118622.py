N = int(raw_input())
s = raw_input()
assert(3 <= N <= 1e5)
assert(len(s) == N)

res = []
sheep = 'S'
wolf = 'W'
container = [val for val in s]
o = 'o'
x = 'x'
passed = False
res0 = [sheep, sheep]
res1 = [sheep, wolf]
res2 = [wolf, sheep]
res3 = [wolf, wolf]
RES = [res0, res1, res2, res3]
for res in RES:
    passed1 = False
    passed2 = False
    for i in xrange(1, len(container) - 1):
        val = container[i]
        if res[i] == sheep:
            if val == o:
                res.append(res[i - 1])
            else:
                if res[i - 1] == sheep:
                    res.append(wolf)
                else:
                    res.append(sheep)
        else:# wolf
            if val == o:
                if res[i - 1] == sheep:
                    res.append(wolf)
                else:
                    res.append(sheep)
            else:
                res.append(res[i - 1])
    if (res[0] == sheep):
        if (container[0] == o) and (res[-1] == res[1]):
            passed1 = True
        elif (container[0] == x) and (not (res[-1] == res[1])):
            passed1 = True
    else:
        if (container[0] == o) and (not (res[-1] == res[1])):
            passed1 = True
        elif (container[0] == x) and (res[-1] == res[1]):
            passed1 = True

    if (res[-1] == sheep):
        if (container[-1] == o) and (res[-2] == res[0]):
            passed2 = True
        elif (container[-1] == x) and (not (res[-2] == res[0])):
            passed2 = True
    else:
        if (container[-1] == o) and (not (res[-2] == res[0])):
            passed2 = True
        elif (container[-1] == x) and (res[-2] == res[0]):
            passed2 = True
    if passed1 and passed2:
        passed = True
        break

if passed:
    print ''.join(res)
else:
    print -1