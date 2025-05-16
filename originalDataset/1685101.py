N,K = map(int,input().split())
points1 = []
points2 = []
for i in range(N):
	x,y = tuple((map(int,input().split())))
	points1.append((x,y))
	points2.append(y)
points1.sort()
points2.sort()

xDict = {}
index = 0
for x,y in points1:
	if index in xDict:
		if xDict[index] != x:
			index += 1
			xDict[index] = x
	else:
		xDict[index] = x

yDict = {}
index = 0
for y in points2:
	if index in yDict:
		if yDict[index] != y:
			index += 1 
			yDict[index] = y
	else:
		yDict[index] = y

nPoints = [[0 for j in range(len(yDict))] for i in range(len(xDict))]

for kx,vx in xDict.items():
	for ky,vy in yDict.items():
		exists = 1 if (vx,vy) in points1 else 0
		if kx == 0 and ky == 0:
			nPoints[kx][ky] += exists
		elif kx == 0 and ky > 0:
			nPoints[kx][ky] += nPoints[kx][ky-1] + exists
		elif kx > 0 and ky == 0:
			nPoints[kx][ky] += nPoints[kx-1][ky] + exists
		else:
			nPoints[kx][ky] += nPoints[kx-1][ky] + nPoints[kx][ky-1] - nPoints[kx-1][ky-1] + exists

ans = -1
for x1 in range(len(xDict)):
	for x2 in range(x1+1,-1,-1):
		for y1 in range(len(yDict)):
			for y2 in range(y1+1,-1,-1):
				point = nPoints[x1][y1]
				if x2 > 0:
					point -= nPoints[x2-1][y1]
				if y2 > 0:
					point -= nPoints[x1][y2-1]
				if x2 > 0 and y2 > 0:
					point += nPoints[x2-1][y2-1]
				if point >= K:
					area = (xDict[x1]-xDict[x2]) * (yDict[y1]-yDict[y2])
					if ans < 0:
						ans = area
					else:
						ans = min(ans, area)
					break
print(ans)