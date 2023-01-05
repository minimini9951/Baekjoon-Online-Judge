tot = int(input())
n = int(input())
x = 0

for i in range(n):
    a, b = map(int, input().split())
    x += a * b

if x == tot:
    print('Yes')
elif x != tot:
    print('No')