id0,id1=input().split()
id2=id3(id0)
id4=id3(id1)
id5=[]
for id6 in id7(0,id4):
    id8, id9=input().split()
    id5.id10((id3(id8),id3(id9)))
id11,id12=id13(*id5)

id14=id11+id12
id15=id12+id11


def id16(id17):
    global id14
    global id15
    global id18
    global id19
    for id20 in id7(0,id21(id14)):
        if id14[id20]==id17:
            if not id15[id20] in id18[0:id19]:
                yield id15[id20]

def id22(): #returns whether "move" succeeded or not
    global id18
    global id23
    global id19
    global id24
    global id2
    global id25
    try:
        _=id26(id23[id19])
        id18[id19+1]=_
        id19+=1
        #print("success move to {}".format(nodes[step]))
        #print("map: {}".format(nodes[0:step+1]))
        #print("I am at {}th node".format(step+1))
        if id19==id2-1:
            id24+=1
            #print('REACHED GOAL!!!')
        id23[id19]=id16(id18[id19])
    except id27:
        id19-=1
        #print("failed to move")
        if not id19==-1:
            pass#print("map: {}".format(nodes[0:step+1]))
            #print("I am at {}th node".format(step+1))
        if id19==-1:
            #print("I fell from the first node")
            id25=True

id18=[0]*id2
id23=[0]*id2
id24=0
id19=0
id18[id19]=1
id23[id19]=id16(id18[0])
id25=False

while not id25:
    id22()


print(id24)