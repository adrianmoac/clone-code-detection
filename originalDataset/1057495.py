Sx, Sy, Tx, Ty = map(int, input().split())

first_x = Tx - Sx
first_y = Ty - Sy

ans1_list = []

if first_y > 0:
	ans1_list.append('U'*first_y)
	if first_x > 0:
		ans1_list.append('R'*first_x)
	else:
		ans1_list.append('L'*first_x)


else:
	print('D'*first_y)
	if first_x > 0:
		ans1_list.append('R'*first_x)
	else:
		ans1_list.append('L'*first_x)

ans1_list_ = "".join(ans1_list)
#ans2_list_ = "".join(ans2_list)

count1_list = []

#ans_list = ans1_list_ + ans2_list_

for s in ans1_list_:
	if s == 'U':
		count1_list.append('D')
	elif s == 'D':
		count1_list.append('U')
	elif s == 'R':
		count1_list.append('L')
	elif s == 'L':
		count1_list.append('R')

ans1_list = ans1_list_ + "".join(count1_list)

ans2_list = []

if "".join(ans1_list)[0] == 'U':
	ans2_list.append('L')
	ans2_list.append('U')
	ans2_list.append("".join(ans1_list_))
	ans2_list.append('R')
	ans2_list.append('D')

elif "".join(ans1_list)[0] == 'R':
	ans2_list.append('U')
	ans2_list.append('R')
	ans2_list.append("".join(ans1_list_))
	ans2_list.append('D')
	ans2_list.append('L')

elif "".join(ans1_list)[0] == 'D':
	ans2_list.append('R')
	ans2_list.append('D')
	ans2_list.append("".join(ans1_list_))
	ans2_list.append('L')
	ans2_list.append('U')
elif "".join(ans1_list)[0] == 'L':
	ans2_list.append('D')
	ans2_list.append('L')
	ans2_list.append("".join(ans1_list_))
	ans2_list.append('U')
	ans2_list.append('R')

ans2_list_ = "".join(ans2_list)

count_list = []

ans_list = ans1_list + ans2_list_

for s in ans2_list_:
	if s == 'U':
		count_list.append('D')
	elif s == 'D':
		count_list.append('U')
	elif s == 'R':
		count_list.append('L')
	elif s == 'L':
		count_list.append('R')


count_ = "".join(count_list)
ans_list = "".join(ans_list) + count_

ans = ans_list
print(ans)