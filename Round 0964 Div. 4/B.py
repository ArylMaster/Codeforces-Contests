def solver(arr):
    a1, a2, b1, b2 = arr
    count = 0
    if a1 > b1 and a2 > b2:
        count += 2
    if a1 > b2 and a2 > b1:
        count += 2
    if a1 > b1 and a2 == b2:
        count += 2
    if a1 > b2 and a2 == b1:
        count += 2
    if a2 > b2 and a1 == b1:
        count += 2
    if a2 > b1 and a1 == b2:
        count += 2
    print(count)


def takeInputAndPutItInSolver():
    # int(input())
    arr = list(map(int, input().strip().split()))
    solver(arr)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()