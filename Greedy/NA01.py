N = int(input())
scary = list(map(int, input().split()))
scary.sort()

num = 1 # 현재 만들어지고 있는 그룹의 공포도
count = 0 # 현재 만들어지고 있는 그룹의 인원수
result = 0

for i in scary:
    if i <= num: #다음 모험가의 공포도가 현재 그룹의 최대 공포도보다 낮을때(ex) 현재 그룹의 최대 공포도가 2인데 다음 모험가의 공포도가 2일때)
        count += 1 # 인원수 추가
        if count == i: #만약 인원이 다 차면 count를 다시 0으로
            result += 1
            count = 0
    else:
        num += 1 

print(result)