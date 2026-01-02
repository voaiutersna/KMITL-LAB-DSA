class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
class BinaryTree:
    def __init__(self):
        self.root = None
    def insert(self, data):
        """แทรกข้อมูลแบบ Binary Search Tree"""
        # TODO: ถ้า root เป็น None ให้สร้าง root ใหม่
        # TODO: ถ้ามี root แล้ว ให้เรียก _insert_recursive()
        if self.root is None:
            self.root = TreeNode(data)
        else:
            node = self.root
            self._insert_recursive(node, data)


    def _insert_recursive(self, node, data):
        """แทรกข้อมูลแบบ recursive"""
        # TODO: ถ้า data < node.data
        #       - ถ้า left เป็น None → สร้าง node ใหม่ที่ left
        #       - ถ้า left มี node แล้ว → เรียก _insert_recursive(node.left, data)
        # TODO: ถ้า data >= node.data
        #       - ถ้า right เป็น None → สร้าง node ใหม่ที่ right
        #       - ถ้า right มี node แล้ว → เรียก _insert_recursive(node.right, data)
        insert_node = TreeNode(data)
        if data < node.data: #go left
            if node.left is None: #base case
                node.left = insert_node
            elif node.left is not None:
                self._insert_recursive(node.left, data)
        else: #go right
            if node.right is None: #base case
                node.right = insert_node
            elif node.right is not None:
                self._insert_recursive(node.right, data)
    def traverse_inorder(self, node=None, first_call=True):
        """แสดงข้อมูลแบบ Inorder (Left -> Root -> Right)"""
        # TODO: ถ้าเป็นการเรียกครั้งแรก (first_call=True)
        #       - ให้ node = self.root
        #       - ถ้า root is None ให้ print "This is an empty tree." แล้ว return
        
        # TODO: ถ้า node ไม่เป็น None
        #       1. เรียก traverse_inorder(node.left, False) ← ไปซ้ายก่อน
        #       2. print(node.data, end=" ") ← แสดงข้อมูล
        #       3. เรียก traverse_inorder(node.right, False) ← ไปขวา
        pass
def main():
    tree = BinaryTree()
    print("Tree created successfully!")
    # print(f"Root is None: {tree.root is None}")
    tree.insert(50)
    tree.insert(30)
    tree.insert(70)
    tree.insert(20)

    print(f"Root: {tree.root.data}")  # ควรได้ 50
    print(f"Root Left: {tree.root.left.data}")  # ควรได้ 30
    print(f"Root Right: {tree.root.right.data}")  # ควรได้ 70
    print(f"Root Left-Left: {tree.root.left.left.data}")  # ควรได้ 20
main()
