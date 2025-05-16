#coding=UTF-8

siri=[]
def tansaku(kousei,depth,tmpans):
    global siri
    global N

    if depth==N:
        nin=0
        if habatup(kousei):
            nin=sum(kousei)
        return max(nin,tmpans)
    else:
        kaeshi=0
        if habatup(kousei+[1]):
            kaeshi=tansaku(kousei+[1],depth+1,max(tmpans,sum(kousei)+1))

        kaeshi=max(tansaku(kousei+[0],depth+1,tmpans),kaeshi)
        return kaeshi

def habatup(hito):
    zin_list=[]
    for idx in range(0,len(hito),1):
        if hito[idx]==1:
            zin_list.append(idx)

    return nakayoship(zin_list)

def nakayoship(lst):
    if len(lst)<=1:
        return True
    else:
        atama=lst[0]
        rest=lst[1:len(lst)]
        kaeshi=True
        for hito in rest:
            if siri[hito][atama]==False:
                return False
        return nakayoship(rest)

mozir=input()
hyo=mozir.split(' ')

N=int(hyo[0])
M=int(hyo[1])

rel=[]
for idx in range(0,M,1):
    mozir=input()
    hyo=mozir.split(' ')
    rel.append((int(hyo[0])-1,int(hyo[1])-1))


for idx in range(0,N,1):
    siri.append([False]*N)

for mono in rel:
    siri[mono[0]][mono[1]]=True
    siri[mono[1]][mono[0]]=True

ans=tansaku([],0,0)
print(ans)
