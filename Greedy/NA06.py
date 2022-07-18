#정확성 테스트는 통과하나, 효율성 테스트에서는 시간 초과 발생

def solution(food_times, k):
    answer = 0
    n = len(food_times)
    j = 0
    for key in range(k+1):
        if food_times[j%n] == 0:
            if sum(food_times) == 0:
                answer = -1
                return answer
            while food_times[j%n] == 0:
                j += 1
        if key == k:
            answer = j%n+1
            break
        food_times[j%n] -= 1
        j += 1
        
    return answer