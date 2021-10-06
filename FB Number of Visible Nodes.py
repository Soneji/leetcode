'''
https://gist.github.com/kuntalchandra/417f8ddace0ef8ac934b29fc52a392ab
'''

def visible_nodes(root):
  # Write your code here
  if root == None:
    return 0
  
  left = visible_nodes(root.left)
  right = visible_nodes(root.right)
  
  return max(left, right) + 1
