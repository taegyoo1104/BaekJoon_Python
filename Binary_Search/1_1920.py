'''
수 찾기 https://www.acmicpc.net/problem/1920

문제
N개의 정수 A[1], A[2], …, A[N]이 주어져 있을 때, 이 안에 X라는 정수가 존재하는지 알아내는 프로그램을 작성하시오.

입력
첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다.
다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다.
다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다.
다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다.
모든 정수의 범위는 -2^31 보다 크거나 같고 2^31보다 작다.

출력
M개의 줄에 답을 출력한다. 존재하면 1을, 존재하지 않으면 0을 출력한다.
'''
n1 = int(input())
data1 = list(map(int, input().split()))
data1.sort()

n2 = int(input())
data2 = list(map(int, input().split()))


def search(data, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if data[mid] == target:
        return True
    elif data[mid] > target:
        return search(data, target, start, mid-1)
    else:
        return search(data, target, mid + 1, end)
    return False

for i in data2:
    if search(data1, i, 0, n1-1):
        print(1)
    else:
        print(0)