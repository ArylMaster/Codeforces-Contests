from sys import stdout

def solver():
    l, r = 2, 999

    while l < r:
        mid = (l+r)//2
        x = (l + mid)//2
        y = (mid + r)//2

        print(f"? {x} {y}")
        stdout.flush()
        area = int(input())
        if area == x*y:
            l = y + 1

        elif area == (x+1)*(y+1):
            r = x

        else:
            l = x + 1
            r = y

    print(f"! {l}")


for _ in range(int(input())):
    solver()