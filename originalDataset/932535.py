import sys
import math
from decimal import Decimal
def gcd(a,b):
    while b>0:
        a,b=b,a%b
    return int(a)
def lcm(a,b):
    return int(a*b/gcd(a,b))

lines = sys.stdin.readlines()
n = int(lines[0])
ret = [1,1]
before_sum = 2
before_ret = [ret[0],ret[1]]
for line in lines[1:]:
    line = line.rstrip().split(" ")
    for l in range(len(line)):
        line[l] = int(line[l])
    #print ("line=",line)
    #print ("ret=",ret)
    #print ("before_sum=",before_sum)
    #print ("before_ret=",before_ret)
    a,b = int(line[0]),int(line[1])
    #before_ret = [ret[0],ret[1]]
    if (ret[0]<=a) and (ret[1]<=b):
        ret[0]=a
        ret[1]=b
    else:
        check_a = Decimal(ret[0])/Decimal(a)
        check_b = Decimal(ret[1])/Decimal(b)
        if (check_a>check_b):
            ret[0]=math.ceil(check_a)*line[0]
            ret[1]=math.ceil(check_a)*line[1]
        elif (check_a<=check_b):
            ret[0]=math.ceil(check_b)*line[0]
            ret[1]=math.ceil(check_b)*line[1]
    #g = gcd(ret[0],ret[1])
    #print (ret[0],ret[1],g)
    #ret[0]=int(ret[0]/g)
    #ret[1]=int(ret[1]/g)
    """
    if (before_sum>(ret[0]+ret[1])):
        #print ("before_sum=",before_sum,ret)
        check_ret = [ret[0],ret[1]]
        i=2
        print ("check:",check_ret,before_ret)
        while((check_ret[0]+check_ret[1])<before_sum):
            check_ret[0]=ret[0]*i
            check_ret[1]=ret[1]*i
            i+=1
        i=2
        while(check_ret[0]<before_ret[0] or check_ret[1]<before_ret[1]):
            check_ret[0]=ret[0]*i
            check_ret[1]=ret[1]*i
            i+=1
        ret[0] = check_ret[0]
        ret[1] = check_ret[1]
        before_sum=ret[0]+ret[1]
    else:
        before_sum=ret[0]+ret[1]
    """


#print (ret)
print (ret[0]+ret[1])
