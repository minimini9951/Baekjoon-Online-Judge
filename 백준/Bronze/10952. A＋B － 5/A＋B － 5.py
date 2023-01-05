import sys

while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == 0 & b == 0:
        break
    else:
        print(a+b)