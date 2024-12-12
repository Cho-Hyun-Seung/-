"""
동전을 이용해 만들 수 없는 양의 정수 금액 중 최솟값을 구하는 프로그램
"""
answer = 1
n = int(input())
coin = sorted(list(map(int,input().split())))

for i in coin:
  if i > answer:
    break
  else:
    answer+=i
 
print(answer)