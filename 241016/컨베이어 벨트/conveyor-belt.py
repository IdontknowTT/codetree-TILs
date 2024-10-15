from collections import deque

n, t = map(int, input().split()) #n,t 받기
up = list(map(int, input().split())) #위의 리스트 받기
down = list(map(int, input().split())) #아래 리스트 받기

#둘다 큐로 바꿔준다
up = deque(up)
down = deque(down)


#돌린다
for _ in range(t):
    temp1 = up.pop()
    temp2 = down.popleft()

    up.insert(0,temp2)
    down.append(temp1)


print(up)
print(down)