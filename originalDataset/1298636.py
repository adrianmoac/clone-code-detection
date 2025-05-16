import sys
h, w = [int(i) for i in input().split()]
h3 = int(h/3)
w3 = int (w/3)
ret = sys.maxsize
# ||| Split
if(h % 3 == 0 or w % 3 == 0):
    ret = 0
a1 = h3 * w
a2 = (h3+1) * w
if(ret > a2 - a1):
    ret = a2 - a1
a1 = w3 * h
a2 = (w3+1) * h
if(ret > a2 - a1):
    ret = a2 - a1
# print("|||:", a2 - a1)
 
# T Split
a1 = h3 * w
a2 = (h-h3) * int(w/2)
if(w % 2 == 1):
    a2 += (h-h3)
a3 = (h-h3) * int(w/2)
amin = a1
if(a1 > a3):
    amin = a3
amax = a2
if(a1 > a2):
    amax = a1
if(ret > (amax - amin)):
    ret = amax - amin
 
# print("T1: ", amax - amin)
 
h31 = h3 + 1
a1 = (h31) * w      # 10
a2 = (h-h31) * int(w/2)  # 6
if(w % 2 == 1):
    a2 += (h-h31) # 9
a3 = (h-h31) * int(w/2)
amin = a1
if(a1 > a3):
    amin = a3
amax = a2
if(a1 > a2):
    amax = a1
if(ret > (amax - amin)):
    ret = amax - amin
 
# print("T2: ", amax - amin, amax, amin)
 
h, w = w, h
h3 = int(h/3)
w3 = int (w/3)
a1 = h3 * w
a2 = (h-h3) * int(w/2)
if(w % 2 == 1):
    a2 += (h-h3)
a3 = (h-h3) * int(w/2)
amin = a1
if(a1 > a3):
    amin = a3
amax = a2
if(a1 > a2):
    amax = a1
if(ret > (amax - amin)):
    ret = amax - amin
 
# print("T3: ", amax - amin)
 
h31 = h3 + 1
a1 = (h31) * w
a2 = (h-h31) * int(w/2)
if(w % 2 == 1):
    a2 += (h-h31)
a3 = (h-h31) * int(w/2)
amin = a1
if(a1 > a3):
    amin = a3
amax = a2
if(a1 > a2):
    amax = a1
if(ret > (amax - amin)):
    ret = amax - amin
 
# print("T4: ", amax - amin)
 
print(int(ret))