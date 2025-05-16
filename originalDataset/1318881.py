import math

def ty(h,w):
    lenh=h/2
    if h%2==0:
        #tateb
        tatew = math.ceil(w/3)
        maxb = max(h*tatew, (w-tatew)*lenh)
        minb = min(h*tatew, (w-tatew)*lenh)
        res0 = maxb-minb
        #tates
        if w>3:
            tatew = math.floor(w/3)
            maxb = max(h*tatew, (w-tatew)*lenh)
            minb = min(h*tatew, (w-tatew)*lenh)
        res1 = maxb-minb
    else:
        #tateb
        tatew = math.ceil(w/3)
        maxb = max(h*tatew, (w-tatew)*math.ceil(lenh))
        minb = min(h*tatew, (w-tatew)*math.floor(lenh))
        res0 = maxb-minb
        #tates
        if h>3:
            tatew = math.floor(w/3)
            maxb = max(h*tatew, (w-tatew)*math.ceil(lenh))
            minb = min(h*tatew, (w-tatew)*math.floor(lenh))
        res1 = maxb-minb
    return math.floor(min(res0,res1))

h,w = map(int, input().split())
result = [100000,100000,100000, 100000]

#tate3
if h%3==0:
    result[0] = 0
elif h>3:
    result[0] = w
#yoko3
if w%3==0:
    result[1] = 0
elif w>3:
    result[1] = h

#ト
if w%3==0:
    if h%2==0:
        result[2] = 0
    elif h>2:
        result[2] = math.floor(2*w/3)
else:
    result[2] = ty(h,w)
#T
if h%3==0:
    if w%2==0:
        result[3] = 0
    elif w>2:
        result[3] = math.floor(2*h/3)
else:
    result[3] = ty(w,h)
print(min(result))
