# n 받기
n = int(input())


# 2차원 배열 받기
block = []
for i in range(n):
    block.append(list(map(int, input().split())))

    
# 폭탄 위치 받기
r, c = map(int, input().split())
r -= 1
c -= 1

# 폭탄 상하좌우 터지기 
# block의 r-1, c-1 위치의 값을 보고 상하좌우 몇개 터질지 고민 (위에서 r,c를 하나씩 다 줄여놓음)
bomb_num = block[r][c]
bomb_num -= 1 # 값보다 1개 적게 터져야 함

# -> row 방향, column 방향으로 다 -1로 바꾸기
# row방향 먼저 -1로 바꾸기
for dx in range(-bomb_num, bomb_num+1):
    if r+dx<n and r+dx>=0:
        block[r+dx][c] = -1
# col방향 -1로 바꾸기
for dy in range(-bomb_num, bomb_num+1):
    if c+dy<n and c+dy>=0:
        block[r][c+dy] = -1
    

# 한 column씩 temp로 바꿀거야 - 떨어뜨리고 나머지 0으로 정리한 다음 다시 block 새로 바꾸기 -> block 기둥의 맨 아래줄부터 보면서 값이 -1이 아니면 temp 마지막부터 넣어준다
# 각 열마다 리스트 만들어서 값 모으기 - col을 고정하고 row 를 움직이면서 찾아주자 찾고 앞에 모자란 길이만큼 0 채워주면 된다!!!!!
for col in range(0,n):
    temp = []
    for row in range(0,n):
        if block[row][col] != -1:
            temp.append(block[row][col])

    temp = [0]*(n-len(temp)) + temp #빈 칸 채워주기

    # 다시 해당 열에 할당
    for row in range(0,n):
        block[row][col] = temp[row]






for i in range(n):
    for j in range(n):
        print(block[i][j], end = " ")
    print()