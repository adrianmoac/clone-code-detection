import math
Deg,Dis = map(int,(input().split()))

Deg = Deg/10
round=lambda x:(x*2+1)//2
Dis = round(Dis/6)/10

Dir,W = "",0

if Deg < 11.25:
    Dir = "N"
elif Deg <= 33.75:
    Dir = "NNE"
elif Deg <= 56.25:
    Dir = "NE"
elif Deg <= 78.75:
    Dir = "ENE"
elif Deg <= 101.25:
    Dir = "E"
elif Deg <= 123.75:
    Dir = "ESE"
elif Deg <= 146.25:
    Dir = "SE"
elif Deg <= 168.75:
    Dir = "SSE"
elif Deg <= 191.25:
    Dir = "S"
elif Deg <= 213.75 :
    Dir = "SSW"
elif Deg <= 236.25 :
    Dir = "SW"
elif Deg <= 258.75 :
    Dir = "WSW"
elif Deg <= 281.25 :
    Dir = "W"
elif Deg <= 303.75 :
    Dir = "WNW"
elif Deg <= 326.25 :
    Dir = "NW"
elif Deg <= 348.75 :
    Dir = "NNW"
elif Deg > 348.75 :
    Dir = "N"

if Dis <= 0.2:
    W = 0
elif Dis <= 1.5:
    W = 1
elif Dis <= 3.3:
    W = 2
elif Dis <= 5.4:
    W = 3
elif Dis <= 7.9:
    W = 4
elif Dis <= 10.7:
    W = 5
elif Dis <= 13.8:
    W = 6
elif Dis <= 17.1:
    W = 7
elif Dis <= 20.7:
    W = 8
elif Dis <= 24.4:
    W = 9
elif Dis <= 28.4 :
    W = 10
elif Dis <= 32.6 :
    W = 11
elif Dis >= 32.7:
    W = 12

if(W==0):
    print("C " + str(W))
else:
    print(Dir + " " + str(W))
