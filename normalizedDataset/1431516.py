# E

# keta
id0=10**9

print("? "+id1(id0))
id2=input()
# res=sunuke(query)

if id2=="Y":
    # N=10**p
    id0*=2
    # str(query)>str(N)
    for id3 in id4(10):
        id0=id0//10
        if id0==0:
            break
        print("? "+id1(id0))
        id2=input()
        # res=sunuke(query)
        
        if id2=="N":
            break
    if id0>0:
        print("!"+id1(id0*5))
    else:
        print("!1")
            
else:
    for id3 in id4(9):
        id0=id0//10
        
        print("? "+id1(id0))
        id2=input()
        # res=sunuke(query)
        
        if id2=="Y":
            break
    # binary search
    # always query>N
    # query<N<query*10
    # binary search
    # 'N' means query<N
    id5=id0
    id6=id0*10-1
    id7=0
    
    while id7<100:
        id0=(id5+id6)//2
        if id5+1>=id6:
            print("!"+id1(id6))
            break
        
        print("? "+id1(id0*10))
        id2=input()
        # res=sunuke(query)
        id7+=1
        if id2=="N":
            id5=id0
        else:
            id6=id0