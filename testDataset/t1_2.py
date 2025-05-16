from collections import defaultdict
class UnionFind:
    def __init__(self,size):
        self.parent=range(size)
        self.tree_num=size
        self.tree_w=[1]*size
        self.rank=[0]*size

    def findset(self,x):
        if self.parent[x]==x:
            return x
        else:
            self.parent[x]=self.findset(self.parent[x])
            return self.parent[x]

    def unite(self,x,y):
        x=self.findset(x)
        y=self.findset(y)
        if x==y:
            return
        if self.rank[x]<self.rank[y]:
            self.parent[x]=y
            self.tree_num-=1
            self.tree_w[y]+=self.tree_w[x]
        else:
            self.parent[y]=x
            self.tree_num-=1
            self.tree_w[x]+=self.tree_w[y]
            if self.rank[x]==self.rank[y]:
                self.rank[x]+=1

    def same(self,x,y):
        if self.findset(x)==self.findset(y):
            return True
        else:
            return False

    def tree_number(self):
        return self.tree_num

    def tree_weight(self,x):
        return self.tree_w[self.findset(x)]

n,k,l=map(int,raw_input().split())
uf1=UnionFind(n)
uf2=UnionFind(n)
for i in xrange(k):
    p,q=map(int,raw_input().split())
    p-=1;q-=1
    uf1.unite(p,q)
for i in xrange(l):
    p,q=map(int,raw_input().split())
    p-=1;q-=1
    uf2.unite(p,q)
cnt=defaultdict(int)
for i in xrange(n):
    cnt[(uf1.findset(i),uf2.findset(i))]+=1
ans=[0]*n
for i in xrange(n):
    ans[i]+=cnt[(uf1.findset(i),uf2.findset(i))]
print (" ").join(map(str,ans))
