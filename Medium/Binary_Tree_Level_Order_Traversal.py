#Binary Tree Level Order Traversal

#Given the root of a binary tree, return the level order traversal of its nodes' values.
#   (i.e., from left to right, level by level).

#Constraints:
#   The number of nodes in the tree is in the range [0, 2000].
#   -1000 <= Node.val <= 1000

import TreeNode

def levelOrder(root):
    def helper(r, l):
        if r is not None:
            if len(ret) == l:
                ret.append([])
            ret[l].append(r.val)
            helper(r.left, l+1)
            helper(r.right, l+1)
    ret = []
    helper(root, 0)
    return ret

def main():
    testcases = [
        [3,9,20,None,None,15,7],
        [1],
        []
    ]
    for i in testcases:
        tree = TreeNode.to_binary_tree(i)
        print(f'root = {i}\noutput = {levelOrder(tree)}\n')

main()