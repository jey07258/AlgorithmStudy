S = list(input())

count = 1

for i in range(len(S)-1):
    if S[i] != S[i+1]:
        count += 1

    if count % 2 == 0:
        result = count // 2
    else:
        result = (count -1) // 2

print(result)