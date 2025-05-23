#coding=UTF-8

# 基本的に N=1 seq=[K] であれば簡単だった
# 全体では毎回 N減って N-1増えるのできっと収束する
# もし、2本立てると

# 7 7
# 5 8
# 6 6
# 4 7
# 5 5
# 3 6
# 4 4
# 2 5
# 3 3
# 1 4
# 2 2
# 0 3
# 1 1 done! の12回

# f(0,0)=0
# f(1,1)=0
# f(2,2): -> 0,3 -> 1,1 =2
# f(3,3): -> 1,4 -> 2,2 + f(2,2) = 4
# f(4,4): -> 2,5 -> 3,3 + f(3,3) = 6
# f(5,5): -> 3,6 -> 4,4 + f(4,4) = 8 ...

# f(A,A)=(A-1)*2 (A>=1)

# f(2,2,2)=0
# f(3,3,3): -> 0,4,4 -> 1,1,5 -> 2,2,2 =3
# K=1のときは
#  3,0 -> 1,1 ok (非負)

# N=50にするのがつよそう
# 最大の余りは49なので
# 49個が1回ずつ殴られるパターン
# L+50-48 L+50-48 ... L+50-48 L-49 が49回後には
# L L L ... となる
# これが合法手になるのはL>=49のときである

# f([49]*50)=0
# f([50]*50)= 50 + f([49]*50)=50
# f([L]*50)=50*(L-49) (for L >= 49)

# K=50*(10**16)-1 では
# L-49=10**16-1
# L=10**16+48
# L+50-48=10**16 + 50 ok
K=int(input())
print(50)
L=K//50+49
amari=K%50
ansstr=''
#extra amari times
for idx in range(0,50,1):
    if idx < amari:
        ansstr+=str(L+50-(amari-1))+' '
    else:
        ansstr+=str(L-amari)+' '

print(ansstr[0:len(ansstr)-1])

