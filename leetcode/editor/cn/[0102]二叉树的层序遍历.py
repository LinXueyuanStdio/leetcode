# 给你一个二叉树，请你返回其按 层序遍历 得到的节点值。 （即逐层地，从左到右访问所有节点）。 
# 
#  
# 
#  示例： 
# 二叉树：[3,9,20,null,null,15,7], 
# 
#  
#     3
#    / \
#   9  20
#     /  \
#    15   7
#  
# 
#  返回其层序遍历结果： 
# 
#  
# [
#   [3],
#   [9,20],
#   [15,7]
# ]
#  
#  Related Topics 树 广度优先搜索 二叉树 
#  👍 960 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ans = []
        if root is None:
            return ans
        level = [root]
        next_level = []
        while len(level) > 0:
            level_val = []
            for i in level:
                if i is None:
                    continue
                level_val.append(i.val)
                if i.left is not None:
                    next_level.append(i.left)
                if i.right is not None:
                    next_level.append(i.right)
            if len(level_val) > 0:
                ans.append(level_val)
            level = next_level
            next_level = []
        return ans
# leetcode submit region end(Prohibit modification and deletion)
