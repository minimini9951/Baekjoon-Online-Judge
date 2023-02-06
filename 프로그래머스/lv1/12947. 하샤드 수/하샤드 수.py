def solution(x): # x를 받아옴
    answer = True
    if x >= 1 and x <= 10000:
        p = 0
        for i in range(len(str(x))):
            p += int(str(x)[i])
        if x % p != 0:
            answer = False
        return answer