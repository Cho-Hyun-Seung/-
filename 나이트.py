location = input()

answer = 0
alpha = ord(location[0]) - 96
num = int(location[1])

move_arr = [[2,1], [2,-1], [-2,1], [-2,-1], [1,2], [-1,2], [1,-2], [-1,-2]]

for a,b in move_arr:
    x_move = alpha + a
    y_move = num + b
    if 0 < x_move <= 8 and 0 < y_move <= 8:
        answer +=1
print(answer)