""" 나무 자르기 https://www.acmicpc.net/problem/2805 """
n, m = map(int, input().split())
trees = list(map(int, input().split()))

start = 0
end = max(trees)

result = 0
while start <= end:
    total_length = 0
    mid = (start + end) // 2
    for tree in trees:
        if mid < tree:
            total_length = total_length + (tree - mid)
    if total_length < m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1

print(result)