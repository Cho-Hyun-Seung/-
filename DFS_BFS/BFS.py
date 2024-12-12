from collections import deque

graph = [[], [2,3,8], [1,7], [1,4,5], [3,5],[3,4], [7], [2,6,8], [1,7]]

visited = [False]*9


def bfs(graph, v, visited):
    # 큐 생성
    queue = deque([v])
    # v 번 노드 방문 처리
    visited[v] = True
    
    while queue:
        i = queue.popleft()
        print(i, end=' ')
        
        for j in graph[i]:
            # 방문 한 노드가 아니라면
            if not visited[j]:
                # 큐에 삽입
                queue.append(j)
                visited[j] = True
                
bfs(graph,1,visited)
                
                
    
    
    
    
    