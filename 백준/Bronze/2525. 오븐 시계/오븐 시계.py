h, m = map(int, input().split())
min = int(input())
re_min = m + min
if re_min >= 60:
    if h + re_min // 60 < 24:
        print(h + re_min // 60, re_min % 60)
    else:
        print(h + re_min // 60 - 24, re_min % 60)
else:
    print(h, re_min)