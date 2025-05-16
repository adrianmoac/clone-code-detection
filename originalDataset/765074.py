from Queue import * # Queue, LifoQueue, PriorityQueue
from bisect import * #bisect, insort
from collections import * #deque, Counter,OrderedDict,defaultdict
#set([]) 
import math
import copy
import itertools
import string
import sys
myread = lambda : map(int,raw_input().split())
def cancolor(bd, x, y, H, W):
    dx = [-1,-1,-1,0,0,0,1,1,1]
    dy = [-1,0,1,-1,0,1,-1,0,1]
    for k in xrange(9):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < H and 0 <= ny < W:
            if bd[nx][ny] != '#':
                return False
    return True
def OK(x, y, bd, ans, H, W):
    if bd[x][y] == '.':
        return True
    
    dx = [-1,-1,-1,0,0,0,1,1,1]
    dy = [-1,0,1,-1,0,1,-1,0,1]
    for k in xrange(9):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < H and 0 <= ny < W:
            if ans[nx][ny] == '#':
                return True
            if cancolor(bd, nx, ny, H, W):
                ans[nx][ny] = '#'
                return True
    return False

def solver():
    H, W = myread()
    #bd = [raw_input() for _ in xrange(H)]
    bd = [['.' for i in xrange(W)] for i in xrange(H)]
    for i in xrange(H):
        S = raw_input()
        for j in xrange(W):
            bd[i][j] = S[j]
    ans = [['.' for i in xrange(W)] for i in xrange(H)]
    for i in xrange(H):
        for j in xrange(W):
            if not OK(i,j, bd, ans, H, W):
                print "impossible"
                return
    print "possible"
    for i in xrange(H):
        for j in xrange(W):
            sys.stdout.write(ans[i][j])
        sys.stdout.write('\n')



if __name__ == "__main__":
    solver()
    
