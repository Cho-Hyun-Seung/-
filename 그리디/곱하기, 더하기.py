"""
1. 왼쪽부터 순서대로 이뤄짐 곱하기 더하기 순서 없음
2. 
"""

num_arr = map(int,list(input()))
answer = 0

for num in num_arr:
    # 첫 숫자 처리
    if answer == 0:
        answer += num
    # num이 1 or 0인 경우 더하기
    elif num == 0 or num == 1:
        answer += num
    else:
        answer *= num
print(answer)