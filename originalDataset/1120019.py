def findNextAnimal(oxList, swList, index):
    nextAns = oxList[index]
    before = swList[index-1]
    animal = swList[index]
    nextAnimal = ""
    if(nextAns == "o" and before == "S" and animal == "S"):
        nextAnimal = "S"
    elif(nextAns == "o" and before == "S" and animal == "W"):
        nextAnimal = "W"
    elif(nextAns == "o" and before == "W" and animal == "S"):
        nextAnimal = "W"
    elif(nextAns == "o" and before == "W" and animal == "W"):
        nextAnimal = "S"
    elif(nextAns == "x" and before == "S" and animal == "S"):
        nextAnimal = "W"
    elif(nextAns == "x" and before == "S" and animal == "W"):
        nextAnimal = "S"
    elif(nextAns == "x" and before == "W" and animal == "S"):
        nextAnimal = "S"
    elif(nextAns == "x" and before == "W" and animal == "W"):
        nextAnimal = "W"
    return nextAnimal

def checkList(oxList, swList):
    ans = 0
    if(swList[-1] == "S"):
        if(oxList[-1] == "x" and swList[-2] != swList[0]):
            ans = 1
        elif(oxList[-1] == "o" and swList[-2] == swList[0]):
            ans = 1
    elif(swList[-1] == "W"):
        if(oxList[-1] == "x" and swList[-2] == swList[0]):
            ans = 1
        elif(oxList[-1] == "o" and swList[-2] != swList[0]):
            ans = 1
            
    ans2 = 0    
    if(swList[0] == "S"):
        if(oxList[0] == "x" and swList[1] != swList[-1]):
            ans2 = 1
        elif(oxList[0] == "o" and swList[1] == swList[-1]):
            ans2 = 1
    elif(swList[0] == "W"):
        if(oxList[0] == "x" and swList[1] == swList[-1]):
            ans2 = 1
        elif(oxList[0] == "o" and swList[1] != swList[-1]):
            ans2 = 1
    
    return ans*ans2

try:
    while True:  
        n = raw_input().strip().upper()
        oxList = raw_input().strip().lower()
        ans = -1
        for s0 in ["S", "W"]:
            for s1 in ["S","W"]:
                swList = [0]*int(n)
                swList[0] = s0
                swList[1] = s1
                for i in range(2, int(n)):
                    nextAnimal = findNextAnimal(oxList, swList, i-1)
                    swList[i] = nextAnimal
                    flag = checkList(oxList, swList)
                    if(flag == 1):
                        ans = ""
                        for s in swList:
                            ans += s
        print ans
                        
except EOFError:
    pass