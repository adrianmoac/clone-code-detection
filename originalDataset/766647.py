#coding=UTF-8
#9マス黒塗りスタンプで塗れるかどうかじゃないかな


def nurip(x,y):
    if x<0 or x>=W:
        return True
    elif y <0 or y>=H:
        return True
    else:
        return (True if S[y][x]=='#' else False)

def printba(ba):
    for idy in range(0,H,1):
        demoji=''
        for idx in range(0,W,1):
            demoji=demoji+ba[idy][idx]
        print(demoji)
            
mojir=input()
hyo=mojir.split(' ')
H=int(hyo[0])
W=int(hyo[1])

S=[]
for idx in range(0,H,1):
    S.append(input())

#更地
kouho=list(range(0,H,1))
for idy in range(0,H,1):
    kouho[idy]=list(range(0,W,1))
    for idx in range(0,W,1):
        kouho[idy][idx]='.'
for idy in range(0,H,1):
    for idx in range(0,W,1):
        #(x,y)について隣接9マスが入力で全部'#'か場外なら塗る
        for idz in range(0,9,1):
            if not nurip(idx+idz%3-1,idy+idz//3-1):
                break
        else:
            kouho[idy][idx]='#'

#kouhoで塗る
#更地
myon=list(range(0,H,1))
for idy in range(0,H,1):
    myon[idy]=list(range(0,W,1))
    for idx in range(0,W,1):
        myon[idy][idx]='.'
        
for idy in range(0,H,1):
    for idx in range(0,W,1):
        if kouho[idy][idx]=='#':
            for idz in range(0,9,1):
                nurix=idx+idz%3-1
                nuriy=idy+idz//3-1
                if nurix >=0 and nurix < W and nuriy >=0 and nuriy <H:
                    myon[nuriy][nurix]='#'
#print('kouho:')
#printba(kouho)
#print('myon:')
#printba(myon)
#完全再現P
ans='possible'
for idy in range(0,H,1):
    for idx in range(0,W,1):
        if myon[idy][idx]!=S[idy][idx]:
            ans='im'+ans
            break
    if ans != 'possible':
        break

print(ans)
if ans == 'possible':
    #print myon
    printba(kouho)
