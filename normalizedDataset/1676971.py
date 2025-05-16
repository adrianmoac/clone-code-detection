def id0(id1, id2=0):
    id3=10**id2
    return (id1*id3*2+1)//2/id3

def id4(id2, id5):
    if id5==0:
        return "C"

    if id2<1125:
        return "N"
    elif id2<3375:
        return "NNE"
    elif id2<5625:
        return "NE"
    elif id2<7875:
        return "ENE"
    elif id2<10125:
        return "E"
    elif id2<12375:
        return "ESE"
    elif id2<14625:
        return "SE"
    elif id2<16875:
        return "SSE"
    elif id2<19125:
        return "S"
    elif id2<21375:
        return "SSW"
    elif id2<23625:
        return "SW"
    elif id2<25875:
        return "WSW"
    elif id2<28125:
        return "W"
    elif id2<30375:
        return "WNW"
    elif id2<32625:
        return "NW"
    elif id2<34875:
        return "NNW"
    else:
        return "N"


def id6(id2):
    id7=id0(id2/60, 1)
    if id7<=0.2:
        return 0
    elif id7<=1.5:
        return 1
    elif id7<=3.3:
        return 2
    elif id7<=5.4:
        return 3
    elif id7<=7.9:
        return 4
    elif id7<=10.7:
        return 5
    elif id7<=13.8:
        return 6
    elif id7<=17.1:
        return 7
    elif id7<=20.7:
        return 8
    elif id7<=24.4:
        return 9
    elif id7<=28.4:
        return 10
    elif id7<=32.6:
        return 11
    else:
        return 12


id8, id9=map(id10, input().split())
id5=id6(id9)
id8=id4(id8*10, id5)
print("{} {}".id11(id8, id5))