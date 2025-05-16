#coding=UTF-8

import id0
#if digit(a)==digit(b) then
# a<=b<=>a<=_{str} b
# easy nomal

# 1. serch digit(N)
# 2. serch N

#note '0'<'1'<'2'

# utopian when N=123
# ? 1=>Y
# ? 12=>Y
# ? 123=>Y
# ? 1230=>N

# most cases
# ? 100=>Y
# ? 1000=>N
#==>3 digits!# when N=10^c
# no jump (...,{<=,<=_{str}},{>,>_{str}},...)
#=>Try 9,99,999,9999,...
# or 11 101 1001 whatsoever...
# always str(N)<='9'*c

# ? 10**18 is allowed tho N<10**9
# 1 10 100 1000,... are least str for most N (n<=_{str} N)
# In such case, 2nd cond is never true

id1=None
for id2 in id3(0,11,1):
    print("? 1"+"0"*id2)
    id0.id4.id5()
    id6=input()
    if id6=="N":
        id7=id2
        break
else:
    # 10**c case
    for id2 in id3(1,11,1):
        print("? "+"9"*id2)
        id0.id4.id5()
        id6=input()
        if id6=="Y":#no cross
            id8=id2-1
            break
    id1="!1"+"0"*id8

if id1==None:
    #other case
    #To fix one cmp, query str(guess_number)+'0'
    #so that always n>N

    # if responce=='Y'
    # myon+'0'>_{str} N
    # i.e. myon>=N (note that boundary)
    id9=10**(id7-1) # known highest false
    id10=10**(id7)-1 # known lowest true
    while id10-id9>1: # i.e. #not_sure!=0
        id11=(id10+id9)//2
        print("? "+id12(id11)+"0")
        id0.id4.id5()
        id6=input()
        if id6=="Y":
            id10=id11
        else:
            id9=id11

    id1="!"+id12(id10)
            

print(id1)