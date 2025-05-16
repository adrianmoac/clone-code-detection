import math

def my_round(x, d=0):
    p = 10 ** d
    return float(math.floor((x * p) + math.copysign(0.5, x)))/p

# 整数の入力
deg, dis = map(int, input().split())

if(deg < 112.5):
    dir = 'N'
elif(deg < 337.5):
    dir = 'NNE'
elif(deg < 562.5):
    dir = 'NE'
elif(deg < 787.5):
    dir = 'ENE'
elif(deg < 1012.5):
    dir = 'E'
elif(deg < 1237.5):
    dir = 'ESE'
elif(deg < 1462.5):
    dir = 'SE'
elif(deg < 1687.5):
    dir = 'SSE'
elif(deg < 1912.5):
    dir = 'S'
elif(deg < 2137.5):
    dir = 'SSW'
elif(deg < 2362.5):
    dir = 'SW'
elif(deg < 2587.5):
    dir = 'WSW'
elif(deg < 2812.5):
    dir = 'W'
elif(deg < 3037.5):
    dir = 'WNW'
elif(deg < 3262.5):
    dir = 'NW'
elif(deg < 3487.5):
    dir = 'NNW'
else:
    dir = 'N'

dis = my_round(dis / 60, 1)

if(dis <= 0.2):
    w = 0
    dir = 'C'
elif(dis <= 1.5):
    w = 1
elif(dis <= 3.3):
    w = 2
elif(dis <= 5.4):
    w = 3
elif(dis <= 7.9):
    w = 4
elif(dis <= 10.7):
    w = 5
elif(dis <= 13.8):
    w = 6
elif(dis <= 17.1):
    w = 7
elif(dis <= 20.7):
    w = 8
elif(dis <= 24.4):
    w = 9
elif(dis <= 28.4):
    w = 10
elif(dis <= 32.6):
    w = 11
else:
    w = 12

print(dir+' '+str(w))