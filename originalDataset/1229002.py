def main():
    Deg, Dis = map(int, input().split())

    if 112.5 <= Deg < 337.5:
        dir = 'NNE'
    elif 337.5 <= Deg < 562.5:
        dir = 'NE'
    elif 562.5 <= Deg < 787.5:
        dir = 'ENE'
    elif 787.5 <= Deg < 1012.5:
        dir = 'E'
    elif 1012.5 <= Deg < 1237.5:
        dir = 'ESE'
    elif 1237.5 <= Deg < 1462.5:
        dir = 'SE'
    elif 1462.5 <= Deg < 1687.5:
        dir = 'SSE'
    elif 1687.5 <= Deg < 1912.5:
        dir = 'S'
    elif 1912.5 <= Deg < 2137.5:
        dir = 'SSW'
    elif 2137.5 <= Deg < 2362.5:
        dir = 'SW'
    elif 2362.5 <= Deg < 2587.5:
        dir = 'WSW'
    elif 2587.5 <= Deg < 2812.5:
        dir = 'W'
    elif 2812.5 <= Deg < 3037.5:
        dir = 'WNW'
    elif 3037.5 <= Deg < 3262.5:
        dir = 'NW'
    elif 3262.5 <= Deg < 3487.5:
        dir = 'NNW'
    else:
        dir = 'N'

    ws = (Dis / 60 * 20 + 1) // 2 / 10
    if 0 <= ws <= 0.2:
        w = 0
        dir = 'C'
    elif 0.3 <= ws <= 1.5:
        w = 1
    elif 1.6 <= ws <= 3.3:
        w = 2
    elif 3.4 <= ws <= 5.4:
        w = 3
    elif 5.5 <= ws <= 7.9:
        w = 4
    elif 8.0 <= ws <= 10.7:
        w = 5
    elif 10.8 <= ws <= 13.8:
        w = 6
    elif 13.9 <= ws <= 17.1:
        w = 7
    elif 17.2 <= ws <= 20.7:
        w = 8
    elif 20.8 <= ws <= 24.4:
        w = 9
    elif 24.5 <= ws <= 28.4:
        w = 10
    elif 28.5 <= ws <= 32.6:
        w = 11
    else:
        w = 12

    print('{} {}'.format(dir, w))

main()
