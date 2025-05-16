# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
""" 39.1
a,b,c=map(int, raw_input().split())
print 2*(a*b+b*c+a*c)
"""

import numpy as np

"""39.3
a=raw_input()
if a[1]=="W":
    if a[6]=="W":
        print "Si"
    else:
        print "Mi"
elif a[11]=="W":
    if a[5]=="W":
        print "Do"
    else: 
        print "Fa"
else:
    if a[3]=="B":
        print "So"
    elif a[9]=="B":
        print "La"
    else:
        print "Re"   
"""

h,w=map(int, raw_input().split())
a=[]
a.append(list('#'*(w+2)))
for i in range(h):
    inp=raw_input()
    a.append(['#']+list(inp)+['#'])
a.append(list('#'*(w+2)))
a=np.array(a)
b=a.copy()
for i in  range(1,h+1):
    for j in range(1,w+1):
        if a[i][j]==".":
            b[i+1][j+1]=b[i-1][j-1]=b[i-1][j+1]=b[i][j-1]=b[i][j+1]=b[i-1][j]=b[i+1][j]=b[i+1][j-1]="."
#    if a[i][0]==".":
#        b[i+1][0]=b[i-1][0]=b[i][1]=b[i+1][1]=b[i-1][1]="."
#    if a[i][w-1]==".":
#        b[i+1][w-1]=b[i-1][w-1]=b[i][w-2]=b[i+1][w-2]=b[i-1][w-2]="."
#    if a[0][i]==".":
#        b[0][i-1]=b[0][i+1]=b[1][i]=b[1][i+1]=b[1][i-1]="."
#    if a[w-1][i]==".":
#        b[w-1][i-1]=b[w-1][i+1]=b[w-2][i]=b[w-2][i+1]=b[w-2][i-1]="."
#
#if a[0][0]==".":
#    b[0][1]=b[1][1]=b[1][0]="."
#if a[0][w-1]==".":
#    b[1][w-1]=b[1][w-2]=b[0][w-2]="."
#if a[h-1][0]==".":
#    b[h-1][1]=b[h-2][0]=b[h-2][1]="."
#if a[h-1][w-1]==".":
#    b[h-2][w-1]=b[h-1][w-2]=b[h-2][w-2]="."
c=b.copy()
for i in  range(1,h+1):
    for j in range(1,w+1):
        if b[i][j]=="#":
            c[i+1][j+1]=c[i-1][j-1]=c[i-1][j+1]=c[i][j-1]=c[i][j+1]=c[i-1][j]=c[i+1][j]=c[i+1][j-1]="#"
#    if b[i][0]=="#":
#        c[i+1][0]=c[i-1][0]=c[i][1]=c[i+1][1]=c[i-1][1]="#"
#    if b[i][w-1]=="#":
#        c[i+1][w-1]=c[i-1][w-1]=c[i][w-2]=c[i+1][w-2]=c[i-1][w-2]="#"
#    if b[0][i]=="#":
#        c[0][i-1]=c[0][i+1]=c[1][i]=c[1][i+1]=c[1][i-1]="#"
#    if b[w-1][i]=="#":
#        c[w-1][i-1]=c[w-1][i+1]=c[w-2][i]=c[w-2][i+1]=c[w-2][i-1]="#"
#
#if b[0][0]=="#":
#    c[0][1]=c[1][1]=c[1][0]="#"
#if b[0][w-1]=="#":
#    c[1][w-1]=c[1][w-2]=c[0][w-2]="#"
#if b[h-1][0]=="#":
#    c[h-1][1]=c[h-2][0]=c[h-2][1]="#"
#if b[h-1][w-1]=="#":
#    c[h-2][w-1]=c[h-1][w-2]=c[h-2][w-2]="#"
if (c[1:-1,1:-1]==a[1:-1,1:-1]).all():
    print "possible"
    for i in range(1,h+1):
        print ''.join(b[i,1:-1])
else:
    print "impossible"