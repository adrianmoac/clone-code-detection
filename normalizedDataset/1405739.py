import id0

def id1(id2, id3=0):
    id4=10**id3
    return id5(id0.id6((id2*id4)+id0.id7(0.5, id2)))/id4

# 整数の入力
id8, id9=map(id10, input().split())

if(id8<112.5):
    id11="N"
elif(id8<337.5):
    id11="NNE"
elif(id8<562.5):
    id11="NE"
elif(id8<787.5):
    id11="ENE"
elif(id8<1012.5):
    id11="E"
elif(id8<1237.5):
    id11="ESE"
elif(id8<1462.5):
    id11="SE"
elif(id8<1687.5):
    id11="SSE"
elif(id8<1912.5):
    id11="S"
elif(id8<2137.5):
    id11="SSW"
elif(id8<2362.5):
    id11="SW"
elif(id8<2587.5):
    id11="WSW"
elif(id8<2812.5):
    id11="W"
elif(id8<3037.5):
    id11="WNW"
elif(id8<3262.5):
    id11="NW"
elif(id8<3487.5):
    id11="NNW"
else:
    id11="N"

id9=id1(id9/60, 1)

if(id9<=0.2):
    id12=0
    id11="C"
elif(id9<=1.5):
    id12=1
elif(id9<=3.3):
    id12=2
elif(id9<=5.4):
    id12=3
elif(id9<=7.9):
    id12=4
elif(id9<=10.7):
    id12=5
elif(id9<=13.8):
    id12=6
elif(id9<=17.1):
    id12=7
elif(id9<=20.7):
    id12=8
elif(id9<=24.4):
    id12=9
elif(id9<=28.4):
    id12=10
elif(id9<=32.6):
    id12=11
else:
    id12=12

print(id11+" "+id13(id12))