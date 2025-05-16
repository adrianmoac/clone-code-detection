def rnd(x,d=1):
    p=10**d
    return (x*p*2+1)//2/p

def aaa(a):

    n = a / 10.0
    if 11.25 <= n < 33.75:
        ret = 'NNE'
    elif 33.75 <= n < 56.25:
        ret = 'NE'
    elif 56.25 <= n < 78.75:
        ret = 'ENE'
    elif 78.75 <= n < 101.25:
        ret = 'E'
    elif 101.25 <= n < 123.75:
        ret = 'ESE'
    elif 123.75 <= n < 146.25:
        ret = 'SE'
    elif 146.25 <= n < 168.75:
        ret = 'SSE'
    elif 168.75 <= n < 191.25:
        ret = 'S'
    elif 191.25 <= n < 213.75:
        ret = 'SSW'
    elif 213.75 <= n < 236.25:
        ret = 'SW'
    elif 236.25 <= n < 258.75:
        ret = 'WSW'
    elif 258.75 <= n < 281.25:
        ret = 'W'
    elif 281.25 <= n < 303.75:
        ret = 'WNW'
    elif 303.75 <= n < 326.25:
        ret = 'NW'
    elif 326.25 <= n < 348.75:
        ret = 'NNW'
    else:
        ret = 'N'

    return ret

def bbb(b):
    n = rnd(b / 60.0)

    if n <= 0.2:
        ret = 0
    elif n <= 1.5:
        ret = 1
    elif n <= 3.3:
        ret = 2
    elif n <= 5.4:
        ret = 3
    elif n <= 7.9:
        ret = 4
    elif n <= 10.7:
        ret = 5
    elif n <= 13.8:
        ret = 6
    elif n <= 17.1:
        ret = 7
    elif n <= 20.7:
        ret = 8
    elif n <= 24.4:
        ret = 9
    elif n <= 28.4:
        ret = 10
    elif n <= 32.6:
        ret = 11
    else:
        ret = 12

    return ret


lst = input().split(" ")
a = int(lst[0])
b = int(lst[1])

ret1 = aaa(a)
ret2 = bbb(b)

if ret2 == 0:
    print("C 0")
else:
    print("{0} {1}".format(ret1, ret2))