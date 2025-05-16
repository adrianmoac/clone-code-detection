n = int(raw_input())
s = raw_input()

def fill():
    for i in range(n-2):
        c = s[i]
        if a[i] == 0: # hituji
            if c == 'o':
                a[i+1] = a[i-1]
            else:
                a[i+1] = a[i-1] ^ 1
        else: # ookami
            if c == 'o':
                a[i+1] = a[i-1] ^ 1
            else:
                a[i+1] = a[i-1]

def isTrue(i):
    flag = False
    if a[i] == 0:
        if s[i] == 'o' and a[i-1] == a[(i+1)%n]:
            flag = True
        elif s[i] == 'x' and a[i-1] != a[(i+1)%n]:
            flag = True
    else:
        if s[i] == 'o' and a[i-1] != a[(i+1)%n]:
            flag = True
        elif s[i] == 'x' and a[i-1] == a[(i+1)%n]:
            flag = True
    return flag

def convert():
    ret = ""
    for v in a:
        if v == 0:
            ret += 'S'
        else:
            ret += 'W'
    return ret

a = [0] * n

a[-1] = 0 # hituji
a[0]  = 0 # hituji
fill()
if isTrue(n-2) and isTrue(n-1):
    print convert()
    exit()

a[-1] = 0 # hituji
a[0]  = 1 # ookami
fill()
if isTrue(n-2) and isTrue(n-1):
    print convert()
    exit()

a[-1] = 1 # ookami
a[0]  = 1 # ookami
fill()
if isTrue(n-2) and isTrue(n-1):
    print convert()
    exit()

a[-1] = 1 # ookami
a[0]  = 0 # hituji
fill()
if isTrue(n-2) and isTrue(n-1):
    print convert()
    exit()

print -1