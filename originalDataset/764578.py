size = raw_input().split(" ")
h = int(size[0])
w = int(size[1])

img = []

for y in range(h):
	img.append(raw_input())


img2 = []

for y in range(h):
	line = ""
	for x in range(w):
		if img[y][x] == "#":
			flag = False
			for i in range(3):
				for j in range(3):

					if (x+(j-1) >= 0) and (x+(j-1) < w) and (y+(i-1) >= 0) and (y+(i-1) < h) and (img[y+i-1][x+j-1] == "."):
						flag = True
			if flag == True:
				line += "."
			else:
				line += "#"

		else:
			line += "."
	img2.append(line)


##############################


img3 = []

for y in range(h):
	line = ""
	for x in range(w):
		if img2[y][x] == ".":
			flag = False
			for i in range(3):
				for j in range(3):
					if (x+(i-1) >= 0) and (x+(i-1) < w) and (y+(j-1) >= 0) and (y+(j-1) < h) and (img2[y+(j-1)][x+(i-1)] == "#"):
						flag = True
						break
			if flag == True:
				line += "#"
			else:
				line += "."

		else:
			line += "#"
	img3.append(line)

#################################

flag = True
for y in range(h):
	for x in range(w):
		if img[y][x] != img3[y][x]:
			flag = False
			break

if flag == True:
	print "possible"
	for y in range(h):
		print img2[y]
else:
	print "impossible"



