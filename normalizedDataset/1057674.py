id0, id1, id2, id3=id4(map(id5, input().split()))

id6=[]
id7, id8=id0, id1
for id9 in id10(id3-id1-1):
    id6.id11("U")
    id8+=1

for id9 in id10(id2-id0-1):
    id6.id11("R")
    id7+=1

for id9 in id10(id3-id8):
    id6.id11("U")
    id8+=1

for id9 in id10(id2-id7):
    id6.id11("R")
    id7+=1

id6.id11("R")
id7+=1

for id9 in id10(id3-id1+1):
    id6.id11("D")
    id8-=1

for id9 in id10(id7-id0):
    id6.id11("L")
    id7-=1

id6.id11("U")
id8+=1
id6.id11("L")
id7-=1

for id9 in id10(id3+1-id8):
    id6.id11("U")
    id8+=1

for id9 in id10(id2-id7):
    id6.id11("R")
    id7+=1

id6.id11("D")
id8-=1

id6.id11("D")
id8-=1

for id9 in id10(id3-id1-1):
    id6.id11("D")
    id8-=1

for id9 in id10(id2-id0-1):
    id6.id11("L")
    id7-=1

for id9 in id10(id8-id1):
    id6.id11("D")
    id8-=1

for id9 in id10(id7-id0):
    id6.id11("L")
    id7-=1

# print(vec)
# print(x, y)
for id12 in id6:
    print(id12, id13="")