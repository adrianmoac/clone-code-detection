#!/usr/bin/python3
import sys

a, k = input().split()
a = list(map(int, a))
k = int(k)
d = list(map(int, input().split()))
avail = list(set(range(10)) - set(d))
avail.sort()

print('a={}'.format(a), file=sys.stderr)
print('avail={}'.format(avail), file=sys.stderr)

n = len(a)

def calc(a):
    res = 0
    for x in a:
        res *= 10
        res += x
    return res

# i桁目を決めたい
# flag: もう超えてる? フラグ
def dfs(a, i, flag):
    print('a={}, i={}, flag={}'.format(a, i, flag), file=sys.stderr)
    if i == n:
        return a

    if a[i] in avail:
        return dfs(a, i+1, flag)
    else:
        if flag:
            a[i] = min(avail)
            return dfs(a, i+1, flag)

        arr = [val for val in avail if val > a[i]]
        if arr:
            a[i] = min(arr)
            return dfs(a, i+1, True)
        else:
            if i > 0:
                arr2 = [val for val in avail if val > a[i-1]]
                if arr2:
                    a[i-1] = min(arr2)
                    a[i] = min(avail)
                    return dfs(a, i+1, True)
                else:
                    raise Exception('not impl')
            else:
                a[i] = min(set(avail) - set([0])) * 10 + min(avail)
                return dfs(a, i+1, True)






try:
    resArr = dfs(a, 0, False)
except Exception as ex:
    print(ex, file=sys.stderr)
    resArr = [min(set(avail) - set([0]))] + [min(set(avail))] * (n-1)
    if calc(resArr) <  calc(a):
        resArr[0] = min(set(avail) - set([0])) * 10 + min(avail)


    
print(resArr, file=sys.stderr)
res = calc(resArr)

print(res)
