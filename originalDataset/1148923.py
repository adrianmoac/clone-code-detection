a = int(input())
b = list(input())
frag = 0
parks = [list("SS"),list("SW"),list("WS"),list("WW")]
for park in parks:
    for i in range(len(b)-2):
        if b[i+1] == "o":
            if park[i]=="S" and park[i+1]=="S":
                park.append("S")
            elif park[i]=="S" and park[i+1]=="W":
                park.append("W")
            elif park[i]=="W" and park[i+1]=="S":
                park.append("W")
            elif park[i]=="W" and park[i+1]=="W":
                park.append("S")
        elif b[i+1] == "x":
            if park[i]=="S" and park[i+1]=="S":
                park.append("W")
            elif park[i]=="S" and park[i+1]=="W":
                park.append("S")
            elif park[i]=="W" and park[i+1]=="S":
                park.append("S")
            elif park[i]=="W" and park[i+1]=="W":
                park.append("W")
    
    frag2 = 0
    if b[0]=="o":
        if park[0] == "S":
            if park[-1]==park[1]:
                frag2 = 1 
        if park[0] == "W":
            if park[-1]!=park[1]:
                frag2 = 1
    if b[0]=="x":
        if park[0] == "S":
            if park[-1]!=park[1]:
                frag2 = 1
        if park[0] == "W":
            if park[-1]==park[1]:
                frag2 = 1
                
    if frag2 == 1:
        if b[-1]=="o":
            if park[-1] == "S":
                if park[0]==park[-2]:
                    print (''.join(park))
                    frag = 1
                    break
            if park[-1] == "W":
                if park[0]!=park[-2]:
                    print (''.join(park))
                    frag = 1
                    break
        if b[-1]=="x":
            if park[-1] == "S":
                if park[0]!=park[-2]:
                    print (''.join(park))
                    frag = 1
                    break
            if park[-1] == "W":
                if park[0]==park[-2]:
                    print (''.join(park))
                    frag = 1
                    break
if frag == 0:
    print(-1)
        