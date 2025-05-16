import math
 
deg, dis = map(float, input().split())
 
round = lambda x:(x*2+1)//2
 
deg /= 10
dis = round(dis/6)
dis /= 10
 
w = ""
drc = ""
 
if dis <= 0.2:
    w = "0"
elif 0.3 <= dis and dis <= 1.5:
    w = "1"
elif 1.6 <= dis and dis <= 3.3:
    w = "2"
elif 3.4 <= dis and dis <= 5.4:
    w = "3"
elif 5.5 <= dis and dis <= 7.9:
    w = "4"
elif 8.0 <= dis and dis <= 10.7:
    w = "5"
elif 10.8 <= dis and dis <= 13.8:
    w = "6"
elif 13.9 <= dis and dis <= 17.1:
    w = "7"
elif 17.2 <= dis and dis <= 20.7:
    w = "8"
elif 20.8 <= dis and dis <= 24.4:
    w = "9"
elif 24.5 <= dis and dis <= 28.4:
    w = "10"
elif 28.5 <= dis and dis <= 32.6:
    w = "11"
elif 32.7 <= dis:
    w = "12"
 
if w == "0":
    drc  = "C"
elif 11.25 <= deg and deg < 33.75 :
    drc = "NNE"
elif 33.75 <= deg and deg < 56.25 :
    drc = "NE"
elif 56.25 <= deg and deg < 78.75 :
    drc = "ENE"
elif 78.75 <= deg and deg < 101.25 :
    drc = "E"
elif 101.25 <= deg and deg < 123.75 :
    drc = "ESE"
elif 123.75 <= deg and deg < 146.25 :
    drc = "SE"
elif 146.25 <= deg and deg < 168.75 :
    drc = "SSE"
elif 168.75 <= deg and deg < 191.25 :
    drc = "S"
elif 191.25 <= deg and deg < 213.75 :
    drc = "SSW"
elif 213.75 <= deg and deg < 236.25 :
    drc = "SW"
elif 236.25 <= deg and deg < 258.75 :
    drc = "WSW"
elif 258.75 <= deg and deg < 281.25 :
    drc = "W"
elif 281.25 <= deg and deg < 303.75 :
    drc = "WNW"
elif 303.75 <= deg and deg < 326.25 :
    drc = "NW"
elif 326.25 <= deg and deg < 348.75 :
    drc = "NNW"
else:
    drc = "N"
 
print(drc + " " + w)