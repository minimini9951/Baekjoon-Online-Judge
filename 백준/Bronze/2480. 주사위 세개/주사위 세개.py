n1, n2, n3 = map(int, input().split())
num = [n1, n2, n3]
num.sort(reverse=True)
if n1 == n2 == n3:
    print(10000 + n1 * 1000)
elif n1 != n2 & n2 != n3 & n3 != n1:
    print(num[0] * 100)
elif n1 == n2 & n2 != n3:
    print(1000 + n1 * 100)
elif n2 == n3:
    print(1000 + n2 * 100)
elif n1 == n3:
    print(1000 + n3 * 100)