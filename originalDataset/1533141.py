Deg, Dis = map(int, input().split())
Deg = Deg / 10
Dis = Dis / 60

if 11.25 <= Deg < 33.75:
    Dir = "NNE"
elif 33.75 <= Deg < 56.25:
    Dir = "NE"
elif 56.25 <= Deg < 78.75:
    Dir = "ENE"
elif 78.75 <= Deg < 101.25:
    Dir = "E"
elif 101.25 <= Deg < 123.75:
    Dir = "ESE"
elif 123.75 <= Deg < 146.25:
    Dir = "SE"
elif 146.25 <= Deg < 168.75:
    Dir = "SSE"
elif 168.75 <= Deg < 191.25:
    Dir = "S"
elif 191.25 <= Deg < 213.75:
    Dir = "SSW"
elif 213.75 <= Deg < 236.25:
    Dir = "SW"
elif 236.25 <= Deg < 258.75:
    Dir = "WSW"
elif 258.75 <= Deg < 281.25:
    Dir = "W"
elif 281.25 <= Deg < 303.75:
    Dir = "WNW"
elif 303.75 <= Deg < 326.25:
    Dir = "NW"
elif 326.25 <= Deg < 348.75:
    Dir = "NNW"
else:
    Dir = "N"

if Dis < 0.25:
    Dir = "C"
    W = 0
elif 0.25 <= Dis < 1.55:
    W = 1
elif 1.55 <= Dis < 3.35:
    W = 2
elif 3.35 <= Dis < 5.45:
    W = 3
elif 5.45 <= Dis < 7.95:
    W = 4
elif 7.95 <= Dis < 10.75:
    W = 5
elif 10.75 <= Dis < 13.85:
    W = 6
elif 13.85 <= Dis < 17.15:
    W = 7
elif 17.15 <= Dis < 20.75:
    W = 8
elif 20.75 <= Dis < 24.45:
    W = 9
elif 24.45 <= Dis < 28.45:
    W = 10
elif 28.45 <= Dis < 32.65:
    W = 11
else:
    W = 12


print(Dir,W)
