n, k = map(int, input().split())
d = [int(i) for i in input().split()]
ablenum = [int(i) for i in range(10)]
lis_n = str(n)
lis_n = list(lis_n)

#print(lis_n)

# 使用可能な数一覧
for i in d:
    ablenum.remove(i)

#print(ablenum)

flag_bigdigit = -1

# max(ablenum)より大きい桁があるかどうか
for i in range(len(lis_n)):
    _i = len(lis_n) - i - 1
    if(int(lis_n[_i]) > max(ablenum)):
        flag_bigdigit = _i
        break

#  max(ablenum)より大きい桁があれば
if(flag_bigdigit != -1):
    flag_increaseDights = 1
    #  桁を増やす必要があるかどうか確認
    for i in range(flag_bigdigit-1, 0):
        # nの桁より大きい数字がablenumに存在していれば桁を増やす必要はない
        if(int(lis_n[i]) < max(ablenum)):
            flag_increaseDights = 0
            break
else:
    flag_increaseDights = 0

#print("bigdigit:{0} increace:{1}".format(flag_bigdigit, flag_increaseDights))

ans = ""
# 桁を増やす必要があるならば
if(flag_increaseDights == 1):
    for i in range(len(lis_n)+1):
        # 一桁目は0以外の最も小さな数
        if(i == 0):
            mnum = min(ablenum)
            if(mnum == 0):
                mnum = ablenum[1]
            ans += str(mnum)
        # 2桁目以降は最も小さい数
        else:
            mnum = min(ablenum)
            ans += str(mnum)
# 桁を増やす必要がなければ、各桁の数字以上の最も小さい数を使う
else:
    flag_over = 0
    for i in range(len(lis_n)):
        if(flag_over == 0):
            mnum = min(ablenum)
            # その桁以上の数になるまで大きくする
            j = 0
            while mnum < int(lis_n[i]):
                #print("mnum:{0} j:{1}".format(mnum, j))
                j += 1
                mnum = ablenum[j]
            if(mnum > int(lis_n[i])):
                flag_over = 1
            ans += str(mnum)
        else:
            mnum = min(ablenum)
            ans += str(mnum)

print(ans)
