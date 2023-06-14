#Serialize and Deserialize Binary Tree

#Serialization is the process of converting a data structure or object into a sequence of bits so that it can be
#   stored in a file or memory buffer, or transmitted across a network connection link to be reconstructed later
#   in the same or another computer environment.
#Design an algorithm to serialize and deserialize a binary tree.
#There is no restriction on how your serialization/deserialization algorithm should work.
#You just need to ensure that a binary tree can be serialized to a string and this string can be deserialized to
#   the original tree structure.

#Clarification:
#   The input/output format is the same as how LeetCode serializes a binary tree.
#   You do not necessarily need to follow this format, so please be creative and come up with different
#       approaches yourself.

#Constraints
#   The number of nodes in the tree is in the range [0, 104].
#   -1000 <= Node.val <= 1000

import TreeNode as tn
class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """

        def ser_helper(root, s):
            if root is None:
                s += 'None,'
            else:
                s += str(root.val) + ','
                s = ser_helper(root.left, s)
                s = ser_helper(root.right, s)
            return s

        return ser_helper(root, '')

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        def des_helper(l):
            if l[0] == 'None':
                l.pop(0)
                return None
            root = tn.TreeNode(val=l[0])
            l.pop(0)
            root.left = des_helper(l)
            root.right = des_helper(l)
            return root

        data_list = data.split(',')
        root = des_helper(data_list)
        return root

def main():
    testcases = [
        [1,2,3,None,None,4,5],
        []
    ]
    for i in testcases:
        ser = Codec()
        deser = Codec()
        x = tn.to_binary_tree(i)
        s = ser.serialize(x)
        d = deser.deserialize(s)
        print(f'x: {x}\ns: {s}\nd: {d}')
        #ans = deser.deserialize(ser.serialize(tn.to_binary_tree(i)))
        #print(f'root = {i}\noutput = {ans}\n')


main()

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))