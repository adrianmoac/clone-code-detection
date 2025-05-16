#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""001-c"""


import sys


STEP = 225


def convertDirection(dir, wind_power):
    """Convert direction."""
    if wind_power == 0:
        return "C"
    elif dir >= 112.5 + STEP * 0 and dir < 337.5 + STEP * 0:
        return "NNE"
    elif dir >= 112.5 + STEP * 1 and dir < 337.5 + STEP * 1:
        return "NE"
    elif dir >= 112.5 + STEP * 2 and dir < 337.5 + STEP * 2:
        return "ENE"
    elif dir >= 112.5 + STEP * 3 and dir < 337.5 + STEP * 3:
        return "E"
    elif dir >= 112.5 + STEP * 4 and dir < 337.5 + STEP * 4:
        return "ESE"
    elif dir >= 112.5 + STEP * 5 and dir < 337.5 + STEP * 5:
        return "SE"
    elif dir >= 112.5 + STEP * 6 and dir < 337.5 + STEP * 6:
        return "SSE"
    elif dir >= 112.5 + STEP * 7 and dir < 337.5 + STEP * 7:
        return "S"
    elif dir >= 112.5 + STEP * 8 and dir < 337.5 + STEP * 8:
        return "SSW"
    elif dir >= 112.5 + STEP * 9 and dir < 337.5 + STEP * 9:
        return "SW"
    elif dir >= 112.5 + STEP * 10 and dir < 337.5 + STEP * 10:
        return "WSW"
    elif dir >= 112.5 + STEP * 11 and dir < 337.5 + STEP * 11:
        return "W"
    elif dir >= 112.5 + STEP * 12 and dir < 337.5 + STEP * 12:
        return "WNW"
    elif dir >= 112.5 + STEP * 13 and dir < 337.5 + STEP * 13:
        return "NW"
    elif dir >= 112.5 + STEP * 14 and dir < 337.5 + STEP * 14:
        return "NNW"
    else:
        return "N"

def round_(val, decimal_place):
    """Round function."""
    assert decimal_place > 0

    n = 10 * decimal_place
    r = lambda x: (x * 2 + 1) // 2
    return r(val * n) / n

def calcWindPower(dis):
    """Calculate wind power from distance."""
    wind_speed = round_(dis / 60, 1)
    if wind_speed >= 0.0 and wind_speed <= 0.2:
        return 0
    elif wind_speed >= 0.3 and wind_speed <= 1.5:
        return 1
    elif wind_speed >= 1.6 and wind_speed <= 3.3:
        return 2
    elif wind_speed >= 3.4 and wind_speed <= 5.4:
        return 3
    elif wind_speed >= 5.5 and wind_speed <= 7.9:
        return 4
    elif wind_speed >= 8.0 and wind_speed <= 10.7:
        return 5
    elif wind_speed >= 10.8 and wind_speed <= 13.8:
        return 6
    elif wind_speed >= 13.9 and wind_speed <= 17.1:
        return 7
    elif wind_speed >= 17.2 and wind_speed <= 20.7:
        return 8
    elif wind_speed >= 20.8 and wind_speed <= 24.4:
        return 9
    elif wind_speed >= 24.5 and wind_speed <= 28.4:
        return 10
    elif wind_speed >= 28.5 and wind_speed <= 32.6:
        return 11
    elif wind_speed >= 32.7:
        return 12


def main():
    """Main function."""
    deg, dis = map(int, sys.stdin.readline().split(' '))

    wind_power = calcWindPower(dis)
    print("%s %d" % (convertDirection(deg, wind_power), wind_power))


if __name__ == '__main__':
    sys.exit(main())
