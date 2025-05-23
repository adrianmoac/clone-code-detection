# -*- coding: utf-8 -*-
"""
"""
#


def solve(line1, line2):
    seq = []
    if len(line1) == 0:
        return 0
    elif len(line1) == 1:
        return 3
    else:
        prev_mark = line1[0]
        for m in line1[1:]:
            if prev_mark is None:
                prev_mark = m
                continue
            if m == prev_mark:
                seq.append('h')
                prev_mark = None
            else:
                seq.append('v')
                prev_mark = m
        if prev_mark:
            seq.append('v')

    if len(seq) == 1:
        return 6
    if seq[0] == 'h':
        ans = 6
        prev_p = 'h'
    else:
        ans = 3
        prev_p = 'v'

    for d in seq[1:]:
        if prev_p == 'h' and d == 'h':
            ans *= 3
            prev_p = 'h'
        elif prev_p == 'h' and d == 'v':
            prev_p = 'v'
        elif prev_p == 'v' and d == 'h':
            ans *= 2
            prev_p = 'h'
        else:
            ans *= 2
            prev_p = 'v'
    return ans % 1000000007




def main():
    n = int(input())
    line1 = input()
    line2 = input()
    result = solve(line1, line2)
    print(result)




if __name__ == '__main__':
    main()
    
