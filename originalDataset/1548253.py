# -*- coding: utf-8 -*-
# C - 風力観測


def deg_to_dir(deg):
    """Summary line.

    風向から方位を返します。

    Args:
        deg (int): 風向

    Returns:
        string: 方位

    """
    degs_list = ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE',
                 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW']
    deg_index = ((deg * 10 + 1125) // 2250) % 16
    return degs_list[deg_index]


def dis_to_w(dis):
    """Summary line.

    風程から風力を返します。

    Args:
        des (int): 風程

    Returns:
        w (int): 風力

    """
    w = -1
    ws_list = [0.0, 0.3, 1.6, 3.4, 5.5, 8.0, 10.8,
               13.9, 17.2, 20.8, 24.5, 28.5, 32.7]
    r_dif = int(dis / 60 * 10 + 0.5) / 10
    for n in ws_list:
        if r_dif >= n:
            w += 1
        else:
            break
    return w


def dir_w(deg, dis):
    """Summary line.

    風向、風程から方位と風力を返します。

    Args:
        deg (int): 風程
        des (int): 風程

    Returns:
        (strint, int): (方位, 風力)のタプル

    """
    w = dis_to_w(dis)
    if w == 0:
        dir = 'C'
    else:
        dir = deg_to_dir(deg)
    return (dir, w)


Deg, Dis = map(int, input().split())

result = dir_w(Deg, Dis)

print(*result)
