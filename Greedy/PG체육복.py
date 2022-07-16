def solution(n, lost, reserve):
    lost.sort()
    lost_copy = lost.copy()
    answer = n - len(lost)

    #for문과 remove를 같이 써야할땐 index error가 나기 쉬우니 중복 리스트를 만들어 써주자
    for i in lost_copy:
        if i in reserve:
            reserve.remove(i)
            lost.remove(i)
            answer += 1

    for i in range(len(lost)):
        if lost[i]-1 in reserve:
            reserve.remove(lost[i]-1)
            answer += 1
        elif lost[i]+1 in reserve:
            reserve.remove(lost[i]+1)
            answer += 1
    return answer