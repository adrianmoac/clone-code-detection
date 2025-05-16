# encoding: "utf-8"

from collections import defaultdict

# class Stdin:
#     @staticmethod
#     def read_line(converter=str):
#         return [converter(x) for x in input().split()]
    
#     @staticmethod
#     def read_lines(n, converter=str):
#         result = list()
#         for _ in range(n):
#             result.append(Stdin.read_line(converter))
#         return result
    
#     @staticmethod
#     def convert(data, converter):
#         assert(len(data) == len(converter))
#         return tuple(map(lambda x, f: f(x), data, converter))

#     @staticmethod
#     def convert_lines(datas, n, converter):
#         return [converter(data, n, converter) for data in datas]


def first_count_and_pop(xs):
    cnt = 0
    fst = xs[0]
    cnt = xs.count(fst)
    # for x in xs:
    #     if x != fst:
    #         break
    #     cnt += 1
    return (cnt, xs[cnt:])    
    

def main():
    _ = input()
    # xs = Stdin.read_line(converter=int)
    xs = [int(x) for x in input().split()]
    xs.sort()
    ys = defaultdict(int)
    for key in xs:
        ys[key] += 1
        ys[key-1] += 1
        ys[key+1] += 1

    print(max(ys.values()))

# def main_():
#     input()
#     xs = Stdin.read_line(converter=int)
#     xs.sort()
#     counts = list()
#     for i in range(100000):
#         if not xs:
#             counts.extend([0] * (100000 - len(counts)))
#             break     
#         elif i == xs[0]:
#             cnt, xs = first_count_and_pop(xs)
#             counts.append(cnt)
#         else:
#             counts.append(0)
#     m = 0
#     for i in range(0, 100000):
#         if i == 0:
#             temp = counts[i] + counts[i+1]
#         elif i == 100000 - 1:
#             temp = counts[i-1] + counts[i]
#         else:
#             temp = counts[i-1] + counts[i] + counts[i+1]
#         if m < temp:
#             m = temp
#     print(m)

if __name__ == "__main__":
    main()