from collections import deque

# 입력
n,m = map(int, input().split())

# 뱀 없어야 1
grid = [list(map(int, input().split())) for _ in range(n)] #n개의 행 (n번째행, m번째열) 이라고 생각


def can_go(x,y):
    if x<0 or y<0 or x>=n or y>=m:
        return False
    if visited[x][y] == True or grid[x][y] == 0:
        return False
    return True

def bfs():

    while q:
        # 큐에서 하나 꺼내
        (x,y) = q.popleft()
        # 그 꺼낸 자리에서 상하좌우 이동하면서 갈 수 있나 볼거야
        dxs, dys = [1,0,-1,0], [0,1,0,-1]

        for dx, dy in zip(dxs, dys):

            new_x = x+dx
            new_y = y+dy
            # 갈수 있다면 방문 표시하고 q에 append 하기
            if can_go(new_x, new_y):
                visited[new_x][new_y] = True
                q.append((new_x, new_y))


# for grid i,j 로 받아서 이 노드 갈? 방문? -> bfs
visited = [[False for _ in range(m)] for _ in range(n)]
q = deque()
q.append((0,0)) # 큐에 넣어
visited[0][0] = True
bfs() # bfs 호출해



if visited[n-1][m-1]:
    print(1)
else:
    print(0)