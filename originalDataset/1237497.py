n = int(input())
a = list(map(int, input().split()))

count = 0
sum_i = a[0]

if a[0] < 0:
    sum_i = 1
    pos_count = 1 - a[0]
    for i in range(1, n):
        if sum_i < 0:
            sum_i += a[i]
            if sum_i <= 0:
                pos_count += 1 - sum_i
                sum_i = 1
        elif sum_i > 0:
            sum_i += a[i]
            if sum_i >= 0:
                pos_count += sum_i + 1
                sum_i = -1
    sum_i = a[0]
    neg_count = 0
    for i in range(1, n):
        if sum_i < 0:
            sum_i += a[i]
            if sum_i <= 0:
                neg_count += 1 - sum_i
                sum_i = 1
        elif sum_i > 0:
            sum_i += a[i]
            if sum_i >= 0:
                neg_count += sum_i + 1
                sum_i = -1
    if neg_count < pos_count:
        count = neg_count
    else:
        count = pos_count
elif a[0] > 0:
    sum_i = a[0]
    pos_count = 0
    for i in range(1, n):
        if sum_i < 0:
            sum_i += a[i]
            if sum_i <= 0:
                pos_count += 1 - sum_i
                sum_i = 1
        elif sum_i > 0:
            sum_i += a[i]
            if sum_i >= 0:
                pos_count += sum_i + 1
                sum_i = -1
    sum_i = -1
    neg_count = 1 + a[0]
    for i in range(1, n):
        if sum_i < 0:
            sum_i += a[i]
            if sum_i <= 0:
                neg_count += 1 - sum_i
                sum_i = 1
        elif sum_i > 0:
            sum_i += a[i]
            if sum_i >= 0:
                neg_count += sum_i + 1
                sum_i = -1
    if neg_count < pos_count:
        count = neg_count
    else:
        count = pos_count
else:
    sum_i = 1
    pos_count = 1
    for i in range(1, n):
        if sum_i < 0:
            sum_i += a[i]
            if sum_i <= 0:
                pos_count += 1 - sum_i
                sum_i = 1
        elif sum_i > 0:
            sum_i += a[i]
            if sum_i >= 0:
                pos_count += sum_i + 1
                sum_i = -1
    sum_i = -1
    neg_count = 1
    for i in range(1, n):
        if sum_i < 0:
            sum_i += a[i]
            if sum_i <= 0:
                neg_count += 1 - sum_i
                sum_i = 1
        elif sum_i > 0:
            sum_i += a[i]
            if sum_i >= 0:
                neg_count += sum_i + 1
                sum_i = -1
    if neg_count < pos_count:
        count = neg_count
    else:
        count = pos_count

print(count)
