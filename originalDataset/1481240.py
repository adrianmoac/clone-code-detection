# coding:utf-8


def wind_info(dig, dis):
    # wind_direction
    dig /= 10
    if 11.25 <= dig < 33.75:
        direction = 'NNE'
    elif 33.75 <= dig < 56.25:
        direction = 'NE'
    elif 56.25 <= dig < 78.75:
        direction = 'ENE'
    elif 78.75 <= dig < 101.25:
        direction = 'E'
    elif 101.25 <= dig < 123.75:
        direction = 'ESE'
    elif 123.75 <= dig < 146.25:
        direction = 'SE'
    elif 146.25 <= dig < 168.75:
        direction = 'SSE'
    elif 168.75 <= dig < 191.25:
        direction = 'S'
    elif 191.25 <= dig < 213.75:
        direction = 'SSW'
    elif 213.75 <= dig < 236.25:
        direction = 'SW'
    elif 236.25 <= dig < 258.75:
        direction = 'WSW'
    elif 258.75 <= dig < 281.25:
        direction = 'W'
    elif 281.25 <= dig < 303.75:
        direction = 'WNW'
    elif 303.75 <= dig < 326.25:
        direction = 'NW'
    elif 326.25 <= dig < 348.75:
        direction = 'NNW'
    else:
        direction = 'N'

    # wind_power
    dis = (dis / 60 * 10 * 2 + 1) // 2 / 10
    if 0.0 <= dis <= 0.2:
        return ['C', 0]
    elif 0.3 <= dis <= 1.5:
        power = 1
    elif 1.6 <= dis <= 3.3:
        power = 2
    elif 3.4 <= dis <= 5.4:
        power = 3
    elif 5.5 <= dis <= 7.9:
        power = 4
    elif 8.0 <= dis <= 10.7:
        power = 5
    elif 10.8 <= dis <= 13.8:
        power = 6
    elif 13.9 <= dis <= 17.1:
        power = 7
    elif 17.2 <= dis <= 20.7:
        power = 8
    elif 20.8 <= dis <= 24.4:
        power = 9
    elif 24.5 <= dis <= 28.4:
        power = 10
    elif 28.5 <= dis <= 32.6:
        power = 11
    elif 32.7 <= dis:
        power = 12

    return [direction, power]

dig, dis = map(int, input().split())
print("{} {}".format(*wind_info(dig, dis)))
