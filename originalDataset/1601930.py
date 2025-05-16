import sys

# sys.stdin = open('c1.in')


def read_int_list():
    return list(map(int, input().split()))


def read_str_list():
    return input().split()


def read_int():
    return int(input())


def read_str():
    return input()


def main():
    a, b, c, d, e, f = read_int_list()
    best_water = 100 * a
    best_sugar = 0
    i = 0
    while 100 * i * a <= f:
        j = 0
        while 100 * i * a + 100 * j * b <= f:

            water = 100 * i * a + 100 * j * b
            k = 0
            while water + k * c <= f and k * c <= e * (i * a + j * b):

                l1 = int((f - water - k * c) / d)
                l2 = int((e * (i * a + j * b) - k * c) / d)
                l = min(l1, l2)
                if (i, j, k, l) != (0, 0, 0, 0):
                    if True:
                        # rapide
                        sugar = k * c + l * d
                        total = water + sugar
                        density = sugar / total
                        best_total = best_sugar + best_water
                        best_density = best_sugar / best_total
                        if density > best_density:
                            best_sugar = sugar
                            best_water = water
                    else:
                        # trop lent
                        l = 0
                        while water + k * c + l * d <= f and k * c + l * d <= e * (i * a + j * b):
                            if (i, j, k, l) == (0, 0, 0, 0):
                                continue
                            sugar = k * c + l * d
                            total = water + sugar
                            density = sugar / total
                            best_total = best_sugar + best_water
                            best_density = best_sugar / best_total
                            if density > best_density:
                                best_sugar = sugar
                                best_water = water
                            l += 1
                k += 1
            j += 1
        i += 1

    print(best_water + best_sugar, best_sugar)


main()
