def solver(n):
    final = []
    for a in range(1, 10001):
        fakeTotal = str(n)*a
        actualTotal = n*a
        l = len(fakeTotal)
        bMax = min(10000, a*n)
        for b in range(max(1, l-7), min(l, bMax)):
            if actualTotal - b == int(fakeTotal[:l-b]):
                final.append((a,b))



    print(len(final))
    for i in final:
        print(i[0], i[1])

    
    
    
    pass

def takeInputAndPutItInSolver():
    n = int(input())
    # list(map(int, input().strip().split()))
    solver(n)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()