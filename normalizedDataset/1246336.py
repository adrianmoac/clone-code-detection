import id0
 
id1, id2=map(id3, input().split())
 
id4=lambda id5:(id5*2+1)//2
 
id1/=10
id2=id4(id2/6)
id2/=10
 
id6=""
id7=""
 
if id2<=0.2:
    id6="0"
elif 0.3<=id2 and id2<=1.5:
    id6="1"
elif 1.6<=id2 and id2<=3.3:
    id6="2"
elif 3.4<=id2 and id2<=5.4:
    id6="3"
elif 5.5<=id2 and id2<=7.9:
    id6="4"
elif 8.0<=id2 and id2<=10.7:
    id6="5"
elif 10.8<=id2 and id2<=13.8:
    id6="6"
elif 13.9<=id2 and id2<=17.1:
    id6="7"
elif 17.2<=id2 and id2<=20.7:
    id6="8"
elif 20.8<=id2 and id2<=24.4:
    id6="9"
elif 24.5<=id2 and id2<=28.4:
    id6="10"
elif 28.5<=id2 and id2<=32.6:
    id6="11"
elif 32.7<=id2:
    id6="12"
 
if id6=="0":
    id7="C"
elif 11.25<=id1 and id1<33.75 :
    id7="NNE"
elif 33.75<=id1 and id1<56.25 :
    id7="NE"
elif 56.25<=id1 and id1<78.75 :
    id7="ENE"
elif 78.75<=id1 and id1<101.25 :
    id7="E"
elif 101.25<=id1 and id1<123.75 :
    id7="ESE"
elif 123.75<=id1 and id1<146.25 :
    id7="SE"
elif 146.25<=id1 and id1<168.75 :
    id7="SSE"
elif 168.75<=id1 and id1<191.25 :
    id7="S"
elif 191.25<=id1 and id1<213.75 :
    id7="SSW"
elif 213.75<=id1 and id1<236.25 :
    id7="SW"
elif 236.25<=id1 and id1<258.75 :
    id7="WSW"
elif 258.75<=id1 and id1<281.25 :
    id7="W"
elif 281.25<=id1 and id1<303.75 :
    id7="WNW"
elif 303.75<=id1 and id1<326.25 :
    id7="NW"
elif 326.25<=id1 and id1<348.75 :
    id7="NNW"
else:
    id7="N"
 
print(id7+" "+id6)