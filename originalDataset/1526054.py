# coding=utf-8


# x,a,b = map(int, input().split())
# if abs(x-a) < abs(x-b):
#     print('A')
# else :
#     print('B')

#BBBBBBBBB
# hoge = [0] * 26
# a = ord('a')
# string = input()
# for i in range(len(string)):
#     hoge[ord(string[i])-a] = 1

# for i in range(26):
#     if hoge[i] == 0:
#         print(chr(i+a))
#         break
#     if i == 25:
#         print('None')


###CCCC

n = map(int, input().split())
A = map(int, input().split())
A = sorted(A,reverse = True)
# print(A)
e1 = A[0]
e2 = 0
hoge = False
skip = 0
# print(range(1,len(A)-1))
for i in range(1,len(A)-1):
    # print('i={}'.format(i))
    if i == skip:
        # print('cont')
        continue
    else:
        if hoge == False:
            if A[i] == e1 :
                hoge = True
                e2 = A[i+1]
                skip = i+1
                # print('skip={}'.format(skip))
            else :
                e1 = A[i] 
        else:
            if A[i] == e2 :
                # print('break')
                break
            else:
                e2 = A[i]
        if i == range(1,len(A)-1)[-1]:
            e2 = 0

print(e1*e2)

