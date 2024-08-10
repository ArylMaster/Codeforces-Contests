def decoder(n, s):
    Map = {}
    for i in s:
            Map[i] = None
    MapOrdered = []
    alph = 'abcdefghijklmnopqrstuvwxyz'
    for i in alph:
        if i in Map:
            MapOrdered.append(i)
    l = len(Map)
    lptr, rptr = 0, l-1
    while lptr <= rptr:
        Map[MapOrdered[lptr]], Map[MapOrdered[rptr]] = MapOrdered[rptr], MapOrdered[lptr]
        lptr += 1
        rptr -= 1
    newS = ""
    for i in s:
        newS += Map[i]
    return newS

t = int(input())
output = []
for i in range(t):
    n = int(input())
    s = input()
    output.append(decoder(n, s))

for i in output:
    print(i)
