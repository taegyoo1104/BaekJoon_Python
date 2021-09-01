""" 문자열 폭발 """

s = input()
bomb = input()

stack = []
for i in range(len(s)):
    stack.append(s[i])
    if s[i] == bomb[-1] and ''.join(stack[-len(bomb):]) == ''.join(bomb):
        for j in range(len(bomb)):
            del stack[-1]

result = ''.join(stack)
if result == '':
    print('FRULA')
else:
    print(result)