def solver(n, x, a):
    segment = 1
    stack = []
    for i in a:
        if i == 1:
            continue
        if x % i != 0:
            continue
        if i in stack:
            segment += 1
            stack = [x//i]
            continue
        for j in range(len(stack)):
            if stack[j] % i == 0:
                stack.append(stack[j]//i)
        stack.append(x//i)


    print(segment)


def takeInputAndPutItInSolver():
    n, x = list(map(int, input().strip().split()))
    a =  list(map(int, input().strip().split()))
    solver(n, x, a)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()