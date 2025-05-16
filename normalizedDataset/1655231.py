#-*-coding: utf-8-*-from decimal import Decimal, ROUND_HALF_UP

# 入力の数値
id0, id1=map(id2, input().split())

# 風向の場合分け
id0/=10
id3="N"
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

# 風程を風速にする
id4=id1/60
# 小数第2位を四捨五入(python3はroundだといけない)
id5=id6(id7(id4))
id5=id5.id8(id6(".1"), id9)
id4=id10(id5)

# 風力の場合分け
if 0.0<=id4<=0.2:
	id11="0"
elif 0.3<=id4<=1.5:
	id11="1"
elif 1.6<=id4<=3.3:
	id11="2"
elif 3.4<=id4<=5.4:
	id11="3"
elif 5.5<=id4<=7.9:
	id11="4"
elif 8.0<=id4<=10.7:
	id11="5"
elif 10.8<=id4<=13.8:
	id11="6"
elif 13.9<=id4<=17.1:
	id11="7"
elif 17.2<=id4<=20.7:
	id11="8"
elif 20.8<=id4<=24.4:
	id11="9"
elif 24.5<=id4<=28.4:
	id11="10"
elif 28.5<=id4<=32.6:
	id11="11"
elif id4>=32.7:
	id11="12"

# 風力が0なら風向はCで確定
if id11=="0":
	id3="C"

print(id3+" "+id11)