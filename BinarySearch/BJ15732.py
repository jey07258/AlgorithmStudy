import sys

N, K, D = map(int, sys.stdin.readline().split())
rules = []
for _ in range(K):
    rules.append(list(map(int, sys.stdin.readline().split())))

start = 1
end = N

while start <= end:
    mid = (start+end)//2
    count = 0
    for rule_start, rule_end, rule_step in rules:
        if mid < rule_start:
            continue
        if mid >= rule_end:
            count += (rule_end - rule_start)//rule_step + 1
        else:
            count += (mid - rule_start)//rule_step + 1

    if count >= D:
        result = mid
        end = mid - 1
    else:
        start = mid + 1
        
print(result)