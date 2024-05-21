# Given the root of a binary tree, return the sum of all left leaves.

# A leaf is a node with no children. A left leaf is a leaf that is the left child of another node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 24
# Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
# Example 2:

# Input: root = [1]
# Output: 0
 

# Constraints:

# The number of nodes in the tree is in the range [1, 1000].
# -1000 <= Node.val <= 1000


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def isLeaf(node):
            return node and not node.left and not node.right
        
        def traverse(node):
            if not node:
                return 0
            
            left_sum = traverse(node.left) if node.left else 0
            right_sum = traverse(node.right) if node.right else 0
            
            if isLeaf(node.left):
                return node.left.val + left_sum + right_sum
            else:
                return left_sum + right_sum
        
        return traverse(root)