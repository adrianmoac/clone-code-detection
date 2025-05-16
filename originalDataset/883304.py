# 提出2
def kakudai(fig):
    for i in range(len(fig)):
            now=fig[i]
            for n in range(len(now)):
                pixel=fig[i][n]
                if i==0:
                    if n==0:
                        if "." not in [fig[i][n],fig[i][n+1],fig[i+1][n],fig[i+1][n+1]] :
                            temp2[i][n] = "#"
                    elif n==int(W)-1:
                        if "." not in [fig[i][n],fig[i][n-1],fig[i+1][n],fig[i+1][n-1]] :
                            temp2[i][n] = "#"
                    else:
                        if "." not in [fig[i][n],fig[i][n+1],fig[i][n-1],fig[i+1][n],fig[i+1][n+1],fig[i+1][n-1]] :
                            temp2[i][n] = "#"
                elif i==int(H)-1:
                    if n==0:
                        if "." not in [fig[i][n],fig[i][n+1],fig[i-1][n],fig[i-1][n+1]] :
                            temp2[i][n] = "#"
                    elif n==int(W)-1:
                        if "." not in [fig[i][n],fig[i][n-1],fig[i-1][n],fig[i-1][n-1]] :
                            temp2[i][n] = "#"
                    else:
                        if "." not in [fig[i][n],fig[i][n+1],fig[i][n-1],fig[i-1][n],fig[i-1][n+1],fig[i-1][n-1]] :
                            temp2[i][n] = "#"
                else:
                    if n==0:
                        if "." not in [fig[i][n],fig[i][n+1],fig[i+1][n],fig[i+1][n+1],fig[i-1][n],fig[i-1][n+1]] :
                            temp2[i][n] = "#"
                    elif n==int(W)-1:
                        if "." not in [fig[i][n],fig[i][n-1],fig[i+1][n],fig[i+1][n-1],fig[i-1][n],fig[i-1][n-1]] :
                            temp2[i][n] = "#"
                    else:
                        if "." not in [fig[i][n],fig[i][n+1],fig[i][n-1],fig[i+1][n],fig[i+1][n+1],fig[i+1][n-1],fig[i-1][n],fig[i-1][n+1],fig[i-1][n-1]] :
                            temp2[i][n] = "#"

def syusyuku(fig):
    for i in range(len(fig)):
        now=fig[i]
        for n in range(len(now)):
            pixel=fig[i][n]
            if i==0:
                if n==0:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n+1] = "#"
                        temp1[i+1][n] = "#"
                        temp1[i+1][n+1] = "#"
                elif n==int(W)-1:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n-1] = "#"
                        temp1[i+1][n] = "#"
                        temp1[i+1][n-1] = "#"
                else:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n-1] = "#"
                        temp1[i][n+1] = "#"
                        temp1[i+1][n] = "#"
                        temp1[i+1][n-1] = "#"
                        temp1[i+1][n+1] = "#"
            elif i==int(H)-1:
                if n==0:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n+1] = "#"
                        temp1[i-1][n] = "#"
                        temp1[i-1][n+1] = "#"
                elif n==int(W)-1:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n-1] = "#"
                        temp1[i-1][n] = "#"
                        temp1[i-1][n-1] = "#"
                else:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n-1] = "#"
                        temp1[i][n+1] = "#"
                        temp1[i-1][n] = "#"
                        temp1[i-1][n-1] = "#"
                        temp1[i-1][n+1] = "#"
            else:
                if n==0:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n+1] = "#"
                        temp1[i+1][n] = "#"
                        temp1[i+1][n+1] = "#"
                        temp1[i-1][n] = "#"
                        temp1[i-1][n+1] = "#"
                elif n==int(W)-1:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n-1] = "#"
                        temp1[i+1][n] = "#"
                        temp1[i+1][n-1] = "#"
                        temp1[i-1][n] = "#"
                        temp1[i-1][n-1] = "#"
                else:
                    if pixel=="#":
                        temp1[i][n] = "#"
                        temp1[i][n-1] = "#"
                        temp1[i][n+1] = "#"
                        temp1[i+1][n] = "#"
                        temp1[i+1][n-1] = "#"
                        temp1[i+1][n+1] = "#"
                        temp1[i-1][n] = "#"
                        temp1[i-1][n-1] = "#"
                        temp1[i-1][n+1] = "#"
                        

H,W=input().split(" ")
fig=[input() for i in range(int(H))]
temp1=[["." for n in range(int(W))] for i in range(int(H))]
temp2=[["." for n in range(int(W))] for i in range(int(H))]

if W=="1" and H=="1":
    print("possible")
    print(fig[0])
        
elif W=="1" or H=="1":
    num=int(W)*int(H)
    fig=[i for i in "".join(fig)]
    for i in range(num):
        if i==0:
            temp1[i] = "#" if (fig[i]=="#" and fig[i+1]=="#") else "."
        elif i==num-1:
            temp1[i] = "#" if (fig[i]=="#" and fig[i-1]=="#") else "."
        else:
            temp1[i] = "#" if (fig[i]=="#" and fig[i+1]=="#" and fig[i-1]=="#") else "."
    for i in range(num):
        if i==0:
            if temp1[i] == "#":
                temp2[i] = "#"
                temp2[i+1] = "#"
        elif i==num-1:
            if temp1[i] == "#":
                temp2[i] = "#"
                temp2[i-1] = "#"
        else:
            if temp1[i] == "#":
                temp2[i] = "#"
                temp2[i+1] = "#"
                temp2[i-1] = "#"
    if fig==temp1:
        if W=="1":
            print("possible")
            for i in range(len(temp1)):
                print(temp1[i])
        else:
            print("possible")
            print("".join(temp1))
    else:
        print("impossible")
else:
    kakudai(fig)
    syusyuku(temp2)
    if fig == ["".join(i) for i in temp1]:
        print("possible")
        for i in temp2:
            print("".join(i))
    else:
        print("impossible")