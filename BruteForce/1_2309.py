from itertools import combinations

dwarf = []
for i in range(9):
    dwarf.append(int(input()))

dwarf_comb = combinations(dwarf, 7)

for i in dwarf_comb:
    list_dwarf = list(i)
    if sum(list_dwarf) == 100:
        list_dwarf.sort()
        for x in range(7):
            print(list_dwarf[x])
        break
