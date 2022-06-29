# 作者: 张浩然
# 2022年06月14日21时16分08秒
RED = 0
BLACK = 1


class RedBlackTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.p = None
        self.color = RED


def left_rotate(tree, node: RedBlackTreeNode):
    if node.right is None: # 如果右孩子直接为空，则不用左旋
        return False

    node_right = node.right
    node_right.p = node.p
    if node.p is None:
        tree.root = node
    if node == node.p.left:
        node.p.left=node_right# 对node的父节点进行相连
    else:
        node.p.right = node_right
    if node_right.left :
        node.right=node_right.left
        node_right.left.p =node
    node.p=node_right
    node_right.left=node
def right_rotate(tree,node:RedBlackTreeNode):
    if node.right: # 节点右子树不存在则返回false
        return False
    node_left = node.left
    node_left.p=node.p
    if node.p == None: # 如果父节点为空
        tree.root = node
    else:
        if node.p.left == node: # 节点在父节点的
            node.p.left=node_left
        else:
            node.p.right = node_left
    if node_left.right:
        node_left.right.p=node
        node.left=node_left.right
    node.p=node_left
    node_left.right= node
class RedBlackTree:
    def __init__(self):
        self.root:RedBlackTree=None
    def insert(self,node:RedBlackTreeNode):
        if not self.root:
            self.root=node
        else:
            current_node= self.root
            while node:
                parent = current_node
                if node.value<current_node.value:
                    current_node=current_node.left
                elif node.value>current_node.value:
                    current_node=current_node.right
        node.p=parent
        if parent.value > node.value:
            parent.left=node
        elif parent.value < node.value:
            parent.right = node







