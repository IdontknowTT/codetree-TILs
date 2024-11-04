# n 받기
n = int(input())

# block 배열 받기
block = []
for _ in range(n):
    block.append(int(input()))

# e1, s1 받
e1, s1 = map(int, input().split())
# e2, s2 받
e2, s2 = map(int, input().split())


def hamsu(e, s, block):
    # 첫번째 블럭 구간 빼기
    for i in range(e-1, s): #e1-1~s1-1 까지 block을 -1로 바꾼다
        block[i] = -1
    # temp배열에 넣어준다 
    temp = []
    for i in range(len(block)):
        if block[i] != -1:
            temp.append(block[i])
            
    return temp


# 첫번째 블럭 구간 빼기
block1 = hamsu(e1, s1, block)

# 두번째 블럭 구간 빼기
block2 = hamsu(e2, s2, block1)
    
# 결과 출력
if len(block2) == 0:
    print(0)
else:
    print(len(block2))
    for i in block2:
        print(i)