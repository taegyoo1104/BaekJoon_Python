n = int(input())
if n % 10 != 0:
    print(-1)
else:
    a = n // 300
    b = (n % 300) // 60
    c = ((n % 300) % 60) // 10
    print(a, b, c)

'''
n = int(input())

A = 300
B = 60
C = 10
A_Result, B_Result, C_Result = 0, 0, 0

while n > 0:
    if n % C != 0:
        print(-1)
        break;

    if n // A != 0:
        A_Result = n // A
        n = n % A
    if n // B != 0:
        B_Result = n // B
        n = n % B
    if n // C != 0:
        C_Result = n // C
        n = n % C

if A_Result or B_Result or C_Result != 0:
    print(A_Result, B_Result, C_Result)
'''