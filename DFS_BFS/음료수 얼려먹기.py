"""
- 구멍이 뚫린 부분 0
- 구멍이 막힌 부분 1
- 상하좌우 붙으면 연결
- 한번에 만들어지는 아이스크림 개수는?
"""

n, m = map(int, input().split(' '))

graph = []

for _ in range(n):
    graph.append(list(map(int,input())))

def dfs(x,y):
    if x <0 or x >=n or y < 0 or y >=m:
        return False
    
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x-1,y)
        dfs(x+1,y)
        dfs(x,y-1)
        dfs(x,y+1)
        return True
    return False
        
    
result = 0
    
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True:
            result +=1
print(result)