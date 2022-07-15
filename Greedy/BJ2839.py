N = int(input())

if N % 5 == 0:
    count = N // 5
elif N % 5 == 1:
    count = (N - 6) // 5 + 2
elif N % 5 == 2:
    if N == 7:
        count = -1
    else:
        count = (N - 12) // 5 + 4
elif N % 5 == 3:
    count = N//5 + 1
elif N % 5 == 4:
    if N == 4:
        count = -1
    else:
        count = (N - 9) // 5 + 3

print(count)