queue = []

def enqueue(num):
    queue.append(num)
    return queue

def dequeue():
    if queue:  # 큐가 비어있지 않을 때만 처리
        queue.pop(0)  # 첫 번째 요소를 제거
    return queue

while True:
    try:
        a = int(input("입력 >> "))  # 사용자 입력을 받는 부분
        if a == 1:
            num = int(input("큐에 추가할 숫자를 입력하세요: "))  # 추가할 숫자를 입력
            enqueue(num)
        elif a == 2:
            dequeue()
        elif a == 3:
            break
        else:
            print("1, 2, 3 중 하나를 입력하세요.")
    except ValueError:
        print("유효한 숫자를 입력하세요.")
    
    print("현재 큐:", queue)
