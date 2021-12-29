T = int(input())
data = []
for i in range(T):
    data.append(int(input()))

def solution(number):
    if number == 1:
        return 1
    elif number == 2:
        return 2
    elif number == 3:
        return 4

    return solution(number-1) + solution(number-2) + solution(number-3)

result = []
for i in data:
    result.append(solution(i))

for i in result:
    print(i)