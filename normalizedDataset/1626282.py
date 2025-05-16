def id0(id1, id2=0):
    id3=10**id2
    return (id1*id3*2+1)//2/id3

id4, id5=map(id6, input().split())

if(id4>=112.5 and id4<337.5):
    id7="NNE"
elif(id4>=337.5 and id4<562.5):
    id7="NE"
elif(id4>=562.5 and id4<787.5):
    id7="ENE"
elif(id4>=787.5 and id4<1012.5):
    id7="E"
elif(id4>=1012.5 and id4<1237.5):
    id7="ESE"
elif(id4>=1237.5 and id4<1462.5):
    id7="SE"
elif(id4>=1462.5 and id4<1687.5):
    id7="SSE"
elif(id4>=1678.5 and id4<1912.5):
    id7="S"
elif(id4>=1912.5 and id4<2137.5):
    id7="SSW"
elif(id4>=1912.5 and id4<2137.5):
    id7="SSW"
elif(id4>=2137.5 and id4<2362.5):
    id7="SW"
elif(id4>=2362.5 and id4<2587.5):
    id7="WSW"
elif(id4>=2587.5 and id4<2812.5):
    id7="W"
elif(id4>=2812.5 and id4<3037.5):
    id7="WNW"
elif(id4>=3037.5 and id4<3262.5):
    id7="NW"
elif(id4>=3262.5 and id4<3487.5):
    id7="NNW"
else:
    id7="N"

id8=id0(id5/60, 1)
if(id8<=0.2):
    id7="C"
    id9=0
elif(id8<=1.5):
    id9=1
elif(id8<=3.3):
    id9=2
elif(id8<=5.4):
    id9=3
elif(id8<=7.9):
    id9=4
elif(id8<=10.7):
    id9=5
elif(id8<=13.8):
    id9=6
elif(id8<=17.1):
    id9=7
elif(id8<=20.7):
    id9=8
elif(id8<=24.4):
    id9=9
elif(id8<=28.4):
    id9=10
elif(id8<=32.6):
    id9=11
else:
    id9=12

print("{0} {1}".id10(id7, id9))