number = input()

list_number = []
for i in range(len(number)):
    list_number.append(number[i])

list_number.sort(reverse=True)
print(''.join(list_number))