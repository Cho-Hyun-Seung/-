"""
무게가 같은 공이 있을 수 있지만 서로 다른 공으로 간주
"""

answer = 0
n, m = map(int,input().split(' '))
balls = list(map(int,input().split(' ')))

for idx, ball in enumerate(balls[:-1]):
    for second_ball in balls[idx:]:
        if ball != second_ball:
            answer +=1
        
print(answer)


           