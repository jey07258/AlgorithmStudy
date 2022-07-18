S = list(map(int, input()))

while 0 in S:
    S.remove(0) #0인경우: 자동으로 앞 숫자에 + 한 것으로 취급

i = 1
while i < len(S): #1인경우: 앞 숫자에 + 해준다
    if S[i] == 1:
        S[i-1] += 1
        S.pop(i)
    else:
        i += 1

result = 1
for i in range(len(S)): #그외 2~9의 숫자인 경우 곱한다
    print(S[i])
    result *= S[i]

print(result)