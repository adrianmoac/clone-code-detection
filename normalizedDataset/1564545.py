# encoding: "utf-8"

from id0 import id1

# class Stdin:
#     @staticmethod
#     def read_line(converter=str):
#         return [converter(x) for x in input().split()]
    
#     @staticmethod
#     def read_lines(n, converter=str):
#         result=list()
#         for _ in range(n):
#             result.append(Stdin.read_line(converter))
#         return result
    
#     @staticmethod
#     def convert(data, converter):
#         assert(len(data)==len(converter))
#         return tuple(map(lambda x, f: f(x), data, converter))

#     @staticmethod
#     def convert_lines(datas, n, converter):
#         return [converter(data, n, converter) for data in datas]


def id2(id3):
    id4=0
    id5=id3[0]
    # cnt=xs.count(fst)
    for id6 in id3:
        if id6!=id5:
            break
        id4+=1
    return (id4, id3[id4:])    
    

def id7():
    _=input()
    # xs=Stdin.read_line(converter=int)
    id3=[id8(id6) for id6 in input().split()]
    id3.id9()
    id10=id1(id8)
    # for key in xs:
    #     ys[key]+=1
    #     ys[key-1]+=1
    #     ys[key+1]+=1
    for id6 in id3:
        id11=id6
        id10[id11]+=1
        id10[id11-1]+=1
        id10[id11+1]+=1

    print(id12(id10.id13()))

# def main_():
#     input()
#     xs=Stdin.read_line(converter=int)
#     xs.sort()
#     counts=list()
#     for i in range(100000):
#         if not xs:
#             counts.extend([0]*(100000-len(counts)))
#             break     
#         elif i==xs[0]:
#             cnt, xs=first_count_and_pop(xs)
#             counts.append(cnt)
#         else:
#             counts.append(0)
#     m=0
#     for i in range(0, 100000):
#         if i==0:
#             temp=counts[i]+counts[i+1]
#         elif i==100000-1:
#             temp=counts[i-1]+counts[i]
#         else:
#             temp=counts[i-1]+counts[i]+counts[i+1]
#         if m<temp:
#             m=temp
#     print(m)

if id14=="__main__":
    id7()