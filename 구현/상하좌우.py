
answer = [1,1]
n = int(input())
command = input().split(' ')
command_dict = {"L":0, "R":1, "U":2, "D":3}

dy = [-1 ,1 ,0 ,0]
dx = [0, 0, -1, 1]


for move in command:
    y_check = answer[0]+ dx[command_dict[move]]
    x_check = answer[1]+ dy[command_dict[move]]
    if 0< x_check <= n and 0< y_check <= n:
        answer = [y_check, x_check]

answer = ' '.join(map(str, answer))
print(answer)