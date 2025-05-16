#  coding:utf-8

def _func(n, s):
    res = ["S", "S"]
    for x in s[1:-1]:
        if x == "o":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("S")
            else:
                res.append("W")
        elif x == "x":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("W")
            else:
                res.append("S")
    else:
        if (s[0], s[-1]) == ("o", "o"):
            if (res[-2], res[-1]) == ("S", "S"):
                return "".join(res)
        elif (s[0], s[-1]) == ("o", "x"):
            if (res[-2], res[-1]) == ("W", "S"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "o"):
            if (res[-2], res[-1]) == ("W", "W"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "x"):
            if (res[-2], res[-1]) == ("S", "W"):
                return "".join(res)
        
    res = ["S", "W"]
    for x in s[1:-1]:
        if x == "o":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("S")
            else:
                res.append("W")
        elif x == "x":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("W")
            else:
                res.append("S")
    else:
        if (s[0], s[-1]) == ("o", "o"):
            if (res[-2], res[-1]) == ("W", "W"):
                return "".join(res)
        elif (s[0], s[-1]) == ("o", "x"):
            if (res[-2], res[-1]) == ("S", "W"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "o"):
            if (res[-2], res[-1]) == ("S", "S"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "x"):
            if (res[-2], res[-1]) == ("W", "S"):
                return "".join(res)

    res = ["W", "S"]
    for x in s[1:-1]:
        if x == "o":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("S")
            else:
                res.append("W")
        elif x == "x":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("W")
            else:
                res.append("S")
    else:
        if (s[0], s[-1]) == ("o", "o"):
            if (res[-2], res[-1]) == ("S", "W"):
                return "".join(res)
        elif (s[0], s[-1]) == ("o", "x"):
            if (res[-2], res[-1]) == ("W", "W"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "o"):
            if (res[-2], res[-1]) == ("S", "S"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "x"):
            if (res[-2], res[-1]) == ("W", "S"):
                return "".join(res)

    res = ["W", "W"]
    for x in s[1:-1]:
        if x == "o":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("S")
            else:
                res.append("W")
        elif x == "x":
            if ((res[-2] == "S" and res[-1] == "S") or
                (res[-2] == "W" and res[-1] == "W")):
                res.append("W")
            else:
                res.append("S")
    else:
        if (s[0], s[-1]) == ("o", "o"):
            if (res[-2], res[-1]) == ("W", "S"):
                return "".join(res)
        elif (s[0], s[-1]) == ("o", "x"):
            if (res[-2], res[-1]) == ("S", "S"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "o"):
            if (res[-2], res[-1]) == ("S", "W"):
                return "".join(res)
        elif (s[0], s[-1]) == ("x", "x"):
            if (res[-2], res[-1]) == ("W", "W"):
                return "".join(res)

    return -1


if __name__ == "__main__":
    n = int(raw_input())
    S = raw_input()
    print _func(n, S)