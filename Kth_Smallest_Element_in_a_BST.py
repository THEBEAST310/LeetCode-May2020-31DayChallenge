# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def recursive(curr,list1)->list:
    if curr==None:
        return list1
    else:
        list1.append(curr.val)
        list1=recursive(curr.left,list1)
        list1=recursive(curr.right,list1)
        return list1
        
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        list1=[]
        list1=recursive(root,list1)
        list1.sort()
        return(list1[k-1])
    

            
