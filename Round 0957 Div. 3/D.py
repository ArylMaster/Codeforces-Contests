def solver(n, m, k, a):
    if m > n:
        print("YES")
        return
    
    trav = 0
    waterFound = False
    logFound = False
    while True:
        if not waterFound:
            if trav + m > n:
                print("YES")
                return
            logFound = False
            for i in range(trav+m, trav, -1):
                if a[i-1] == 'L':
                    trav = i
                    logFound = True
                    break
            if logFound:
                continue
            else:
                for i in range(trav+m, trav, -1):
                    if a[i-1] == 'W':
                        trav = i
                        waterFound = True
                        break

                if not waterFound:
                    print("NO")
                    return
        else:
            trav += 1
            k -= 1
            if k < 0:
                print("NO")
                return
            if trav == n+1:
                print("YES")
                return
            if a[trav-1] == 'C':
                print("NO")
                return
            if a[trav-1] == 'L':
                waterFound = False
                logFound = True

    pass

def takeInputAndPutItInSolver():
    # int(input())
    n, m, k = list(map(int, input().strip().split()))
    a = input()
    solver(n, m, k, a)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()