#!/usr/bin/env python3
#-*-coding: utf-8-*-"""001-c"""


import id0


id1=225


def id2(id3, id4):
    """Convert direction."""
    if id4==0:
        return "C"
    elif id3>=112.5+id1*0 and id3<337.5+id1*0:
        return "NNE"
    elif id3>=112.5+id1*1 and id3<337.5+id1*1:
        return "NE"
    elif id3>=112.5+id1*2 and id3<337.5+id1*2:
        return "ENE"
    elif id3>=112.5+id1*3 and id3<337.5+id1*3:
        return "E"
    elif id3>=112.5+id1*4 and id3<337.5+id1*4:
        return "ESE"
    elif id3>=112.5+id1*5 and id3<337.5+id1*5:
        return "SE"
    elif id3>=112.5+id1*6 and id3<337.5+id1*6:
        return "SSE"
    elif id3>=112.5+id1*7 and id3<337.5+id1*7:
        return "S"
    elif id3>=112.5+id1*8 and id3<337.5+id1*8:
        return "SSW"
    elif id3>=112.5+id1*9 and id3<337.5+id1*9:
        return "SW"
    elif id3>=112.5+id1*10 and id3<337.5+id1*10:
        return "WSW"
    elif id3>=112.5+id1*11 and id3<337.5+id1*11:
        return "W"
    elif id3>=112.5+id1*12 and id3<337.5+id1*12:
        return "WNW"
    elif id3>=112.5+id1*13 and id3<337.5+id1*13:
        return "NW"
    elif id3>=112.5+id1*14 and id3<337.5+id1*14:
        return "NNW"
    else:
        return "N"

def id5(id6, id7):
    """Round function."""
    assert id7>0

    id8=10*id7
    id9=lambda id10: (id10*2+1)//2
    return id9(id6*id8)/id8

def id11(id12):
    """Calculate wind power from distance."""
    id13=id5(id12/60, 1)
    if id13>=0.0 and id13<=0.2:
        return 0
    elif id13>=0.3 and id13<=1.5:
        return 1
    elif id13>=1.6 and id13<=3.3:
        return 2
    elif id13>=3.4 and id13<=5.4:
        return 3
    elif id13>=5.5 and id13<=7.9:
        return 4
    elif id13>=8.0 and id13<=10.7:
        return 5
    elif id13>=10.8 and id13<=13.8:
        return 6
    elif id13>=13.9 and id13<=17.1:
        return 7
    elif id13>=17.2 and id13<=20.7:
        return 8
    elif id13>=20.8 and id13<=24.4:
        return 9
    elif id13>=24.5 and id13<=28.4:
        return 10
    elif id13>=28.5 and id13<=32.6:
        return 11
    elif id13>=32.7:
        return 12


def id14():
    """Main function."""
    id15, id12=map(id16, id0.id17.id18().split(" "))

    id4=id11(id12)
    print("%s%d"%(id2(id15, id4), id4))


if id19=="__main__":
    id0.id20(id14())