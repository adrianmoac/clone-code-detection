#-*-coding: utf-8-*-# C-風力観測


def id0(id1):
    """Summary line.

    風向から方位を返します。

    Args:
        deg (int): 風向

    Returns:
        string: 方位

    """
    id2=["N", "NNE", "NE", "ENE", "E", "ESE", "SE", "SSE",
                 "S", "SSW", "SW", "WSW", "W", "WNW", "NW", "NNW"]
    id3=((id1*10+1125)//2250)%16
    return id2[id3]


def id4(id5):
    """Summary line.

    風程から風力を返します。

    Args:
        des (int): 風程

    Returns:
        w (int): 風力

    """
    id6=-1
    id7=[0.0, 0.3, 1.6, 3.4, 5.5, 8.0, 10.8,
               13.9, 17.2, 20.8, 24.5, 28.5, 32.7]
    id8=id9(id5/60*10+0.5)/10
    for id10 in id7:
        if id8>=id10:
            id6+=1
        else:
            break
    return id6


def id11(id1, id5):
    """Summary line.

    風向、風程から方位と風力を返します。

    Args:
        deg (int): 風程
        des (int): 風程

    Returns:
        (strint, int): (方位, 風力)のタプル

    """
    id6=id4(id5)
    if id6==0:
        id12="C"
    else:
        id12=id0(id1)
    return (id12, id6)


id13, id14=map(id9, input().split())

id15=id11(id13, id14)

print(*id15)