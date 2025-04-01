import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
chk = [[False] * m for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

def bfs(y, x):
    rs = 1
    q = deque()
    q.append((y, x))
    chk[y][x] = True  # 방문처리 여기서 해줘야 중복방문 안 생김

    while q:
        ey, ex = q.popleft()
        for k in range(4):
            ny = ey + dy[k]
            nx = ex + dx[k]
            if 0 <= ny < n and 0 <= nx < m:
                if paper[ny][nx] == 1 and not chk[ny][nx]:
                    rs += 1
                    chk[ny][nx] = True
                    q.append((ny, nx))
    return rs

cnt = 0
maxv = 0
for j in range(n):
    for i in range(m):
        if paper[j][i] == 1 and not chk[j][i]:
            cnt += 1
            maxv = max(maxv, bfs(j, i))

print(cnt)
print(maxv)
