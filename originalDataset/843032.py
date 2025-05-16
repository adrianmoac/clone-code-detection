import re


class IO_for_Contest(object):
    @staticmethod
    def my_input():
        return input()

    @staticmethod
    def read_from_input():
        n = IO_for_Contest.read_int()
        return IO_for_Contest.read_n_int(n)

    @staticmethod
    def read_line():
        return IO_for_Contest.my_input().strip()

    @staticmethod
    def read_int():
        return int(IO_for_Contest.my_input().strip())

    @staticmethod
    def read_n_int(n):
        return list(map(
            int,
            re.split('\s+', IO_for_Contest.my_input().strip())))[: n]


def solve():
    a = IO_for_Contest.read_from_input()
    print(min_cost_from_left_to_right(a))


def min_cost_from_left_to_right(a):
    '''
    >>> min_cost_from_left_to_right([100, 150, 130, 120])
    40
    >>> min_cost_from_left_to_right([100, 125, 80, 110])
    40
    >>> a = [314, 159, 265, 358, 979, 323, 846, 264, 338]
    >>> min_cost_from_left_to_right(a)
    310
    '''
    min_cost = prepare_array_of_min_cost(a)
    min_cost_from_left_to_right_inner(a, min_cost)
    return min_cost[-1]


def min_cost_from_left_to_right_inner(a, out_min_cost):
    out_min_cost[0] = 0
    for i in range(1, len(a)):
        for diff in [1, 2]:
            pre = i - diff
            if pre < 0:
                continue
            d = out_min_cost[pre] + abs(a[pre] - a[i])
            out_min_cost[i] = min(out_min_cost[i], d)


def prepare_array_of_min_cost(a):
    MAX = 10000
    MAX_N = 100000
    MAX_TOTAL = MAX * MAX_N
    min_cost = [MAX_TOTAL] * len(a)
    return min_cost

if __name__ == '__main__':
    # import doctest
    # doctest.testmod()
    solve()