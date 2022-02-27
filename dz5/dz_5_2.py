class Solution(object):
    def isSymmetric(self, root):

        def helper(l_side, r_side):
            if not l_side and not r_side:
                return True
            if not l_side or not r_side:
                return False
            if l_side.val != r_side.val:
                return False
            l = helper(l_side.left, r_side.right)
            r = helper(l_side.right, r_side.left)

            return l and r

        return helper(root.left, root.right)
