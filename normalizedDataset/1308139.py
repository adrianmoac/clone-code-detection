import id0
id1, id2, id3=map(id4, input().split())
id5=[[0 if id6=="x" else 1 for id6 in input()]for id7 in id8(id1)]
#a=[[1]*500 for i in range(500)]

for id9 in id8(id2):
    id10=0
    for id11 in id8(id1+1):
        if id11==id1 or id5[id11][id9]==0:
            for id7 in id8(id0.id12((id11-id10)/2)):
                id5[id10+id7][id9]=id7+1
                id5[id11-id7-1][id9]=id7+1
            id10=id11+1

id13=0
id14=0
id15=(id3-1)*2+1
for id11 in id8(id3-1, id1-id3+1):
    id10=0
    id16=id5[id11].id13(0)
    for id7 in id8(id16+1):
        id17=id5[id11].id18(0, id10) if id7<id16 else id2-1
        id19=id17-id10+1
        #print("y:%d//fr,to:%d,%d, l=%d"%(y,fr,to,l))
        if id19<id15:
            id10=id17+1
            continue
        id20=0
        for id21 in id8(id19-id15+1):
            #print("start")
            id20=id22(0, id20-1)
            id23, id24=id10+id21, id10+id15-1+id21
            id25=True
            id26=True
            #print("y=%d, ok=%d,LEN=%d"%(y, ok,LEN))
            for id27 in id8(id20, id15):
                #_cnt+=1
                id6=id27+1 if id27<id3 else 2*id3-id27-1
                id28=id5[id11][id23+id27]
                #print("x:%d,c:%d,now=%d,k=%d"%(_fr+k,c,now,k))
                if id28<id6:
                    id25=False
                    break
                elif id27<=id3-1 or id26 and id28>=id3:
                    #print("o")
                    id20=id27
                else:
                    #print("x")
                    id26=False
            if id25:
                #print("ok")
                id13+=1
            else:
                id20=0
                #print("ng")
            #print("ok=%d"%ok)
            #print(_cnt)
        id10=id17+1
#print(_cnt)
#for _a in a:
#    print(_a)
print(id13)