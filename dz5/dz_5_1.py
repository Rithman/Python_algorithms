class Solution(object):
    def postorderTraversal(self, root):
        res = []

        def helper(root):
            if root:
                helper(root.left)
                helper(root.right)
                res.append(root.val)

        helper(root)
        return res
