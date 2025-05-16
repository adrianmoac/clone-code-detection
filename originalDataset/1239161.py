n = int(input())
i = input()

i = i.split()
for item in range(len(i)):
    i[item] = int(i[item])

totn = 0
totp = 0

countp = 0
countn = 0

for x in range(len(i)):
    totp += i[x]
    totn += i[x]
    
    if x == 0:
        if totp == 0:   
            totn = -1
            countn = 1

            totp = 1
            countp = 1
            
        elif totp < 0:
            countp = abs(totp) + 1
            totp = 1

        elif totp > 0:
            countn = abs(totn) + 1
            totn = -1

    elif x %2 == 1:
        if totn == 0:
            countn += 1
            totn = 1
        elif totn < 0:
            countn += abs(totn) + 1
            totn = 1

        if totp == 0:
            countp += 1
            totp = -1
        elif totp > 0:
            countp += abs(totp) + 1
            totp = -1

    elif x %2 == 0:
        if totn == 0:
            countn += 1
            totn = -1
        elif totn > 0:
            countn += abs(totn) + 1
            totn = -1

        if totp == 0:
            countp += 1
            totp = 1
        elif totp < 0:
            countp += abs(totp) + 1
            totp = 1
    '''print('totn', totn)
    print('countn', countn)
    print('totp', totp)
    print('countp', countp) '''   
count = min(countn, countp)
print(count)
