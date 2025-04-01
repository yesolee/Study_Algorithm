# 아이디어
# 최소의 칸 수 => (0,0)시작점 → (n-1,m-1)도착점
# 상하좌우로만 이동 가능
# 0: 갈 수 없는 벽
# 1: 갈 수 있는 길

# 시간복잡도
# BFS : O(V+E)
# O(V) : 100*100
# O(E) : 100*100*4
# O(V+E) : 5*100*100 <5천만 (1초) ok

# 자료구조
# graph int [][]
# chk bool[][]
# queue


from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
graph = [list(map(int, list(input().strip()))) for _ in range(n)]
chk = [[0]*m for _ in range(n)] # 방문여부+거리 동시에 저장

# 상하좌우
dy = [0,1,0,-1]
dx = [1,0,-1,0]

def bfs():
    q = deque()
    q.append((0,0))
    chk[0][0] = 1 # 시작점 거리 1로 시작    
    
    
    while q:
        ey,ex = q.popleft()
        for k in range(4):
            ny = ey+dy[k]
            nx = ex+dx[k]
            if 0<=ny<n and 0<=nx<m:
                if graph[ny][nx] == 1 and chk[ny][nx]==False:
                    chk[ny][nx] = chk[ey][ex]+1
                    q.append((ny,nx))
    return chk[n-1][m-1]                 

print(bfs())