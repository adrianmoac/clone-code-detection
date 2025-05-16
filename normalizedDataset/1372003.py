id0, id1, id2=map(id3, input().split("/"))
if id0%400==0 or (id0%4==0 and id0%100!=0):
    while id0%(id1*id2)!=0:
        if id1==1 or id1==3 or id1==5 or id1==7 or id1==8 or id1==10:
            if id2<31:
                id2+=1
            else:
                id2=1
                id1+=1
        elif id1==4 or id1==6 or id1==9 or id1==11:
            if id2<30:
                id2+=1
            else:
                id2=1
                id1+=1
        elif id1==2:
            if id2<29:
                id2+=1
            else:
                id2=1
                id1+=1
        elif id1==12:
            if id2<31:
                id2+=1
            else:
                id2=1
                id1=1
                id0+=1
if id0%4!=0 or (id0%100==0 and id0%400!=0):
    while id0%(id1*id2)!=0:
        if id1==1 or id1==3 or id1==5 or id1==7 or id1==8 or id1==10:
            if id2<31:
                id2+=1
            else:
                id2=1
                id1+=1
        elif id1==4 or id1==6 or id1==9 or id1==11:
            if id2<30:
                id2+=1
            else:
                id2=1
                id1+=1
        elif id1==2:
            if id2<28:
                id2+=1
            else:
                id2=1
                id1+=1
        elif id1==12:
            if id2<31:
                id2+=1
            else:
                id2=1
                id1=1
                id0+=1
id0="{:2d}".id4(id0)
id1="{:02d}".id4(id1)
id2="{:02d}".id4(id2)
id5="{}/{}/{}".id4(id0, id1, id2)
print(id5)