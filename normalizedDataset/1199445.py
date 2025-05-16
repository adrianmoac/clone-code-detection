def id0(id1,id2=1):
    id3=10**id2
    return (id1*id3*2+1)//2/id3

def id4(id5):

    id6=id5/10.0
    if 11.25<=id6<33.75:
        id7="NNE"
    elif 33.75<=id6<56.25:
        id7="NE"
    elif 56.25<=id6<78.75:
        id7="ENE"
    elif 78.75<=id6<101.25:
        id7="E"
    elif 101.25<=id6<123.75:
        id7="ESE"
    elif 123.75<=id6<146.25:
        id7="SE"
    elif 146.25<=id6<168.75:
        id7="SSE"
    elif 168.75<=id6<191.25:
        id7="S"
    elif 191.25<=id6<213.75:
        id7="SSW"
    elif 213.75<=id6<236.25:
        id7="SW"
    elif 236.25<=id6<258.75:
        id7="WSW"
    elif 258.75<=id6<281.25:
        id7="W"
    elif 281.25<=id6<303.75:
        id7="WNW"
    elif 303.75<=id6<326.25:
        id7="NW"
    elif 326.25<=id6<348.75:
        id7="NNW"
    else:
        id7="N"

    return id7

def id8(id9):
    id6=id0(id9/60.0)

    if id6<=0.2:
        id7=0
    elif id6<=1.5:
        id7=1
    elif id6<=3.3:
        id7=2
    elif id6<=5.4:
        id7=3
    elif id6<=7.9:
        id7=4
    elif id6<=10.7:
        id7=5
    elif id6<=13.8:
        id7=6
    elif id6<=17.1:
        id7=7
    elif id6<=20.7:
        id7=8
    elif id6<=24.4:
        id7=9
    elif id6<=28.4:
        id7=10
    elif id6<=32.6:
        id7=11
    else:
        id7=12

    return id7


id10=input().split(" ")
id5=id11(id10[0])
id9=id11(id10[1])

id12=id4(id5)
id13=id8(id9)

if id13==0:
    print("C 0")
else:
    print("{0} {1}".id14(id12, id13))