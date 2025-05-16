# coding=utf-8


# x,a,b=map(int, input().split())
# if abs(x-a)<abs(x-b):
#     print('A')
# else :
#     print('B')

#BBBBBBBBB
# hoge=[0]*26
# a=ord('a')
# string=input()
# for i in range(len(string)):
#     hoge[ord(string[i])-a]=1

# for i in range(26):
#     if hoge[i]==0:
#         print(chr(i+a))
#         break
#     if i==25:
#         print('None')


###CCCC

id0=map(id1, input().split())
id2=map(id1, input().split())
id2=id3(id2,id4=True)
# print(A)
id5=id2[0]
id6=0
id7=False
id8=0
# print(range(1,len(A)-1))
for id9 in id10(1,id11(id2)-1):
    # print('i={}'.format(i))
    if id9==id8:
        # print('cont')
        continue
    else:
        if id7==False:
            if id2[id9]==id5 :
                id7=True
                id6=id2[id9+1]
                id8=id9+1
                # print('skip={}'.format(skip))
            else :
                id5=id2[id9] 
        else:
            if id2[id9]==id6 :
                # print('break')
                break
            else:
                id6=id2[id9]
        if id9==id10(1,id11(id2)-1)[-1]:
            id6=0

print(id5*id6)
