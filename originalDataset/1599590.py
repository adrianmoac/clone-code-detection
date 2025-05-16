#!/usr/bin/python

import sys

p=[0]*10000;mp=[];inf=65530060;v=[0]*1000;t=[0]*1000
 
 
ans=100000000

 
n,m,r=map(int,sys.stdin.readline().split(" "))



s=sys.stdin.readline().replace("\n","")

p=map(int,s.split(" "))


def dsss(x,now):
	global ans,v,p,t,mp
	if x==r+1:
		ans=min(ans,now)
		return 
	else :
		for i in range(r):
			if v[p[i]]==0 :
				v[p[i]]=1
				t[x]=p[i]
				if x==1:
					dsss(x+1,now)
				else :
					dsss(x+1,now+mp[p[i]-1][t[x-1]-1])
				v[p[i]]=0
	return 
 
 
for i in range(n+5):
	mp.append(range(n+5))
 
 
for i in range(n+5):
    for j in range(n+5):
            mp[i][j]=inf


for i in range(m):
	a,b,c=map(lambda x: int(x),sys.stdin.readline().split(" ",3))
	a-=1;b-=1;
	mp[a][b]=min(mp[a][b],c)
	mp[b][a]=min(mp[b][a],c)


for i in xrange(n):
	for j in xrange(n):
		for k in xrange(n):
			if mp[j][i]+mp[i][k]<mp[j][k]:
			    mp[j][k]=mp[j][i]+mp[i][k]

dsss(1,0)
 
print ans
