# -*- coding: utf-8 -*-
#Python
import sys

N=input()
adj=[[] for i in range(N+1)]

#隣接リスト
for i in range(N-1):
    x,y=list(map(int,raw_input().split()))
    adj[x].append(y)
    adj[y].append(x)

#print adj

#訪問判別フラグ
F=(N+1)*[0]

#Stack
S=[]

#距離
dist=(N+1)*[0]


#先頭から深さ優先探索
S.append(1)
while len(S) != 0:
	#print S
	v=S.pop()
	#print v
	
	if F[v]==0:
		F[v]=1
		#print F
		for u in adj[v]:
			#print "u::"+str(u)
			if F[u]==0:
				S.append(u)
				dist[u]=dist[v]+1
				#print S

#print dist



#訪問判別フラグ
F=(N+1)*[0]

#Stack
S=[]

#距離
dist2=(N+1)*[0]

#最後から深さ優先探索
S.append(N)
while len(S) != 0:
	#print S
	v=S.pop()
	#print v
	
	if F[v]==0:
		F[v]=1
		#print F
		for u in adj[v]:
			#print "u::"+str(u)
			if F[u]==0:
				S.append(u)
				dist2[u]=dist2[v]+1
				#print S

#print dist2



f_p=0
s_p=0
for k in range(1,N+1):
	if dist[k]<=dist2[k]:
		f_p+=1
	else:
		s_p+=1


if f_p>s_p:
	print 'Fennec'
else:
	print 'Snuke'
