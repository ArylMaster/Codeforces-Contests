def solver(n, k, a):
    lenA = len(a)
    if lenA == 1:
        print(0)
        return
    a.sort(reverse=True)
    moves = 0
    for i in range(1, lenA):
        moves += 2*a[i] - 1
    print(moves)



def takeInputAndPutItInSolver():
    # int(input())
    n, k = list(map(int, input().strip().split()))
    a = list(map(int, input().strip().split()))
    solver(n, k, a)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()