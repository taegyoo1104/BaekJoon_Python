S = input()
list_s = []

for i in range(len(S)):
    list_s.append(S[i:len(S) + 1])

list_s.sort()
for i in range(len(list_s)):
    print(list_s[i])