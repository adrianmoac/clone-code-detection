import math,string,itertools,fractions,heapq,collections,re,array,bisect,sys,random,time,copy,functools

sys.setrecursionlimit(10**7)
inf = 10**20
mod = 10**9 + 7

def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LI_(): return [int(x)-1 for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def I(): return int(sys.stdin.readline())
def F(): return float(sys.stdin.readline())
def S(): return input()


def main():
    a,b = LI()

    def f(n):
        if n < 4:
            return 0
        a = []
        while n > 0:
            a.append(n%10)
            n //= 10
        a.reverse()
        l = len(a)
        dp = [[[0]*2, [0]*2] for _ in range(l)]
        for i in range(a[0]):
            if i == 4:
                dp[0][1][1] += 1
            else:
                dp[0][1][0] += 1
        if a[0] in [4,9]:
            dp[0][0][1] = 1
        else:
            dp[0][0][0] = 1

        for i in range(1,l):
            ai = a[i]
            if ai in [4,9]:
                dp[i][0][1] = dp[i-1][0][0] + dp[i-1][0][1]
            else:
                dp[i][0][0] = dp[i-1][0][0]
                dp[i][0][1] = dp[i-1][0][1]

            for j in range(ai):
                if j == 4:
                    dp[i][1][1] += sum(dp[i-1][0])
                else:
                    dp[i][1][1] += dp[i-1][0][1]
                    dp[i][1][0] += dp[i-1][0][0]

            for j in range(10):
                if j in [4,9]:
                    dp[i][1][1] += sum(dp[i-1][1])
                else:
                    dp[i][1][1] += dp[i-1][1][1]
                    dp[i][1][0] += dp[i-1][1][0]


        return dp[-1][0][1] + dp[-1][1][1]

    return f(b) - f(a-1)


print(main())
