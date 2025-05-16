# -*- coding: utf-8 -*-
import sys


N=input()


a=[[] for i in range(N+1)]

#隣接リスト
for i in range(N-1):
	x,y,z=list(map(int,raw_input().split()))
	a[x].append((y,z))
	a[y].append((x,z))

#print a
	

Q,K=list(map(int,raw_input().split()))


b=[]
for i in range(Q):
	b.append(map(int, raw_input().split()))
#print b



#訪問判別フラグ
F=(N+1)*[0]

#Stack
S=[]

#距離
dist=[0 for i in range(N+1)]

#先頭から深さ優先探索
S.append(K)
former_v=0
v=0
while len(S) != 0:
	v=S.pop()
	
	if F[v]==0:
		F[v]=1

		for u,length in a[v]:
			if F[u]==0:
				S.append(u)
				dist[u]=dist[v]+length
				#print dist

#print dist



for x in range(len(b)):

	print dist[ b[x][0] ]+ dist[ b[x][1] ]
