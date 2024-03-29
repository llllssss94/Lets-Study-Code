from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bfs(root1, root2):
    ret = True

    if root1 is None:
        if root2 is None:
            return True
        else:
            return False
    elif root2 is None:
        return False
    
    if root1.val != root2.val:
        return False
    print(root1.val, root2.val)

    ret &= bfs(root1.left, root2.left)
    print("right - ", ret)

    ret &= bfs(root1.right, root2.right)
    print("left - ", ret)
    
    return ret
    

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return bfs(p, q)