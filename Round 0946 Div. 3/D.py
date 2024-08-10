def finder(n, s):
    if n%2 == 1:
        return "NO"
    ls = []
    a = b = c = d = 0
    for i in s:
        if i == 'N':
            a += 1
        elif i == 'S':
            b += 1
        elif i == 'E':
            c += 1
        else:
            d += 1
        ls.append(i)
    v = a-b
    h = c-d
    if v%2 == 1 or h%2 == 1:
        return "NO"
    dest = [h//2, v//2]
    locR = [0, 0]
    locH = [0, 0]
    solution = ''
    if dest[0] > 0:
        hIsP = True
    elif dest[0] < 0:
        hIsP = False
    else:
        hIsP = None
    if dest[1] > 0:
        vIsP = True
    elif dest[1] < 0:
        vIsP = False
    else:
        vIsP = None
    exception = False
    for i in range(n):
        if vIsP == True:
            if ls[i] == 'N':
                if locR[1] < dest[1]:
                    ls[i] = 'R'
                    locR[1] += 1
                else:
                    ls[i] = 'H'
                    locH[1] += 1
            elif ls[i] == 'S':
                ls[i] = 'H'
                locH[1] -= 1

        elif vIsP == False:
            if ls[i] == 'S':
                if locR[1] > dest[1]:
                    ls[i] = 'R'
                    locR[1] -= 1
                else:
                    ls[i] = 'H'
                    locH[1] -= 1
            elif ls[i] == 'N':
                ls[i] = 'H'
                locH[1] += 1
        else:
            if hIsP == None:
                exception = True
            else:
                if ls[i] == 'N':
                    ls[i] = 'H'
                    locH[1] += 1
                elif ls[i] == 'S':
                    ls[i] = 'H'
                    locH[1] -= 1

    for i in range(n):
        if hIsP == True:
            if ls[i] == 'E':
                if locR[0] < dest[0]:
                    ls[i] = 'R'
                    locR[0] += 1
                else:
                    ls[i] = 'H'
                    locH[0] += 1
            elif ls[i] == 'W':
                ls[i] = 'H'
                locH[0] -= 1

        elif hIsP == False:
            if ls[i] == 'W':
                if locR[0] > dest[0]:
                    ls[i] = 'R'
                    locR[0] -= 1
                else:
                    ls[i] = 'H'
                    locH[0] -= 1
            elif ls[i] == 'E':
                ls[i] = 'H'
                locH[0] += 1
            else:
                if not exception:
                    if ls[i] == 'E':
                        ls[i] = 'H'
                        locH[0] += 1
                    elif ls[i] == 'W':
                        ls[i] = 'H'
                        locH[0] -= 1

    if not exception:
        if locH == locR == dest:
            return ''.join(ls)
    else:
        pass






    


t = int(input())
output = []
for i in range(t):
    n = int(input())
    s = input()
    output.append(finder(n, s))

for i in output:
    print(i)