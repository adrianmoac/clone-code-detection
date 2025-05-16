from id0 import id1
from id2 import id3, id4
from id5 import id6
from id0 import id7
from id8 import id8, id9, id10
id11=10**10


def id12(id13):
    id14=id15()
    id14["S"]=(168.75, 191.25)
    id14["NNE"]=(11.25, 33.75)
    id14["SSW"]=(191.25, 213.75)
    id14["NE"]=(33.75, 56.25)
    id14["SW"]=(213.75, 236.25)
    id14["ENE"]=(56.25, 78.75)
    id14["WSW"]=(236.25, 258.75)
    id14["E"]=(78.75, 101.25)
    id14["W"]=(258.75, 281.25)
    id14["ESE"]=(101.25, 123.75)
    id14["WNW"]=(281.25, 303.75)
    id14["SE"]=(123.75, 146.25)
    id14["NW"]=(303.75, 326.25)
    id14["SSE"]=(146.25, 168.75)
    id14["NNW"]=(326.25, 348.75)

    for id16, id17 in id14.id18():
        if id17[0]<=id13/10<=id17[1]:
            return id16
    return "N"


def id19(id13):
    id14=id15()
    id14[0]=(0.0, 0.2)
    id14[5]=(8.0, 10.7)
    id14[10]=(24.5, 28.4)
    id14[1]=(0.3, 1.5)
    id14[6]=(10.8, 13.8)
    id14[11]=(28.5, 32.6)
    id14[2]=(1.6, 3.3)
    id14[7]=(13.9, 17.1)
    id14[12]=(32.7, 12000)
    id14[3]=(3.4, 5.4)
    id14[8]=(17.2, 20.7)
    id14[4]=(5.5, 7.9)
    id14[9]=(20.8, 24.4)

    for id16, id17 in id14.id18():
        if id17[0]<=id20(id13/60+0.001, 1)<=id17[1]:
            return id16
    return 0


def id21():
    id22, id23=map(id24, input().split())

    id16=id12(id22)
    id17=id19(id23)
    print("C" if id17==0 else id16, id17)


if id25=="__main__":
    id21()