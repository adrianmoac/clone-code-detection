def id0():
    id1, id2=map(id3, input().split())

    if 112.5<=id1<337.5:
        id4="NNE"
    elif 337.5<=id1<562.5:
        id4="NE"
    elif 562.5<=id1<787.5:
        id4="ENE"
    elif 787.5<=id1<1012.5:
        id4="E"
    elif 1012.5<=id1<1237.5:
        id4="ESE"
    elif 1237.5<=id1<1462.5:
        id4="SE"
    elif 1462.5<=id1<1687.5:
        id4="SSE"
    elif 1687.5<=id1<1912.5:
        id4="S"
    elif 1912.5<=id1<2137.5:
        id4="SSW"
    elif 2137.5<=id1<2362.5:
        id4="SW"
    elif 2362.5<=id1<2587.5:
        id4="WSW"
    elif 2587.5<=id1<2812.5:
        id4="W"
    elif 2812.5<=id1<3037.5:
        id4="WNW"
    elif 3037.5<=id1<3262.5:
        id4="NW"
    elif 3262.5<=id1<3487.5:
        id4="NNW"
    else:
        id4="N"

    id5=(id2/60*20+1)//2/10
    if 0<=id5<=0.2:
        id6=0
        id4="C"
    elif 0.3<=id5<=1.5:
        id6=1
    elif 1.6<=id5<=3.3:
        id6=2
    elif 3.4<=id5<=5.4:
        id6=3
    elif 5.5<=id5<=7.9:
        id6=4
    elif 8.0<=id5<=10.7:
        id6=5
    elif 10.8<=id5<=13.8:
        id6=6
    elif 13.9<=id5<=17.1:
        id6=7
    elif 17.2<=id5<=20.7:
        id6=8
    elif 20.8<=id5<=24.4:
        id6=9
    elif 24.5<=id5<=28.4:
        id6=10
    elif 28.5<=id5<=32.6:
        id6=11
    else:
        id6=12

    print("{} {}".id7(id4, id6))

id0()