id0=id1(input())
id2=input()

id2=id2.split()
for id3 in id4(id5(id2)):
    id2[id3]=id1(id2[id3])

id6=0
id7=0

id8=0
id9=0

for id10 in id4(id5(id2)):
    id7+=id2[id10]
    id6+=id2[id10]
    
    if id10==0:
        if id7==0:   
            id6=-1
            id9=1

            id7=1
            id8=1
            
        elif id7<0:
            id8=id11(id7)+1
            id7=1

        elif id7>0:
            id9=id11(id6)+1
            id6=-1

    elif id10%2==1:
        if id6==0:
            id9+=1
            id6=1
        elif id6<0:
            id9+=id11(id6)+1
            id6=1

        if id7==0:
            id8+=1
            id7=-1
        elif id7>0:
            id8+=id11(id7)+1
            id7=-1

    elif id10%2==0:
        if id6==0:
            id9+=1
            id6=-1
        elif id6>0:
            id9+=id11(id6)+1
            id6=-1

        if id7==0:
            id8+=1
            id7=1
        elif id7<0:
            id8+=id11(id7)+1
            id7=1
    """print("totn", totn)
    print("countn", countn)
    print("totp", totp)
    print("countp", countp) """   
id12=id13(id9, id8)
print(id12)