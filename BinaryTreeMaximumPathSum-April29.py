def maxPathSum(root):
    def maxPath(root):
        if not root:
            return 0
        left, right = maxPath(root.left), maxPath(root.right)
        value = max(root.val, root.val+max(left,right))
        self.res = max(value, value, root.val+left+right)  
        return value
    
    self.res = None
    maxPath(root)
    return self.res