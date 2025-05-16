
x = list(map(int, input().split()))
k = [list(map(str, input())) for i in range(x[0])]

def check(i,j,k):
    if k[i][j]=='#':
        return '#'
    count=0
    if len(k)==1:
        if len(k[0])==1:
            if k[0][0]=='#':
                return '#'
            return 0
        if len(k[0])!=1:
            if j==0:
                if k[0][1]=='#':
                    count+=1
                return count
            if j==len(k[0])-1:
                if k[0][len(k[0])-2]=='#':
                    count+=1
                return count
            for jj in range(-1,2):
                if jj==0:
                    continue
                if k[0][j+jj]=='#':
                    count+=1
            return count

    if len(k[0])==1:
        if i==0:
            if k[1][0]=='#':
                count+=1
            return count
        if i==len(k)-1:
            if k[len(k)-2][0]=='#':
                count+=1
            return count
        for ii in range(-1,2):
            if ii==0:
                continue
            if k[i+ii][0]=='#':
                count+=1
        return count           


    if i==0 and j==0:
        for ii in range(0,2):
            for jj in range(0,2):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1
        return count
    if i==0 and j==len(k[0])-1:
        for ii in range(0,2):
            for jj in range(-1,1):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1
        return count    

    if i==len(k)-1 and j==0:
        for ii in range(-1,1):
            for jj in range(0,2):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1
        return count 
    if i==len(k)-1 and j==len(k[0])-1:
        for ii in range(-1,1):
            for jj in range(-1,1):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1
        return count
    if i==0:
        for ii in range(0,2):
            for jj in range(-1,2):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1
        return count

    if i==len(k)-1:
        for ii in range(-1,1):
            for jj in range(-1,2):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1
        return count

    if j==0:
        for ii in range(-1,2):
            for jj in range(0,2):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1 
        return count

    if j==len(k[0])-1:
        for ii in range(-1,2):
            for jj in range(-1,1):
                if ii==0 and jj==0:
                    continue
                if k[i+ii][j+jj]=='#':
                    count+=1
        return count
       
    for ii in range(-1,2):
        for jj in range(-1,2):
            if ii==0 and jj==0:
                continue
            if k[i+ii][j+jj]=='#':
                count+=1
    return count

res=[]
for ik in range(len(k)):
    for jk in range(len(k[0])):
        res.append(check(ik,jk,k))  

for i in range(x[0]):
    sta=0+x[1]*i
    fin=x[1]+x[1]*i
    while sta<fin:
        print(res[sta],end='')
        sta +=1
    print('')
quit()


