deg, dis = map(int, input().split())
dis = round(dis * 1.0 / 60 + 0.00001, 1)

adeg = [
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

if 0.0 <= dis <= 0.2:
    n = 0
elif 0.3 <= dis <= 1.5:
    n = 1
elif 1.6 <= dis <= 3.3:
    n = 2
elif 3.4 <= dis <= 5.4:
    n = 3
elif 5.5 <= dis <= 7.9:
    n = 4
elif 8.0 <= dis <= 10.7:
    n = 5
elif 10.8 <= dis <= 13.8:
    n = 6
elif 13.9 <= dis <= 17.1:
    n = 7
elif 17.2 <= dis <= 20.7:
    n = 8
elif 20.8 <= dis <= 24.4:
    n = 9
elif 24.5 <= dis <= 28.4:
    n = 10
elif 28.5 <= dis <= 32.6:
    n = 11
else:
    n = 12

t = deg / 10

if n == 0:
    s = 'C'
elif adeg[0] <= t < adeg[1]:
    s = 'NNE'
elif adeg[1] <= t < adeg[2]:
    s = 'NE'
elif adeg[2] <= t < adeg[3]:
    s = 'ENE'
elif adeg[3] <= t < adeg[4]:
    s = 'E'
elif adeg[4] <= t < adeg[5]:
    s = 'ESE'
elif adeg[5] <= t < adeg[6]:
    s = 'SE'
elif adeg[6] <= t < adeg[7]:
    s = 'SSE'
elif adeg[7] <= t < adeg[8]:
    s = 'S'
elif adeg[8] <= t < adeg[9]:
    s = 'SSW'
elif adeg[9] <= t < adeg[10]:
    s = 'SW'
elif adeg[10] <= t < adeg[11]:
    s = 'WSW'
elif adeg[11] <= t < adeg[12]:
    s = 'W'
elif adeg[12] <= t < adeg[13]:
    s = 'WNW'
elif adeg[13] <= t < adeg[14]:
    s = 'NW'
elif adeg[14] <= t < adeg[15]:
    s = 'NNW'
else:
    s = 'N'

print(s, n)