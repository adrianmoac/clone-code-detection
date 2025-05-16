#!/usr/bin/env python
#coding:utf-8

def read():
    return map(int, raw_input().split())


def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def matmul(a, b, MOD):
    c = [[0,0],[0,0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % MOD
    return c


def matpow(p, n, MOD):

    if n == 0:
        return [[1,0],[0,1]]

    t = matpow(p, n / 2, MOD)

    return matmul(t, t, MOD) if n % 2 == 0 else matmul(matmul(t, t, MOD), p, MOD)
    

def mypow(p, n, MOD):
    
    if n == 0:
        return 1

    t = mypow(p, n / 2, MOD)
    
    return t * t % MOD if n % 2 == 0 else t * t * p % MOD


def work((A, B, MOD)):
    
    C = gcd(A, B)

    # one(n): 111...111 のように、1 が n 個並んだ整数とする
    # lcm(one(A), one(B)) = one(A) * one(B) / one(C)
    
    # one(A) % MOD を計算
    mat = [[10,1], [0,1]]
    ret1 = matpow(mat, A, MOD)
    
    # (one(B) / one(C)) % MOD を計算
    mat = [[mypow(10, C, MOD),1],[0,1]]
    ret2 = matpow(mat, B / C, MOD)

    # one(A) * (one(B) / one(C)) % MOD を計算
    print ret1[0][1] * ret2[0][1] % MOD


if __name__ == "__main__":
    work(read())
