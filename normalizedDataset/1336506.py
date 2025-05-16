
def id0(id1):
    id2=id1/10
    if 11.25<=id2 and id2<33.75:
        return "NNE"
    if 33.75<=id2 and id2<56.25:
        return "NE"
    if 56.25<=id2 and id2<78.75:
        return "ENE"
    if 78.75<=id2 and id2<101.25:
        return "E"
    if 101.25<=id2 and id2<123.75:
        return "ESE"
    if 123.75<=id2 and id2<146.25:
        return "SE"
    if 146.25<=id2 and id2<168.75:
        return "SSE"
    if 168.75<=id2 and id2<191.25:
        return "S"
    if 191.25<=id2 and id2<213.75:
        return "SSW"
    if 213.75<=id2 and id2<236.25:
        return "SW"
    if 236.25<=id2 and id2<258.75:
        return "WSW"
    if 258.75<=id2 and id2<281.25:
        return "W"
    if 281.25<=id2 and id2<303.75:
        return "WNW"
    if 303.75<=id2 and id2<326.25:
        return "NW"
    if 326.25<=id2 and id2<348.75:
        return "NNW"
    return "N"

def id3(id4):
    id5=lambda id2:(id2*2+1)//2

    id6=id5(id4/6)/10

    if id6<=0.2:
        return 0
    if 0.3<=id6<=1.5:
        return 1
    if id6<=3.3:
        return 2
    if id6<=5.4:
        return 3
    if id6<=7.9:
        return 4
    if id6<=10.7:
        return 5
    if id6<=13.8:
        return 6
    if id6<=17.1:
        return 7
    if id6<=20.7:
        return 8
    if id6<=24.4:
        return 9
    if id6<=28.4:
        return 10
    if id6<=32.6:
        return 11
    if 32.7<=id6:
        return 12
    return 0

def id7( id8, id9):
    id10=id3(id9)
    id11=id0(id8)
    if id10==0:
        return "C 0"
    else:
        return id11+" "+(id12)(id10)

if id13=="__main__":
    id14,id15=map(id16,(input().split()))
    print(id7(id14,id15))
