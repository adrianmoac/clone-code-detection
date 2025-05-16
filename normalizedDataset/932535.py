import id0
import id1
from id2 import id3
def id4(id5,id6):
    while id6>0:
        id5,id6=id6,id5%id6
    return id7(id5)
def id8(id5,id6):
    return id7(id5*id6/id4(id5,id6))

id9=id0.id10.id11()
id12=id7(id9[0])
id13=[1,1]
id14=2
id15=[id13[0],id13[1]]
for id16 in id9[1:]:
    id16=id16.id17().split(" ")
    for id18 in id19(id20(id16)):
        id16[id18]=id7(id16[id18])
    #print ("line=",line)
    #print ("ret=",ret)
    #print ("before_sum=",before_sum)
    #print ("before_ret=",before_ret)
    id5,id6=id7(id16[0]),id7(id16[1])
    #before_ret=[ret[0],ret[1]]
    if (id13[0]<=id5) and (id13[1]<=id6):
        id13[0]=id5
        id13[1]=id6
    else:
        id21=id3(id13[0])/id3(id5)
        id22=id3(id13[1])/id3(id6)
        if (id21>id22):
            id13[0]=id1.id23(id21)*id16[0]
            id13[1]=id1.id23(id21)*id16[1]
        elif (id21<=id22):
            id13[0]=id1.id23(id22)*id16[0]
            id13[1]=id1.id23(id22)*id16[1]
    #g=gcd(ret[0],ret[1])
    #print (ret[0],ret[1],g)
    #ret[0]=int(ret[0]/g)
    #ret[1]=int(ret[1]/g)
    """
    if (before_sum>(ret[0]+ret[1])):
        #print ("before_sum=",before_sum,ret)
        check_ret=[ret[0],ret[1]]
        i=2
        print ("check:",check_ret,before_ret)
        while((check_ret[0]+check_ret[1])<before_sum):
            check_ret[0]=ret[0]*i
            check_ret[1]=ret[1]*i
            i+=1
        i=2
        while(check_ret[0]<before_ret[0] or check_ret[1]<before_ret[1]):
            check_ret[0]=ret[0]*i
            check_ret[1]=ret[1]*i
            i+=1
        ret[0]=check_ret[0]
        ret[1]=check_ret[1]
        before_sum=ret[0]+ret[1]
    else:
        before_sum=ret[0]+ret[1]
    """


#print (ret)
print (id13[0]+id13[1])