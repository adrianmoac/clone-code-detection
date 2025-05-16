def menagerie_2():
	n = int(raw_input())
	ans = str(raw_input())

	def check_possibility(at, a):
		re = ['#']*len(a)
		re[0] = at[0]
		re[1] = at[1]
		for i in range(1, n-1):
			if a[i]=='o':
				if re[i]==1:
					re[i+1] = re[i-1]
				else:
					re[i+1] = re[i-1]*-1
			else:
				if re[i]==1:
					re[i+1] = re[i-1]*-1
				else:
					re[i+1] = re[i-1]

		c1 = False
		c2 = False
		if a[0]=='o':
			if re[0]==1 and (re[1]*re[-1]==1):
				c1 = True
			elif re[0]==-1 and (re[1]*re[-1]==-1):
				c1 = True
		else:
			if re[0]==1 and (re[1]*re[-1]==-1):
				c1 = True
			elif re[0]==-1 and (re[1]*re[-1]==1):
				c1 = True
		if a[-1]=='o':
			if re[-1]==1 and (re[0]*re[-2]==1):
				c2 = True
			elif re[-1]==-1 and (re[0]*re[-2]==-1):
				c2 = True
		else:
			if re[-1]==1 and (re[0]*re[-2]==-1):
				c2 = True
			elif re[-1]==-1 and (re[0]*re[-2]==1):
				c2 = True
		if c1 and c2:
			return re
		else:
			return None

	if check_possibility([1,1], ans) is not None:
		op = ['S' if x == 1 else 'W' for x in check_possibility([1,1], ans)]
		print''.join(op)
	elif check_possibility([1,-1], ans) is not None:
		op = ['S' if x == 1 else 'W' for x in check_possibility([1,-1], ans)]
		print''.join(op)
	elif check_possibility([-1,1], ans) is not None:
		op = ['S' if x == 1 else 'W' for x in check_possibility([-1,1], ans)]
		print''.join(op)
	elif check_possibility([-1,-1], ans) is not None:
		op = ['S' if x == 1 else 'W' for x in check_possibility([-1,-1], ans)]
		print''.join(op)
	else:
		print -1


if __name__ == "__main__":
	menagerie_2()