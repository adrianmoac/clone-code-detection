def round(x, d=0):
    p=10**d
    return (x*p*2+1)//2/p

def calc_deg(d, fusoku):
    if fusoku == 0:
        return 'C'

    if d < 1125:
        return 'N'
    elif d < 3375:
        return 'NNE'
    elif d < 5625:
        return 'NE'
    elif d < 7875:
        return 'ENE'
    elif d < 10125:
        return 'E'
    elif d < 12375:
        return 'ESE'
    elif d < 14625:
        return 'SE'
    elif d < 16875:
        return 'SSE'
    elif d < 19125:
        return 'S'
    elif d < 21375:
        return 'SSW'
    elif d < 23625:
        return 'SW'
    elif d < 25875:
        return 'WSW'
    elif d < 28125:
        return 'W'
    elif d < 30375:
        return 'WNW'
    elif d < 32625:
        return 'NW'
    elif d < 34875:
        return 'NNW'
    else:
        return 'N'


def calc_fusoku(d):
    speed = round(d/60, 1)
    if speed <= 0.2:
        return 0
    elif speed <= 1.5:
        return 1
    elif speed <= 3.3:
        return 2
    elif speed <= 5.4:
        return 3
    elif speed <= 7.9:
        return 4
    elif speed <= 10.7:
        return 5
    elif speed <= 13.8:
        return 6
    elif speed <= 17.1:
        return 7
    elif speed <= 20.7:
        return 8
    elif speed <= 24.4:
        return 9
    elif speed <= 28.4:
        return 10
    elif speed <= 32.6:
        return 11
    else:
        return 12


deg, dis = map(int, input().split())
fusoku = calc_fusoku(dis)
deg = calc_deg(deg * 10, fusoku)
print("{} {}".format(deg, fusoku))
