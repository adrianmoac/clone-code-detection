def id0(id1):
    id2=(
        "N", "NNE", "NE", "ENE",
        "E", "ESE", "SE", "SSE",
        "S", "SSW", "SW", "WSW",
        "W", "WNW", "NW", "NNW"
    )
    id3=36000/16
    for id4 in id5(1, 16):
        id6=id3*id4-id3//2
        id7=id3*id4+id3//2
        if id6<=10*id1<id7:
            return id2[id4]
    return id2[0]
def id8(id9):
    id10=id11(60*id12 for id12 in (
         0,
         0.25,
         1.55,
         3.35,
         5.45,
         7.95,
        10.75,
        13.85,
        17.15,
        20.75,
        24.45,
        28.45,
        32.65
    ))
    for id4 in id5(id13(id10)-1):
        id6=id10[id4]
        id7=id10[id4+1]
        if id6<=id9<id7:
            return id4
    return id13(id10)-1
def id14():
    id1, id9=map(id15, input().split())
    id16=id0(id1)
    id17=id8(id9)
    if id17==0: id16="C"
    print("{} {}".id18(id16, id17))
if id19=="__main__": id14()