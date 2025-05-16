# coding:utf-8


def id0(id1, id2):
    # wind_direction
    id1/=10
    if 11.25<=id1<33.75:
        id3="NNE"
    elif 33.75<=id1<56.25:
        id3="NE"
    elif 56.25<=id1<78.75:
        id3="ENE"
    elif 78.75<=id1<101.25:
        id3="E"
    elif 101.25<=id1<123.75:
        id3="ESE"
    elif 123.75<=id1<146.25:
        id3="SE"
    elif 146.25<=id1<168.75:
        id3="SSE"
    elif 168.75<=id1<191.25:
        id3="S"
    elif 191.25<=id1<213.75:
        id3="SSW"
    elif 213.75<=id1<236.25:
        id3="SW"
    elif 236.25<=id1<258.75:
        id3="WSW"
    elif 258.75<=id1<281.25:
        id3="W"
    elif 281.25<=id1<303.75:
        id3="WNW"
    elif 303.75<=id1<326.25:
        id3="NW"
    elif 326.25<=id1<348.75:
        id3="NNW"
    else:
        id3="N"

    # wind_power
    id2=(id2/60*10*2+1)//2/10
    if 0.0<=id2<=0.2:
        return ["C", 0]
    elif 0.3<=id2<=1.5:
        id4=1
    elif 1.6<=id2<=3.3:
        id4=2
    elif 3.4<=id2<=5.4:
        id4=3
    elif 5.5<=id2<=7.9:
        id4=4
    elif 8.0<=id2<=10.7:
        id4=5
    elif 10.8<=id2<=13.8:
        id4=6
    elif 13.9<=id2<=17.1:
        id4=7
    elif 17.2<=id2<=20.7:
        id4=8
    elif 20.8<=id2<=24.4:
        id4=9
    elif 24.5<=id2<=28.4:
        id4=10
    elif 28.5<=id2<=32.6:
        id4=11
    elif 32.7<=id2:
        id4=12

    return [id3, id4]

id1, id2=map(id5, input().split())
print("{} {}".id6(*id0(id1, id2)))