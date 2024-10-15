n = int(input())
block = []

#1. 일단 받아서 append를 해야돼 - 근데 append하고 reverse해서 맨 아래칸이 맨 왼쪽 가도록
for _ in range(n):
    block.append(int(input()))
block = block[::-1] #뒤집

s1, e1 = map(int, input().split())
s2, e2 = map(int, input().split())



#2. s1, e1 받아서 다 뺀다
for i in range(s1, e1+1,1):
    block[i] = False
#3. temp에 false가 아니라면 채워넣어 -> 다시 block으로 주기
temp = []
for b in block:
    if b != False:
        temp.append(b)
block = temp


#3. s2, e2 받아서 다 뺀다
for i in range(s2, e2+1,1):
    block[i] = False
#3. temp에 false가 아니라면 채워넣어 -> 다시 block으로 주기
temp = []
for b in block:
    if b != False:
        temp.append(b)
block = temp




# 결과----------------
print(len(block))
block = block[::-1]
for b in block:
    print(b)