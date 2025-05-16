#!/usr/local/bin
degStr,dis = raw_input().split()
direction = "N"
deg = float(degStr)
if deg >= 112.5 and deg < 337.5:
  direction = "NNE"      
elif deg >= 337.5 and deg < 562.5:
  direction = "NE"
elif deg >= 562.5 and deg < 787.5:
  direction = "ENE"
elif deg >= 787.5 and deg < 1012.5:
  direction = "E"
elif deg >= 1012.5 and deg < 1237.5:
  direction = "ESE"
elif deg >= 1237.5 and deg < 1462.5:
  direction = "SE"
elif deg >= 1462.5 and deg < 1687.5:
  direction = "SSE"
elif deg >= 1687.5 and deg < 1912.5:
  direction = "S"
elif deg >= 1912.5 and deg < 2137.5:
  direction = "SSW"
elif deg >= 2137.5 and deg < 2362.5:
  direction = "SW"
elif deg >= 2362.5 and deg < 2587.5:
  direction = "WSW"
elif deg >= 2587.5 and deg < 2812.5:
  direction = "W"
elif deg >= 2812.5 and deg < 3037.5:
  direction = "WNW"
elif deg >= 3037.5 and deg < 3262.5:
  direction = "NW"
elif deg >= 3262.5 and deg < 3487.5:
  direction = "NNW"

tmp = int(dis)/60.0
tmpStr = str(tmp)
tmpStr2 = tmpStr.split('.')

winms = round(tmp,1)

if len(tmpStr2) == 2:
  tmpStr3 = tmpStr2[1]
  if len(tmpStr3) >= 2:
    if tmpStr3[1] == "5":
      winms = round(tmp,1) + 0.1

W = 0

if winms >= 0.0 and winms <= 0.2:
  W = 0
  direction = "C"
elif winms >= 0.3 and winms <= 1.5:
  W = 1
elif winms >= 1.6 and winms <= 3.3:
  W = 2
elif winms >= 3.4 and winms <= 5.4:
  W = 3
elif winms >= 5.5 and winms <= 7.9:
  W = 4
elif winms >= 8.0 and winms <= 10.7:
  W = 5
elif winms >= 10.8 and winms <= 13.8:
  W = 6
elif winms >= 13.9 and winms <= 17.1:
  W = 7
elif winms >= 17.2 and winms <= 20.7:
  W = 8
elif winms >= 20.8 and winms <= 24.4:
  W = 9
elif winms >= 24.5 and winms <= 28.4:
  W = 10
elif winms >= 28.5 and winms <= 32.6:
  W = 11
elif winms >= 32.7:
  W = 12

print direction+" "+str(W)
