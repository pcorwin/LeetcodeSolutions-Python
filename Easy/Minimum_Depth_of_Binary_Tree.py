# Minimum Depth of Binary Tree

# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

# Constraints:
#   The number of nodes in the tree is in the range [0, 105].
#   -1000 <= Node.val <= 1000

import TreeNode


def minDepth(root):
    if not root:
        return 0
    childs = [root.left, root.right]
    if not any(childs):
        return 1
    min_depth = float('inf')
    for c in childs:
        if c:
            min_depth = min(minDepth(c), min_depth)

    return min_depth + 1


def main():
    testcases = [
        [3, 9, 20, None, None, 15, 7],
        [2, None, 3, None, 4, None, 5, None, 6]
    ]
    for i in testcases:
        tree = TreeNode.to_binary_tree(i)
        print(f'root = {i}\noutput = {minDepth(tree)}\n')


main()
