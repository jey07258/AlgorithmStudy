#최솟값이 목적 -> 더할 수 있는 값은 다 더해서 한꺼번에 빼는 방식으로 구해야 함
expression = list(input().split('-'))
#마이너스 기호를 기준으로 split
# -> 입력이 '5-5+4-7+6+9-1-2+6'이면 결과물: ['5', '5+4', '7+6+9', '1', '2+6']
result = 0

if len(expression) == 1: #즉, 마이너스 기호 없이 플러스만 있으면
    temp = expression[0].split('+')
    for i in range(len(temp)):
        result += int(temp[i]) #숫자를 다 더한 값이 result
else:
    for k in range(len(expression)):
        if '+' in expression[k]: #사이에 +가 있어서 더할 수 있는 부분이면 더해준다
            tmp = 0
            temp = expression[k].split('+')
            for i in range(len(temp)):
                tmp += int(temp[i])
            if(k == 0): #만약 빼기의 기준이 될 첫번째 숫자라면 값을 따로 기억해둔다
                result = tmp
                continue
            else:
                result -= tmp
        else: # + 없이 숫자만 있다면 바로 빼준다
            if(k == 0): #만약 빼기의 기준이 될 첫번째 숫자라면 값을 따로 기억해둔다
                result = int(expression[k])
                continue
            else:
                result -= int(expression[k])

print(result) 
