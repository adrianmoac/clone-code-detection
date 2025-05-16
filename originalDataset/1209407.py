n = int(input())
sAry = []

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

for i in range(n):
    alphAry = [0] * 26
    s = list(input())
    for alph in s:
        if alph == 'a':
            alphAry[0] += 1
        elif alph == 'b':
            alphAry[1] += 1
        elif alph == 'c':
            alphAry[2] += 1
        elif alph == 'd':
            alphAry[3] += 1
        elif alph == 'e':
            alphAry[4] += 1
        elif alph == 'f':
            alphAry[5] += 1
        elif alph == 'g':
            alphAry[6] += 1
        elif alph == 'h':
            alphAry[7] += 1
        elif alph == 'i':
            alphAry[8] += 1
        elif alph == 'j':
            alphAry[9] += 1
        elif alph == 'k':
            alphAry[10] += 1
        elif alph == 'l':
            alphAry[11] += 1
        elif alph == 'm':
            alphAry[12] += 1
        elif alph == 'n':
            alphAry[13] += 1
        elif alph == 'o':
            alphAry[14] += 1
        elif alph == 'p':
            alphAry[15] += 1
        elif alph == 'q':
            alphAry[16] += 1
        elif alph == 'r':
            alphAry[17] += 1
        elif alph == 's':
            alphAry[18] += 1
        elif alph == 't':
            alphAry[19] += 1
        elif alph == 'u':
            alphAry[20] += 1
        elif alph == 'v':
            alphAry[21] += 1
        elif alph == 'w':
            alphAry[22] += 1
        elif alph == 'x':
            alphAry[23] += 1
        elif alph == 'y':
            alphAry[24] += 1
        elif alph == 'z':
            alphAry[25] += 1
    sAry.append(alphAry)

#print(sAry)

resultAry = [51] * 26
for s in sAry:
    for i in range(26):
        if s[i] < resultAry[i]:
            resultAry[i] = s[i]

#print(resultAry)

answer = ''
for i in range(26):
    for j in range(resultAry[i]):
        answer += alphabet[i]

print(answer)