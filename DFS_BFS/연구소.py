"""
- 0 : 빈칸
- 1 : 벽
- 2 : 바이러스

- 벽은 꼭 3개 세워야함
"""
from collections import deque
from itertools import combinations
from copy import deepcopy

n,m = map(int, input().split(' '))

graph = [list(map(int,input().split(' '))) for _ in range(n)]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

empty_space = []
answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            empty_space.append((i, j))

empty_comb = list(combinations(empty_space,3))

def bfs(graph):
    
    queue = deque()
    count = 0
    
    for i in range(n):
        for j in range(m):
            # 바이러스 구역 입력
            if graph[i][j] == 2:
                queue.append((i,j))
            
    
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] == 0:
                graph[nx][ny] = 2
                queue.append((nx, ny))
    
    return sum(row.count(0) for row in graph)
            
            

for comb in combinations(empty_space, 3):
    copy_graph = deepcopy(graph)
    for x, y in comb:
        copy_graph[x][y] = 1
    safe_zone = bfs(copy_graph)
    answer = max(answer, safe_zone)
    
print(answer)
        