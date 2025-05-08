import sys
readline = sys.stdin.readline
write = sys.stdout.write
flush = sys.stdout.flush

def query(n):
    write("? %d\n" % n)
    flush()
    return readline().strip() == 'Y'
def answer(n):
    write("! %d\n" % n)
    flush()

"""
N = 188
q = 0
def dummy(n, N):
    return ((n <= N and str(n) <= str(N)) or (n > N and str(n) > str(N)))
def query(n):
    global q
    q += 1
    assert q <= 64
    print q, n, N, dummy(n, N)
    return dummy(n, N)
def answer(n):
    print "check", n, N
    assert n == N
"""

dig = None
for i in xrange(10):
    if not query(10**i):
        dig = i
        break
else:
    # 10**k
    for i in xrange(10):
        if query(10**i+1):
            answer(10**i)
            break
    exit(0)

left = 10**(dig-1); right = 10**dig
while left+1 < right:
    mid = (left + right) / 2
    if query(mid*10):
        right = mid
    else:
        left = mid
#print right
answer(right)
