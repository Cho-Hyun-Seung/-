"""
- 낮은 애부터 먼저 증식
- 이미 있는 부분에 증식 불가능

- x,y 위치에 s 초 후 바이런스는?
"""
from collections import deque

n , k = map(int,input().split(' '))

dx = [-1,1,0,0]
dy = [0,0,-1,1]

flask = []

for _ in range(n):
    flask.append(list(map(int,input().split(' '))))
    
s, _x, _y = map(int,input().split(' '))

# 바이러스 위치 찾기
def find_virus():
    virus = []
    for i in range(n):
        for j in range(n):
            if flask[i][j] != 0:
                virus.append((i,j))
    return virus
    

def bfs():
    time = 0
    # 시간 되기 전까지
    while time < s:
        virus = find_virus()
        for x,y in virus:
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                
                if 0 <= nx < n and 0 <= ny < n and flask[nx][ny] ==0:
                    flask[nx][ny] = flask[x][y]
        time +=1
    return flask[_x-1][_y-1]

print(bfs())

                 
        
    
    


            