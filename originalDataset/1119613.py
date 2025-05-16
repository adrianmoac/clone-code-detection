def compare(a, b): # a also b are both string
	l = max(len(a), len(b))
	a_ = a.rjust(l, '0')
	b_ = b.rjust(l, '0')
	return a_ > b_

def divide(num, den): # den is integer
	quo = ''; resi = 0
	digit = len(num) if int(num[0]) >= den else len(num)-1
	for i in range(len(num)):
		temp = (int(num[i])+resi*10)//den
#		print('dtemp', temp)
		resi = (int(num[i])+resi*10)%den
#		print('dresi', resi)
		quo += str(temp)
	return quo

def multi(a, n):
	s = ''; resi = 0
	for i in range(len(a))[::-1]:
		temp = (int(a[i])*n + resi)%10
#		print('mltemp', temp)
		resi = (int(a[i])*n + resi)//10
#		print('mlresi', resi)
		s = str(temp) + s
	return s


def plus(a, b):
	l = max(len(a), len(b))
	a_ = a.rjust(l, '0')
	b_ = b.rjust(l, '0')

	s = ''; resi = 0
	for i in range(l)[::-1]:
		temp = (int(a_[i]) + int(b_[i]) + resi)%10
#		print('ptemp', temp)
		resi = (int(a_[i]) + int(b_[i]) + resi)//10
#		print('presi', resi)
		s = str(temp) + s
	return s

# a is higher than b
def minus(a, b):
	l = max(len(a), len(b))
	a_ = a.rjust(l, '0')
	b_ = b.rjust(l, '0')

	s = ''; bollow = 0
	for i in range(l)[::-1]:
		temp = int(a_[i]) - int(b_[i]) - bollow
#		print('mitemp', temp)
		bollow = 0
		if temp >= 0:
			s = str(temp) + s
		else:
			bollow = 1
			s = str(temp + 10) + s
	return s


s, c = input().split()
if compare(s, divide(c, 2)) or s == c:
	print(int(divide(c, 2)))
else:
	print(int(plus(s, divide(minus(c, multi(s, 2)), 4))))
