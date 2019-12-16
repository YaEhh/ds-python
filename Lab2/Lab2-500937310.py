class MyTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0
        self.descendents = 0

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getData(self):
        return self.data

    def insert(self, data):
        queue = [self]

        while len(queue) > 0:
            insertion_node = queue.pop(0)
            if insertion_node.left is None:
                new_node = self.__class__(data)
                insertion_node.left = new_node
                return self
            else:
                queue.append(insertion_node.left)

            if insertion_node.right is None:
                new_node = self.__class__(data)
                insertion_node.right = new_node
                return self
            else:
                queue.append(insertion_node.right)

    def getHeight(self):
        if not self.left and not self.right:
            return 0

        left_height = 0
        right_height = 0

        if self.left:
            left_height = self.left.getHeight()

        if self.right:
            right_height = self.right.getHeight()

        return 1 + max(left_height, right_height)

    def getLevelOrderTraversalArr(self):
        queue = [self]
        return_list = []

        while len(queue) != 0:
            current_node = queue.pop(0)

            return_list.append(current_node)
            # print(current_node.data)

            if current_node.left is not None:
                queue.append(current_node.left)

            if current_node.right is not None:
                queue.append(current_node.right)

        return return_list


class MyBST(MyTree):
    def __init__(self, data):
        super().__init__(data)

    def insert(self, data):
        new_node = MyBST(data)

        x = self
        y = None

        while x is not None:
            y = x
            if data < x.data:
                x = x.left
            else:
                x = x.right

        if y is None:
            y = new_node
        elif data < y.data:
            y.left = new_node
        else:
            y.right = new_node

        return self

    def __contains__(self, data):
        if self is None or self.data == data:
            return True

        if data < self.data:
            if self.left is not None:
                return self.left.__contains__(data)
        else:
            if self.right is not None:
                return self.right.__contains__(data)

        return False


class MyAVL(MyBST):
    def __init__(self, data, parent=None):
        super().__init__(data)

    def getBalanceFactor(self):
        if self.left:
            left_subtree_height = self.left.getHeight()
        else:
            left_subtree_height = -1

        if self.right:
            right_subtree_height = self.right.getHeight()
        else:
            right_subtree_height = -1

        return left_subtree_height - right_subtree_height

    def insert(self, data):

        if data < self.data:
            if self.left:
                self.left = self.left.insert(data)
            else:
                self.left = self.__class__(data)
        elif data > self.data:
            if self.right:
                self.right = self.right.insert(data)
            else:
                self.right = self.__class__(data)
        else:
            return self

        node_balance = self.getBalanceFactor()

        # LL
        if node_balance > 1 and data < self.left.data:
            return self.rightRotate()

        # RR
        if node_balance < -1 and data > self.right.data:
            return self.leftRotate()

        # LR
        if node_balance > 1 and data > self.left.data:
            self.left = self.left.leftRotate()
            return self.rightRotate()

        # RL
        if node_balance < -1 and data < self.right.data:
            self.right = self.right.rightRotate()
            return self.leftRotate()

        return self

    def leftRotate(self):
        new_root = self.right
        sub_tree = new_root.left

        self.right = sub_tree
        new_root.left = self

        return new_root

    def rightRotate(self):
        new_root = self.left
        sub_tree = new_root.right

        self.left = sub_tree
        new_root.right = self

        return new_root
