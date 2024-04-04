from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        def dfs(node, depth):
            # Edge case #1: 빈 경우
            if node is None:
                return depth - 1
            # Edge case #2: Node는 있는데 값이 없는 경우
            if node.val is None:
                return depth - 1
            
            # Escape Condition: Left 노드 일때
            if node.left is None and node.right is None:
                return depth
            
            # 변수 겹치지 않도록 나누고
            l_d = r_d = depth
            # dfs
            if node.left is not None:
                l_d = max(depth, dfs(node.left, depth+1))
            if node.right is not None:
                r_d = max(depth, dfs(node.right, depth+1))

            # 왼쪽, 오른쪽 중 child 가 있는 쪽에서 max가 나온다.
            return max(l_d, r_d)
        
        return dfs(root, 1)