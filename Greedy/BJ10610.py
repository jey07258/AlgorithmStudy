N = list(map(int, input()))

result = ''

#3의 배수이면서 끝자리가 0인 수 = 30의 배수
if 0 in N:
    if sum(N) % 3 == 0:
        N.sort(reverse=True)
        for i in range(len(N)):
            result += str(N[i])
        print(result)
    else:
        print('-1')
else:
    print('-1')