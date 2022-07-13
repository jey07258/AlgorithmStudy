N, K = map(int, input().split())
result = 0
coin_value = []

for _ in range(N):
    coin_value.append(int(input()))

for coin in coin_value[::-1]:
    if K==0: #해당 조건을 안붙여서 ZeroDivisionError를 냈음... 마지막까지 확인을 잘 하자
        break
    result += K // coin
    K %= coin  

print(result) 
