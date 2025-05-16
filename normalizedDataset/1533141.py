id0, id1=map(id2, input().split())
id0=id0/10
id1=id1/60

if 11.25<=id0<33.75:
    id3="NNE"
elif 33.75<=id0<56.25:
    id3="NE"
elif 56.25<=id0<78.75:
    id3="ENE"
elif 78.75<=id0<101.25:
    id3="E"
elif 101.25<=id0<123.75:
    id3="ESE"
elif 123.75<=id0<146.25:
    id3="SE"
elif 146.25<=id0<168.75:
    id3="SSE"
elif 168.75<=id0<191.25:
    id3="S"
elif 191.25<=id0<213.75:
    id3="SSW"
elif 213.75<=id0<236.25:
    id3="SW"
elif 236.25<=id0<258.75:
    id3="WSW"
elif 258.75<=id0<281.25:
    id3="W"
elif 281.25<=id0<303.75:
    id3="WNW"
elif 303.75<=id0<326.25:
    id3="NW"
elif 326.25<=id0<348.75:
    id3="NNW"
else:
    id3="N"

if id1<0.25:
    id3="C"
    id4=0
elif 0.25<=id1<1.55:
    id4=1
elif 1.55<=id1<3.35:
    id4=2
elif 3.35<=id1<5.45:
    id4=3
elif 5.45<=id1<7.95:
    id4=4
elif 7.95<=id1<10.75:
    id4=5
elif 10.75<=id1<13.85:
    id4=6
elif 13.85<=id1<17.15:
    id4=7
elif 17.15<=id1<20.75:
    id4=8
elif 20.75<=id1<24.45:
    id4=9
elif 24.45<=id1<28.45:
    id4=10
elif 28.45<=id1<32.65:
    id4=11
else:
    id4=12


print(id3,id4)