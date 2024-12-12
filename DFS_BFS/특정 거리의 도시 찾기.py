"""
눈물 뚝뚝 코테준비  ㅜㅜ

- 도시 개수 n
- 도로 개수 m
- 거리 정보 k
- 출발 도시 번호 x

- 최단 거리가 정확히 k 인 도시 정보 출력
"""
from collections import deque

n, m, k, x = map(int,input().split(' '))

# 0 번은 출발 도시 1번은 도착 도시
road = [list(int,input().split(' ')) for _ in range(m)]


def bfs(start):
    queue = deque()
    # 시작도시
    queue.append(start)

