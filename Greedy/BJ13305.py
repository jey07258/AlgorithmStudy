N = int(input())
road = list(map(int, input().split()))
price = list(map(int, input().split()))
result = 0
i = 1

#초기값 설정하기 / 처음에는 기름이 없으므로 무조건 첫 주유소에서 첫 도로만큼은 채워야함
min_price = price[0]
result += min_price * road[0]

while (i<len(road)):
    if price[i] <= min_price: #다음 주유소의 가격이 현재 최소값보다 저렴하면 주유소 교체
        min_price = price[i]
    result += min_price * road[i]
    i += 1

print(result)