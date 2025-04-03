import sys
input = sys.stdin.readline

# 트리 저장용
tree = {}

# 입력
n = int(input())
for _ in range(n):
    root, left, right = input().split()
    tree[root] = [left, right]

# 전위 순회: 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    if node == '.':
        return
    print(node, end='')           # 현재 노드
    preorder(tree[node][0])       # 왼쪽
    preorder(tree[node][1])       # 오른쪽

# 중위 순회: 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])        # 왼쪽
    print(node, end='')           # 현재 노드
    inorder(tree[node][1])        # 오른쪽

# 후위 순회: 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])      # 왼쪽
    postorder(tree[node][1])      # 오른쪽
    print(node, end='')           # 현재 노드

# A가 항상 루트
preorder('A')
print()
inorder('A')
print()
postorder('A')