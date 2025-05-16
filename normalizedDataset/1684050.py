id0, id1=map(id2, input().split())
id3={}
for _ in id4(id0):
    id3[_]=input()
    
def id5(id6, id7, id8):
    id9=id10(id6)
    id9[id8]=id11(id7.id12("#"))
    id6="".id13(id9)
    return id6

for id14 in id4(id0):
    for id8 in id4(id1):
        id15=id3[id14][id8]
        if id15==".":
            if id0==1 and id1==1:
                id3[id14]="0"
            elif id0==1 and id8==0:
                id7=id3[id14][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id0==1 and id8==id1-1:
                id7=id3[id14][id8-1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id0==1:
                id7=id3[id14][id8-1]+id3[id14][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id1==1 and id14==0:
                id7=id3[id14+1][id8]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id1==1 and id14==id1-1:
                id7=id3[id14-1][id8]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id1==1:
                id7=id3[id14-1][id8]+id3[id14+1][id8]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id14==0 and id8==0:
                id7=id3[id14][id8+1]+id3[id14+1][id8]+id3[id14+1][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id14==0 and id8==id1-1:
                id7=id3[id14][id8-1]+id3[id14+1][id8-1]+id3[id14+1][id8]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id14==0:
                id7=id3[id14][id8-1]+id3[id14][id8+1]+id3[id14+1][id8-1]+id3[id14+1][id8]+id3[id14+1][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id14==id0-1 and id8==0:
                id7=id3[id14][id8+1]+id3[id14-1][id8]+id3[id14-1][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id14==id0-1 and id8==id1-1:
                id7=id3[id14][id8-1]+id3[id14-1][id8-1]+id3[id14-1][id8]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id14==id0-1:
                id7=id3[id14][id8-1]+id3[id14][id8+1]+id3[id14-1][id8-1]+id3[id14-1][id8]+id3[id14-1][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id8==0:
                id7=id3[id14-1][id8]+id3[id14-1][id8+1]+id3[id14][id8+1]+id3[id14+1][id8]+id3[id14+1][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
            elif id8==id1-1:
                id7=id3[id14-1][id8-1]+id3[id14-1][id8]+id3[id14][id8-1]+id3[id14+1][id8-1]+id3[id14+1][id8]
                id3[id14]=id5(id3[id14], id7, id8)
            else:
                id7=id3[id14-1][id8-1]+id3[id14-1][id8]+id3[id14-1][id8+1]+id3[id14][id8-1]+id3[id14][id8+1]+id3[id14+1][id8-1]+id3[id14+1][id8]+id3[id14+1][id8+1]
                id3[id14]=id5(id3[id14], id7, id8)
                
for id16 in id4(id0):
    print(id3[id16])