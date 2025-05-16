#coding=UTF-8

N=int(input())
moti=list(range(0,N,1))

#initalize
for idx in range(0,N,1):
    moti[idx]=[]

#input
for idx in range(0,N-1,1):
    mozir=input()
    hyo=mozir.split(' ')
    a=int(hyo[0])-1
    b=int(hyo[1])-1

    moti[a].append(b)
    moti[b].append(a)

#path 0 to N-1
#width serach
belong=list(range(0,N,1))
for idx in range(0,N,1):
    belong[idx]=None

belong[0]="F"
belong[N-1]="S"

fennec_watch=[0]
sunuke_watch=[N-1]
fennec_haven=1
sunuke_haven=1
fennec_zou=1 #for breaking cond
sunuke_zou=1 #also
Teban="F"
while True:
    if Teban=="F":
        fennec_next=[]
        for mono in fennec_watch:
            kouho=moti[mono]
            for butu in kouho:
                if belong[butu]==None:
                    fennec_next.append(butu)
                    belong[butu]="F"

        fennec_watch=fennec_next
        fennec_zou=len(fennec_next)
        fennec_haven=fennec_haven+fennec_zou
    else:
        sunuke_next=[]
        for mono in sunuke_watch:
            kouho=moti[mono]
            for butu in kouho:
                if belong[butu]==None:
                    sunuke_next.append(butu)
                    belong[butu]="S"

        sunuke_watch=sunuke_next
        sunuke_zou=len(sunuke_next)
        sunuke_haven=sunuke_haven+sunuke_zou
        
    if fennec_zou==0 and sunuke_zou==0:
        break
    Teban='F' if Teban=='S' else 'S'

#when fennec_haven==sunuke_haven==k
#k+1 th turn fennec 33-4
if fennec_haven > sunuke_haven:
    print('Fennec')
else:
    print('Snuke')
