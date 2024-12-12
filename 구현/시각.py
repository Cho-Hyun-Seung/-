target_hour = int(input())

answer = 0

for i in range(target_hour +1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i)+str(j)+str(k):
                answer +=1
print(answer)
