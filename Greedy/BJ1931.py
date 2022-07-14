N = int(input())
time_list = []

for i in range(N):
    tmp = list(map(int, input().split()))
    time_list.append(tmp)

#시간 목록을 오름차순으로 정렬
time_list = sorted(time_list, key = lambda x : (x[0], x[1]))
temp = time_list[0]

count = 0
keep = temp #비교 기준이 될 temp와 진행되는 회의를 담아두는 keep의 시작값은 가장 처음 시작하는 회의 정보로 해둔다

for i in range(N):
    if temp == time_list[i]: #temp의 회의가 다음 회의와 일치할때
        #(2 2) (7 7)처럼 시작하는 시간과 끝나는 시간이 같은 회의거나, temp로 정했던 time_list의 첫번째 회의인 경우에만 count +1 해준다
        if time_list[i][0] == time_list[i][1] or i == 0:
            count += 1
        continue #그렇지 않고 (1 2) (1 2)처럼 시작과 끝이 일치만 하는 회의일경우에는 넘긴다
    
    #temp의 끝나는 시간이 time_list의 시작과 끝보다 클 경우, 즉 temp=(1 7) time_list=(3 4) 이런 경우
    if temp[1] > time_list[i][1] and temp[1] > time_list[i][0]:
        #temp를 현재 time_list로 교체하고, count를 -1 해준다
        temp = time_list[i]
        count -= 1

    #temp의 끝나는 시간이 time_list의 시작과 끝보다 작거나 같을 경우, 즉 temp=(1 3) time_list=(3 5) or (4 5) 이런 경우
    if temp[1] <= time_list[i][1] and temp[1] <= time_list[i][0]:
        #temp를 현재 time_list로 교체한다
        temp = time_list[i]

    #temp가 keep과 다르면 count를 +1 해주고 keep을 현재 temp로 교체한다
    if keep != temp:
        count += 1
        keep = temp

print(count)