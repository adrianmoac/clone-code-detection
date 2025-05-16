def flip(c):
    if c=='S':
        return 'W'
    else:
        return 'S'

def judge():
    found=False
    ret = -1
    for i in xrange(N):
        #print r
        if r[i]=='S':
            if s[i]=='o':
                if i==0:
                    r[i-1]=r[i+1]
                elif i==N-1:
                    if r[0]==r[i-1]:
                        found=True
                elif i==N-2:
                    if r[i+1]!=r[i-1]:
                        break;                    
                else:
                    r[i+1]=r[i-1]
            else:
                if i==0:
                    r[i-1]=flip(r[i+1])
                elif i==N-2:
                    if r[i+1]!=flip(r[i-1]):
                        break;                    
                elif i==N-1:
                    if r[0]==flip(r[i-1]):
                        found=True
                else:
                    r[i+1]=flip(r[i-1])
        else: # W
            if s[i]=='x':
                if i==0:
                    r[i-1]=r[i+1]
                elif i==N-1:
                    if r[0]==r[i-1]:
                        found=True
                elif i==N-2:
                    if r[i+1]!=r[i-1]:
                        break;                    
                else:
                    r[i+1]=r[i-1]
            else:
                if i==0:
                    r[i-1]=flip(r[i+1])
                elif i==N-1:
                    if r[0]==flip(r[i-1]):
                        found=True
                elif i==N-2:
                    if r[i+1]!=flip(r[i-1]):
                        break;                    
                else:
                    r[i+1]=flip(r[i-1])
                
        if found:
            ret = ''.join(r)

    return ret
    
N=input()
s=list(raw_input())


ptn=[['S','S'],['S','W'],['W','S'],['W','W']]

ret = None
for p in ptn:
    r = [None]*N
    r[0]=p[0]
    r[1]=p[1]
    ret = judge()
    if ret != -1:
        break
print ret

