def id0():
    id1=input()
    id2=id1.id3(" ")
    id4=id5(id1[0:id2])
    id6=id5(id1[id2+1:])
    id7="   "
    id8=0

    if id4<112.5:
        id7="N"
    elif id4<337.5:
        id7="NNE"
    elif id4<562.5:
        id7="NE"
    elif id4<787.5:
        id7="ENE"
    elif id4<1012.5:
        id7="E"
    elif id4<1237.5:
        id7="ESE"
    elif id4<1462.5:
        id7="SE"
    elif id4<1687.5:
        id7="SSE"
    elif id4<1912.5:
        id7="S"
    elif id4<2137.5:
        id7="SSW"
    elif id4<2362.5:
        id7="SW"
    elif id4<2587.5:
        id7="WSW"
    elif id4<2812.5:
        id7="W"
    elif id4<3037.5:
        id7="WNW"
    elif id4<3262.5:
        id7="NW"
    elif id4<3487.5:
        id7="NNW"
    else:
        id7="N"

    if id6<15:##0.25*60
        id8=0
        id7="C"
    elif id6<93:##1.55*60
        id8=1
    elif id6<201:##3.35*60
        id8=2
    elif id6<327:##5.45*60
        id8=3
    elif id6<477:##7.95*60
        id8=4
    elif id6<645:##10.75*60
        id8=5
    elif id6<831:##13.85*60
        id8=6
    elif id6<1029:##17.15*60
        id8=7
    elif id6<1245:##20.75*60
        id8=8
    elif id6<1467:##24.45*60
        id8=9
    elif id6<1707:##28.45*60
        id8=10
    elif id6<1959:##32.65*60
        id8=11
    else:
        id8=12

    print(id7+" {0:d}".id9(id8))

id0()