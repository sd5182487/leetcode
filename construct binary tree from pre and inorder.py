__author__ = 'Administrator'
class Solution:
# @param {integer[]} preorder
# @param {integer[]} inorder
# @return {TreeNode}
    def buildTree(self, preorder, inorder):
        if not preorder:
            return None

        m = {}
        for i in range(0, len(inorder)):
            m[inorder[i]] = i
        return self.construct_bst_help(preorder, 0, len(preorder), m, [0])


    def construct_bst_help(self, preorder, start, end, m, curr):
        if start == end:
            return None
        if start == end - 1:
            node = TreeNode(preorder[curr[0]])
            curr[0] += 1
            return node

        node = TreeNode(preorder[curr[0]])
        curr[0] += 1

        i = m[node.val]
        node.left = self.construct_bst_help(preorder, start, i, m, curr)
        node.right = self.construct_bst_help(preorder, i + 1, end, m, curr)
        return node

    def buildTree2(self, preorder, inorder):
        lookup = {}
        for i, num in enumerate(inorder):
            lookup[num] = i
        return self.buildTreeRecu(lookup, preorder, inorder, 0, 0, len(inorder))

    def buildTreeRecu(self, lookup, preorder, inorder, pre_start, in_start, in_end):
        if in_start == in_end:
            return None
        node = TreeNode(preorder[pre_start])
        i = lookup[preorder[pre_start]]
        node.left = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1, in_start, i)
        node.right = self.buildTreeRecu(lookup, preorder, inorder, pre_start + 1 + i - in_start, i + 1, in_end)
        return node