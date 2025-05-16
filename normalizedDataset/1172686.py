#!/usr/local/bin
id0,id1=id2().split()
id3="N"
id4=id5(id0)
if id4>=112.5 and id4<337.5:
  id3="NNE"      
elif id4>=337.5 and id4<562.5:
  id3="NE"
elif id4>=562.5 and id4<787.5:
  id3="ENE"
elif id4>=787.5 and id4<1012.5:
  id3="E"
elif id4>=1012.5 and id4<1237.5:
  id3="ESE"
elif id4>=1237.5 and id4<1462.5:
  id3="SE"
elif id4>=1462.5 and id4<1687.5:
  id3="SSE"
elif id4>=1687.5 and id4<1912.5:
  id3="S"
elif id4>=1912.5 and id4<2137.5:
  id3="SSW"
elif id4>=2137.5 and id4<2362.5:
  id3="SW"
elif id4>=2362.5 and id4<2587.5:
  id3="WSW"
elif id4>=2587.5 and id4<2812.5:
  id3="W"
elif id4>=2812.5 and id4<3037.5:
  id3="WNW"
elif id4>=3037.5 and id4<3262.5:
  id3="NW"
elif id4>=3262.5 and id4<3487.5:
  id3="NNW"

id6=id7(id1)/60.0
id8=id9(id6)
id10=id8.split(".")

id11=id12(id6,1)

if id13(id10)==2:
  id14=id10[1]
  if id13(id14)>=2:
    if id14[1]=="5":
      id11=id12(id6,1)+0.1

id15=0

if id11>=0.0 and id11<=0.2:
  id15=0
  id3="C"
elif id11>=0.3 and id11<=1.5:
  id15=1
elif id11>=1.6 and id11<=3.3:
  id15=2
elif id11>=3.4 and id11<=5.4:
  id15=3
elif id11>=5.5 and id11<=7.9:
  id15=4
elif id11>=8.0 and id11<=10.7:
  id15=5
elif id11>=10.8 and id11<=13.8:
  id15=6
elif id11>=13.9 and id11<=17.1:
  id15=7
elif id11>=17.2 and id11<=20.7:
  id15=8
elif id11>=20.8 and id11<=24.4:
  id15=9
elif id11>=24.5 and id11<=28.4:
  id15=10
elif id11>=28.5 and id11<=32.6:
  id15=11
elif id11>=32.7:
  id15=12

print id3+" "+id9(id15)