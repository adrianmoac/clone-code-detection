class UnionFind:
    def __init__(self, size):
        self.table = [-1 for _ in range(size)]
 
    def find(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self.find(self.table[x])
            return self.table[x]
 
    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] <= self.table[s2]:
                self.table[s1] += self.table[s2]
                self.table[s2] = s1
            else:
                self.table[s2] += self.table[s1]
                self.table[s1] = s2
            return True
        return False
 
def cal(d,xl):
    N=len(xl)
    for i in range(N-1):
        r1=abs(xl[i+1][0]-xl[i][0])
        try:
            l=d[r1]
            l.append([xl[i+1][1],xl[i][1]])
            d[r1]=l
        except:
            d[r1]=[[xl[i+1][1],xl[i][1]]]
    return d
N=int(input())
x=[[0,0] for _ in range(N)]
y=[[0,0] for _ in range(N)]
for i in range(N):
    x[i][0],y[i][0]=list(map(int,input().split()))
    x[i][1],y[i][1]=i,i
x=sorted(x,key=lambda l: l[0])
y=sorted(y,key=lambda l: l[0])
a=cal(cal({},x),y)
p=UnionFind(N)
c=0
cost=0
edgecount=0
while True:
    if(edgecount==N-1):
        print(cost)
        break
    try:
        l=a[c]
        for item in l:
            if(p.union(item[0],item[1])):
                cost+=c
                edgecount+=1
            
        c+=1
    except:
        c+=1
        continue