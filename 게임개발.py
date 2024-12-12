"""
1. 현재 위치에서 현재 방향 기준으로 왼쪽 방ㅇ향부터 차례대로 갈 곳을 정함
2. 캐릭터 왼쪽에 가보지 않는 칸이 존재한다면 왼쪽 회전후 한칸 전진
    2.1. 존재하지 않는다면 회전만
    
3. 네방향 모두 가본 칸이거나 바다인 경우 바라보는 방향 유지한채 한칸 뒤로 감
    3.1. 이때, 뒤가 바다면 움직임 멈춤

"""

n, m = map(int, input().split(' '))
now_x, now_y, face = map(int, input().split(' '))

answer = 1
face_count = 0

# 북(0), 동(1), 남(2), 서(3) 방향 정의
face_arr = [(-1, 0), (0, 1), (1, 0), (0, -1)]
maps = []

# 맵 입력받기
for i in range(n):
    maps.append(list(map(int, input().split(' '))))

# 현재 위치 방문 처리
maps[now_x][now_y] = 1

while True:
    # 왼쪽 방향으로 회전
    face = (face - 1) % 4
    check_x = now_x + face_arr[face][0]
    check_y = now_y + face_arr[face][1]

    # 맵 범위 초과 체크 및 육지 확인
    if 0 <= check_x < n and 0 <= check_y < m and maps[check_x][check_y] == 0:
        maps[check_x][check_y] = 1  # 방문 처리
        now_x, now_y = check_x, check_y
        answer += 1
        face_count = 0
        continue
    else:
        face_count += 1

    # 네 방향 모두 이동 불가능한 경우
    if face_count == 4:
        check_x = now_x - face_arr[face][0]
        check_y = now_y - face_arr[face][1]
        
        # 뒤로 갈 수 없는 경우 종료
        if 0 <check_x <= n or 0 <check_x <= m  or maps[check_x][check_y] == 1:
            break
        now_x, now_y = check_x, check_y
        face_count = 0

print(answer)
