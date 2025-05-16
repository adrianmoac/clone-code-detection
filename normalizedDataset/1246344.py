import id0
id1,id2=id3(map(id4,input().split()))
 
id5=lambda id6:(id6*2+1)//2
 
id7=""
id1/=10
id2=id5(id2/6)
id2/=10
 
if 11.25<=id1 and id1<33.75 :
    id8="NNE"
elif 33.75<=id1 and id1<56.25 :
    id8="NE"
elif 56.25<=id1 and id1<78.75 :
    id8="ENE"
elif 78.75<=id1 and id1<101.25 :
    id8="E"
elif 101.25<=id1 and id1<123.75 :
    id8="ESE"
elif 123.75<=id1 and id1<146.25 :
    id8="SE"
elif 146.25<=id1 and id1<168.75 :
    id8="SSE"
elif 168.75<=id1 and id1<191.25 :
    id8="S"
elif 191.25<=id1 and id1<213.75 :
    id8="SSW"
elif 213.75<=id1 and id1<236.25 :
    id8="SW"
elif 236.25<=id1 and id1<258.75 :
    id8="WSW"
elif 258.75<=id1 and id1<281.25 :
    id8="W"
elif 281.25<=id1 and id1<303.75 :
    id8="WNW"
elif 303.75<=id1 and id1<326.25 :
    id8="NW"
elif 326.25<=id1 and id1<348.75 :
    id8="NNW"
else:
    id8="N"
 
if id2<=0.2:
    id8="C"
    id9="0"
elif 0.3<=id2 and id2<=1.5:
    id9="1"
elif 1.6<=id2 and id2<=3.3:
    id9="2"
elif 3.4<=id2 and id2<=5.4:
    id9="3"
elif 5.5<=id2 and id2<=7.9:
    id9="4"
elif 8.0<=id2 and id2<=10.7:
    id9="5"
elif 10.8<=id2 and id2<=13.8:
    id9="6"
elif 13.9<=id2 and id2<=17.1:
    id9="7"
elif 17.2<=id2 and id2<=20.7:
    id9="8"
elif 20.8<=id2 and id2<=24.4:
    id9="9"
elif 24.5<=id2 and id2<=28.4:
    id9="10"
elif 28.5<=id2 and id2<=32.6:
    id9="11"
elif 32.7<=id2:
    id9="12"
 
print(id8+" "+id9)