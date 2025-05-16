from collections import  defaultdict
from collections import deque
import math
N = int(input())

AB = [list(map(int,input().split())) for _ in range(N-1)]


d = defaultdict(list)

for a,b in AB:
    d[a-1].append(b-1)
    d[b-1].append(a-1)


def get_distance(start):
    visited = set([start,])
    distance = [999999999999999999 for _ in range(N)]
    distance[start ] =0
    to_visit = deque([ (1,a) for a in d[start]])

    while to_visit:
        dist,now = to_visit.popleft()
        visited.add(now)
        distance[now]=dist
        for a in d[now]:
            if a not in visited:
                to_visit.append((dist+1,a))

    return distance



a =(get_distance(0))
b= (get_distance(N-1))

distance_ = a[N-1]

def get_close(a,i):
    l = list(sorted([(a[x],x) for x in d[i]]))
    return l[0][1]

tmp = N-1
for i in range((distance_+1)//2-1):
   tmp = get_close(a,tmp)

middle_a = get_close(a,tmp)
middle_b = tmp



x = get_distance(0)
max_ = math.ceil(x[N-1]/2)





d[middle_a].remove(middle_b)
d[middle_b].remove(middle_a)


a_new = (get_distance(0))
b_new = (get_distance(N-1))
"""
print(a)
print(b)
print(middle_a)
print(middle_b)
print(a_new,b_new)
"""
if sum( q<99999999999999999 for q in a_new ) >sum( q<99999999999999999 for q in b_new ):
    print("Fennec")
else:
    print("Snuke")



