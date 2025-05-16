import id0
id1,id2=map(id3,(input().split()))

id1=id1/10
id4=lambda id5:(id5*2+1)//2
id2=id4(id2/6)/10

id6,id7="",0

if id1<11.25:
    id6="N"
elif id1<=33.75:
    id6="NNE"
elif id1<=56.25:
    id6="NE"
elif id1<=78.75:
    id6="ENE"
elif id1<=101.25:
    id6="E"
elif id1<=123.75:
    id6="ESE"
elif id1<=146.25:
    id6="SE"
elif id1<=168.75:
    id6="SSE"
elif id1<=191.25:
    id6="S"
elif id1<=213.75 :
    id6="SSW"
elif id1<=236.25 :
    id6="SW"
elif id1<=258.75 :
    id6="WSW"
elif id1<=281.25 :
    id6="W"
elif id1<=303.75 :
    id6="WNW"
elif id1<=326.25 :
    id6="NW"
elif id1<=348.75 :
    id6="NNW"
elif id1>348.75 :
    id6="N"

if id2<=0.2:
    id7=0
elif id2<=1.5:
    id7=1
elif id2<=3.3:
    id7=2
elif id2<=5.4:
    id7=3
elif id2<=7.9:
    id7=4
elif id2<=10.7:
    id7=5
elif id2<=13.8:
    id7=6
elif id2<=17.1:
    id7=7
elif id2<=20.7:
    id7=8
elif id2<=24.4:
    id7=9
elif id2<=28.4 :
    id7=10
elif id2<=32.6 :
    id7=11
elif id2>=32.7:
    id7=12

if(id7==0):
    print("C "+id8(id7))
else:
    print(id6+" "+id8(id7))