"""
1. 모험가 N명 존재
2. 공포도가 X인 모험가는 X명 이상이 가야 모험 그룹 가능
"""

N = map(int, input().split(' '))
fear_arr = sorted(map(int, input().split(' ')), reverse=True)

max_fear = 0
party = 0
answer = 0

for member in fear_arr:
    # 파티장
    if max_fear == 0:
        max_fear = member
        party +=1
    # 모집 중
    elif party != max_fear:
        party +=1
    
    # 모집 완료
    if party == max_fear:
        max_fear = 0
        party = 0
        answer += 1
print(answer)