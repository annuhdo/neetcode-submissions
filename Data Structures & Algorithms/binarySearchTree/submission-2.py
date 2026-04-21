class TreeNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.left = None
        self.right = None

class TreeMap:
    
    def __init__(self):
        self.root = None


    def insert(self, key: int, val: int) -> None:
        # newNode = TreeNode(key, val)
        # if self.root == None:
        #     self.root = newNode
        #     return

        # current = self.root
        # while True:
        #     if key < current.key:
        #         if current.left == None:
        #             current.left = newNode
        #             return
        #         current = current.left
        #     elif key > current.key:
        #         if current.right == None:
        #             current.right = newNode
        #             return
        #         current = current.right
        #     else:
        #         # We definitely have a node here because we've been adding newNode left or right depending on whether key < curr.key and if left is None
        #         current.val = val 
        #         return

        self.root = self.insertHelper(self.root, key, val)

    def insertHelper(self, node: TreeNode, key: int, val: int) -> TreeNode:
        if not node:
            return TreeNode(key, val)

        if key < node.key:
            node.left = self.insertHelper(node.left, key, val)
        elif key > node.key:
            node.right = self.insertHelper(node.right, key, val)
        else:
            node.val = val
        return node


    def get(self, key: int) -> int:
        cur = self.root
        while cur is not None:
            if key < cur.key:
                cur = cur.left
            elif key > cur.key:
                cur = cur.right
            else:
                return cur.val

        return -1

    def findMin(self, node: TreeNode) -> TreeNode:
        while node and node.left:
            node = node.left
        return node


    def getMin(self) -> int:
        cur = self.root
        while cur and cur.left is not None:
            cur = cur.left

        return cur.val if cur is not None else -1


    def getMax(self) -> int:
        cur = self.root
        while cur and cur.right is not None:
            cur = cur.right

        return cur.val if cur is not None else -1


    def remove(self, key: int) -> None:
        self.root = self.removeHelper(self.root, key)

    # Remove the node with key 
    # Return new root after removal
    def removeHelper(self, node: TreeNode, key: int) -> TreeNode:    
        if node is None:
            return None

        if key > node.key:
            # Imagine we delete the right leaf then the right child should be None
            node.right = self.removeHelper(node.right, key)
        elif key < node.key:
            node.left = self.removeHelper(node.left, key)
        else:
            # We want to delete the current node
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                # Left and right children exist
                # Swap current node with in-order successor which is smallest node in right subtree!!
                minNode = self.findMin(node.right)
                node.key = minNode.key
                node.val = minNode.val
                node.right = self.removeHelper(node.right, minNode.key)

        return node

    def getInorderKeys(self) -> List[int]:
        result = []
        self.inorderTraversal(self.root, result)
        return result

    def inorderTraversal(self, node: TreeNode, result: List[int]):
        if not node:
            return

        self.inorderTraversal(node.left, result)
        result.append(node.key)
        self.inorderTraversal(node.right, result)
