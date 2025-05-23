def C_123sub(N, NG):
    """
    n:nから1,2,3のどれかを引いていき、0にできればOK
    ng:引いていく際にこのリストの要素と一致してはいけない
    """
    if N in NG:
        return 'NO'

    ng_list = sorted(NG)[::-1]
    n = N

    cycle = 99
    while cycle >= 0:
        tmp = n
        i, j, k = tmp - 1, tmp - 2, tmp - 3

        is_ng=['0','0','0']
        for idx,e in enumerate([i,j,k]):
            if e in ng_list:
                is_ng[idx]='1'
        p=''.join(is_ng)

        if p=='000':
            if i==0:
                n=i
            elif j==0:
                n=j
            elif k==0:
                n=k
            else:
                n=k
        elif p=='001':
            if i==0:
                n=i
            elif j==0:
                n=j
            else:
                n=j
        elif p=='010':
            if i==0:
                n=i
            elif k==0:
                n=k
            else:
                n=k
        elif p=='011':
            n=i
        elif p=='100':
            if j==0:
                n=j
            elif k==0:
                n=k
            else:
                n=k
        elif p=='101':
            n=j
        elif p=='110':
            n=k
        elif p=='111':
            return 'NO'

        if n == 0:
            return 'YES'
        cycle -= 1
    return 'NO'

N = int(input())
NG = [int(input()) for i in range(3)]
print(C_123sub(N, NG))