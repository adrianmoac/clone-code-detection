INF=10**9+7
L=[int(i)-1 for i in input().split()]
x=[int(i)   for i in input().split()]
y=[int(i)   for i in input().split()]
x.sort()
y.sort()

X=[x[i+1]-x[i] for i in range(L[0])]
Y=[y[i+1]-y[i] for i in range(L[1])]

usingX=[0 for i in range(L[0])]
usingY=[0 for i in range(L[1])]

if L[0]%2==0:
	for i in range(L[0]):
		temp=min(i,L[0]-i-1)
		temp+=1
		usingX[i]+=int(temp*(temp+1)/2)
		#print(usingX)
		usingX[i]+=temp*int(L[0]/2-temp)
		#print(usingX)
		usingX[i]*=2
		#print()
else:
	for i in range(L[0]):
		temp=min(i,L[0]-i-1)
		temp+=1
		usingX[i]+=int(temp*(temp+1)/2)
		usingX[i]+=temp*int((L[0]-1)/2-temp)
		usingX[i]*=2
		
		usingX[i]+=temp
	#temp=int((L[0]-1)/2)
	#usingX[temp]-=(temp+1)*2


if L[1]%2==0:
	for i in range(L[1]):
		temp=min(i,L[1]-i-1)
		temp+=1
		usingY[i]+=int(temp*(temp+1)/2)
		#print(usingY)
		usingY[i]+=temp*int(L[1]/2-temp)
		#print(usingY)
		usingY[i]*=2
		#print()
else:
	for i in range(L[1]):
		temp=min(i,L[1]-i-1)
		temp+=1
		usingY[i]+=int(temp*(temp+1)/2)
		usingY[i]+=temp*int((L[1]-1)/2-temp)
		usingY[i]*=2
		
		usingY[i]+=temp
	#temp=int((L[1]-1)/2)
	#usingY[temp]-=(temp+1)*2	

#print(usingX)
#print(usingY)
for i in range(L[0]):
	X[i]*=usingX[i]
for j in range(L[1]):
	Y[j]*=usingY[j]
ans=sum(X)*sum(Y)
print(ans%INF)