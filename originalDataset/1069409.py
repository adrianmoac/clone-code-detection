#!/usr/bin/env python3

import collections
import functools
import math
import operator


P = 1000000007


def sieve_of_eratosthenes(end):
    assert end > 1
    is_prime = [True for _ in range(end)]
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, end):
        if is_prime[i]:
            primes.append(i)
            for j in range(2 * i, end, i):
                is_prime[j] = False
    return primes


def factorize_fact(n, primes):
    factors = collections.Counter()
    if n < 2:
        return factors
    for p in primes:
        if p * p > n:
            break
        while n % p == 0:
            factors[p] += 1
            n //= p
    if n > 1:
        factors[n] += 1
    return factors


def sum_ctrs(counters):
    return functools.reduce(operator.add, counters, collections.Counter())


def prod_mod(iterable, mod=P):
    def multi_mod(x, y):
        return (x % mod) * (y % mod) % mod
    return functools.reduce(multi_mod, iterable, 1)


def sum_of_divs_of_fact(n, mod=P):
    primes = sieve_of_eratosthenes(math.ceil(math.sqrt(n)) + 1)
    ctr = sum_ctrs(factorize_fact(x, primes) for x in range(1, n + 1))
    ans = prod_mod(v + 1 for v in ctr.values()) % mod
    return ans


def main():
    print(sum_of_divs_of_fact(int(input())))


if __name__ == '__main__':
    main()
