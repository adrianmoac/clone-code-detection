id0,id1,id2=id3(map(id4,input().split()))
id5=id3(map(id4,input().split()))

def id6(id7, id8):
    """
    Calculate the number of combination (nCr=nPr/r!).
    The parameters need to meet the condition of n>=r>=0.
    It returns 1 if r==0, which means there is one pattern
    to choice 0 items out of the number of n.
    """

    # 10C7=10C3
    id8=id9(id8, id7-id8)

    # Calculate the numerator.
    id10=1
    for id11 in id12(id7, id7-id8,-1):
        id10*=id11

    # Calculate the denominator. Should use math.factorial?
    id13=1
    for id11 in id12(id8, 1,-1):
        id13*=id11

    return id10//id13

id5.id14(id15=True)
id16={}
for id11 in id5:
	id16[id11]=0
for id11 in id5:
	id16[id11]+=1

id17=0

id18=0

id19=[]

for id11 in id12(id1,id2+1):
	if id18<id20(id5[:id11])/id11:
		id18=id20(id5[:id11])/id11
		id19=[id11]
	elif id18==id20(id5[:id11])/id11:
		id19.id21(id11)

for id11 in id19:
	id22=1
	id23={}
	for id24 in id5[:id11]:
		id23[id24]=0
	for id24 in id5[:id11]:
		id23[id24]+=1

	for id24 in id23.id25():
		id22*=id6(id16[id24],id23[id24])
	id17+=id22

print(id18)
print(id17)







