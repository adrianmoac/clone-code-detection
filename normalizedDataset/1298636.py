import id0
id1, id2=[id3(id4) for id4 in input().split()]
id5=id3(id1/3)
id6=id3 (id2/3)
id7=id0.id8
#|||Split
if(id1%3==0 or id2%3==0):
    id7=0
id9=id5*id2
id10=(id5+1)*id2
if(id7>id10-id9):
    id7=id10-id9
id9=id6*id1
id10=(id6+1)*id1
if(id7>id10-id9):
    id7=id10-id9
# print("|||:", a2-a1)
 
# T Split
id9=id5*id2
id10=(id1-id5)*id3(id2/2)
if(id2%2==1):
    id10+=(id1-id5)
id11=(id1-id5)*id3(id2/2)
id12=id9
if(id9>id11):
    id12=id11
id13=id10
if(id9>id10):
    id13=id9
if(id7>(id13-id12)):
    id7=id13-id12
 
# print("T1: ", amax-amin)
 
id14=id5+1
id9=(id14)*id2      # 10
id10=(id1-id14)*id3(id2/2)  # 6
if(id2%2==1):
    id10+=(id1-id14) # 9
id11=(id1-id14)*id3(id2/2)
id12=id9
if(id9>id11):
    id12=id11
id13=id10
if(id9>id10):
    id13=id9
if(id7>(id13-id12)):
    id7=id13-id12
 
# print("T2: ", amax-amin, amax, amin)
 
id1, id2=id2, id1
id5=id3(id1/3)
id6=id3 (id2/3)
id9=id5*id2
id10=(id1-id5)*id3(id2/2)
if(id2%2==1):
    id10+=(id1-id5)
id11=(id1-id5)*id3(id2/2)
id12=id9
if(id9>id11):
    id12=id11
id13=id10
if(id9>id10):
    id13=id9
if(id7>(id13-id12)):
    id7=id13-id12
 
# print("T3: ", amax-amin)
 
id14=id5+1
id9=(id14)*id2
id10=(id1-id14)*id3(id2/2)
if(id2%2==1):
    id10+=(id1-id14)
id11=(id1-id14)*id3(id2/2)
id12=id9
if(id9>id11):
    id12=id11
id13=id10
if(id9>id10):
    id13=id9
if(id7>(id13-id12)):
    id7=id13-id12
 
# print("T4: ", amax-amin)
 
print(id3(id7))