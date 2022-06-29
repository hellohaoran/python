# 作者: 张浩然
# 2022年06月11日22时53分33秒
class node:
    def __init__(self,elem): # 节点类
        self.elem = elem
        self.lchild = None
        self.rchild = None
class Tree: #树类包括建树，前序遍历树，中序遍历树，后序遍历树等方法
    def __init__(self):
        self.root = None
        self.queue = []
    def build_tree(self,elem):
        new_node = node(elem)
        queue_ =self.queue
        queue_.append(new_node)
        if  self.root is None:
            self.root = queue_[0]
        else:
            if queue_[0].lchild is None:
                queue_[0].lchild = new_node
            elif queue_[0].rchild is None:

                queue_[0].rchild = new_node
                queue_.pop(0)
    def preorder(self,node):
        if node:
            print(node.elem,end="")
            self.preorder(node.lchild)
            self.preorder(node.rchild)
    def midorder(self,node):
        if node:
            self.midorder(node.lchild)
            print(node.elem,end = '')
            self.midorder(node.rchild)
    def postorder(self,node):
        if node:
            self.postorder(node.lchild)
            self.postorder(node.rchild)
            print(node.elem,end= '')

if __name__ == '__main__':
    tree = Tree()
    for i in "abcdefghij":
        tree.build_tree(i)
    tree.preorder(tree.root)


