id0, id1=map(id2, input().split())
id1=id3(id1*1.0/60+0.00001, 1)

id4=[
    11.25,
    33.75,
    56.25,
    78.75,
    101.25,
    123.75,
    146.25,
    168.75,
    191.25,
    213.75,
    236.25,
    258.75,
    281.25,
    303.75,
    326.25,
    348.75
]

if 0.0<=id1<=0.2:
    id5=0
elif 0.3<=id1<=1.5:
    id5=1
elif 1.6<=id1<=3.3:
    id5=2
elif 3.4<=id1<=5.4:
    id5=3
elif 5.5<=id1<=7.9:
    id5=4
elif 8.0<=id1<=10.7:
    id5=5
elif 10.8<=id1<=13.8:
    id5=6
elif 13.9<=id1<=17.1:
    id5=7
elif 17.2<=id1<=20.7:
    id5=8
elif 20.8<=id1<=24.4:
    id5=9
elif 24.5<=id1<=28.4:
    id5=10
elif 28.5<=id1<=32.6:
    id5=11
else:
    id5=12

id6=id0/10

if id5==0:
    id7="C"
elif id4[0]<=id6<id4[1]:
    id7="NNE"
elif id4[1]<=id6<id4[2]:
    id7="NE"
elif id4[2]<=id6<id4[3]:
    id7="ENE"
elif id4[3]<=id6<id4[4]:
    id7="E"
elif id4[4]<=id6<id4[5]:
    id7="ESE"
elif id4[5]<=id6<id4[6]:
    id7="SE"
elif id4[6]<=id6<id4[7]:
    id7="SSE"
elif id4[7]<=id6<id4[8]:
    id7="S"
elif id4[8]<=id6<id4[9]:
    id7="SSW"
elif id4[9]<=id6<id4[10]:
    id7="SW"
elif id4[10]<=id6<id4[11]:
    id7="WSW"
elif id4[11]<=id6<id4[12]:
    id7="W"
elif id4[12]<=id6<id4[13]:
    id7="WNW"
elif id4[13]<=id6<id4[14]:
    id7="NW"
elif id4[14]<=id6<id4[15]:
    id7="NNW"
else:
    id7="N"

print(id7, id5)