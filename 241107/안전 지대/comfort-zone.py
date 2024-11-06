# 입력 받
n,m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)] # n*m (세로로 n개)


# 일단 원본 격자 하나 복사해서 copy 격자의 K 이하는 다 0으로 만들고 초과는 1로 만들기
def make_grid(grid, k):
    grid_copy = grid
    for i in range(n):
        for j in range(m):
            if grid_copy[i][j] <= k:
                grid_copy[i][j] = 0
            else:
                grid_copy[i][j] = 1
    return grid_copy



# dfs 안에서는 그 영역 잡은 애들은 visited
def dfs(i,j):

    # 상하좌우 다 탐색
    dxs, dys = [1,0,-1,0], [0,1,0,-1]
    for dx, dy in zip(dxs, dys):
        new_x = i+dxs
        new_y = j+dys

        if can_go(new_x, new_y):
            visited[new_x][new_y] = True    
            dfs(new_x, new_y)

    


# k를 1~100번 돌려(각 집이 1이상 100이하) 
# -> 이거 복잡도 괜찮나? (아니면 네모 안에 있는 숫자 set해서 하는 방법도 -> 아 안되나)
visited = [[False *m]for _ in range(n)]
count = 0

for k in range(K):
    # 일단 원본 격자 하나 복사해서 copy 격자의 K 이하는 다 0으로 만들고 초과는 1로 만들기
    grid_copy = make_grid(grid, k) #함수 호출해서 grid_copy를 만들어오기


    # for 격자 하나하나 다 보면서 
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]: # 안전지대라면, 방문 안했다면
                dfs(i,j) # # 그리고 dfs 들어가기
                count += 1





print(count)