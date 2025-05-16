#coding=UTF-8

def search(jun):
    global ans
    global R
    global r
    global rCost
    tmpans=0
    if len(jun)==R:
        mae=jun[0]
        for idx in range(1,R,1):
            ba=jun[idx]
            tmpans += rCost[mae][r[ba]]
            mae=ba

        if ans==None or tmpans<ans:
            ans=tmpans
    else:
        for me in range(0,R,1):
            if not (me in jun):
                search(jun+[me])


mozir=input()
hyo=mozir.split(' ')
N=int(hyo[0])
M=int(hyo[1])
R=int(hyo[2])

mozir=input()
hyo=mozir.split(' ')
r=[(int(mono) -1 ) for mono in hyo]

michi=[]
for idx in range(0,N,1):
    michi.append([])

for idx in range(0,M,1):
    mozir=input()
    hyo=mozir.split(' ')
    A=int(hyo[0])-1
    B=int(hyo[1])-1
    C=int(hyo[2])
    michi[A].append((B,C))
    michi[B].append((A,C))


rCost=[]
for idr in range(0,R,1):
    Cost=[None]*N
    Cost[r[idr]]=0
    miru=[r[idr]]
    while miru:
        nextmiru=[]
        for toshi in miru:
            preCost=Cost[toshi]
            for (saki,sakiCost) in michi[toshi]:
                tmpCost=preCost+sakiCost
                if Cost[saki]==None or tmpCost < Cost[saki]:
                    Cost[saki]=tmpCost
                    nextmiru.append(saki)

        miru=list(set(nextmiru))
    rCost.append(Cost)

#for ko in rCost:
#    print(ko)

ans=None
search([])
print(ans)
