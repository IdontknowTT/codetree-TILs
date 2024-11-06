import copy

# 입력 받기
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)] # n * m 격자

# 원본 격자 복사 후 k 이하 0, 초과 1로 변환
def make_grid(grid, k):
    grid_copy = copy.deepcopy(grid)  # 깊은 복사 사용
    for i in range(n):
        for j in range(m):
            if grid_copy[i][j] <= k:
                grid_copy[i][j] = 0
            else:
                grid_copy[i][j] = 1
    return grid_copy

# 이동 가능한지 확인하는 함수
def can_go(x, y):
    if x < 0 or y < 0 or x >= n or y >= m:  # 범위 확인
        return False
    if visited[x][y]:  # 이미 방문했다면
        return False
    return True

# DFS 함수
def dfs(i, j):
    visited[i][j] = True  # 방문 체크
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        new_x, new_y = i + dx, j + dy
        if can_go(new_x, new_y) and grid_copy[new_x][new_y] == 1:  # 새로운 위치가 1일 때만 이동
            dfs(new_x, new_y)

# 결과 계산
c = []
for k in range(100):  # k를 1부터 100까지 탐색
    count = 0
    grid_copy = make_grid(grid, k)  # grid_copy 생성
    visited = [[False for _ in range(m)] for _ in range(n)]  # 방문 초기화
    
    for i in range(n):
        for j in range(m):
            if grid_copy[i][j] == 1 and not visited[i][j]:  # 안전지대이고 방문 안 했으면
                dfs(i, j)  # DFS 시작
                count += 1  # 안전지대 개수 증가
    c.append(count)            

print(max(c), c.index(max(c)))