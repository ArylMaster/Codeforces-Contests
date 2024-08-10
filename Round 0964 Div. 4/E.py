import heapq
import math
def solver(l, r):
    heap = [i for i in range(l, r+1)]
    heapq.heapify(heap)

    count = 0
    while True:
        smallest = heapq.heappop(heap)
        small = heapq.heappop(heap)

        if smallest > 0 and small < 3:
            heapq.heappush(heap, 0)
            heapq.heappush(heap, 3*smallest)
            count += 1

        elif smallest == 0:
            heapq.heappush(heap, small)
            break

        else:
            heapq.heappush(heap, smallest//3)
            heapq.heappush(heap, small*3)
            count += 1

    for num in heap:
        if num != 0:
            while num != 0:
                num //= 3
                count += 1

    print(count)
    return




    print(count)
    # while True:
    #     smallest = heapq.heappop(heap)
    #     small = heapq.heappop(heap)
    #     if smallest == small == 0 and not heap:
    #         break
    #     elif smallest == small == 0:
    #         heapq.heappush(heap, 0)
    #         continue
    #     if smallest == 0 or small < 3:
    #         heapq.heappush(heap, 0)
    #     else:
    #         smallest //= 3
    #         small *= 3
    #         heapq.heappush(heap, small)
    #         heapq.heappush(heap, smallest)
    #     count += 1

    # print(count)
        

    
    pass

def takeInputAndPutItInSolver():
    # int(input())
    l, r = list(map(int, input().strip().split()))
    solver(l, r)

def main():
    testCases = int(input())
    for _ in range(testCases):
        takeInputAndPutItInSolver()
             
if __name__ == "__main__":
    main()