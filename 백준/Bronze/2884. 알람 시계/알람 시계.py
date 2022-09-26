x, y = map(int, input().split())
if y >= 45:
    print(x, y - 45)
elif x > 0 and y < 45:
    print(x - 1, y + 15)
elif x == 0 and y < 45:
    print(23, y + 15)