def finder(ls):
    p1, p2, p3 = ls[0], ls[1], ls[2]
    if (p1 + p2 + p3) % 2 == 1:
        return -1
    draws = 0
    for i in range(p1+1):
        t1, t2, t3 = p1, p2, p3
        temp = 0
        temp += i
        t1 -= i
        t2 -= i
        temp += t1
        t3 -= t1
        temp += min(t2, t3)
        if temp > draws:
            draws = temp

    return draws

        





output = []
t = int(input())

for i in range(t):
    output.append(finder(list(map(int, input().split()))))

for i in output:
    print(i)