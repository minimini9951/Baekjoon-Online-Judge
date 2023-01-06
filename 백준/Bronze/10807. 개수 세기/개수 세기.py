import sys

n = int(sys.stdin.readline())
n_list = list(map(int, sys.stdin.readline().split()))
find = int(sys.stdin.readline())

print(n_list.count(find))