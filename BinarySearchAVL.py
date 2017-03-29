from binarytree import Node

class BNode(Node):
    def __init__(self, value, parent=None):
        super().__init__(value)
        self.parent = parent
        self.height = 0


class AVLTree(object):
    def __init__(self, node=None):
        self.head = node

    def _get_height(self, node):
        if node is None:
            return -1
        else:
            return node.height

    def height_difference(self, node):
        # neg = left heavy, pos = right heavy
        return self._get_height(node.right) - self._get_height(node.left)

    def insert(self, value):
        if self.head is None:
            self.head = BNode(value)
        else:
            current_node = self.head
            while True:
                if value <= current_node.value:
                    if current_node.left is None:
                        current_node.left = BNode(value)
                        current_node.left.parent = current_node
                        self.set_upstream(current_node)
                        return
                    else:
                        current_node = current_node.left
                elif value > current_node.value:
                    if current_node.right is None:
                        current_node.right = BNode(value)
                        current_node.right.parent = current_node
                        self.set_upstream(current_node)
                        return
                    else:
                        current_node = current_node.right
                else:
                    raise ValueError

    def find_node(self, value):
        current_node = self.head
        while current_node is not None:
            if value == current_node.value:
                return current_node
            elif value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                raise ValueError('Cannot find node current_node={}'
                                .format(current_node.__repr__))



    def set_upstream(self, node):
        print('begin set_upstream node={}'.format(node.__repr__))
        if node is None:
            return
        else:
            # set new height
            max_height = max(self._get_height(node.left), self._get_height(node.right))
            node.height = max_height + 1
            #check and remedy balance

            node_diff = self.height_difference(node)
            if node_diff < -1:
                print('leans left, right rotate node={} node_diff={}'
                        .format(node.__repr__), node_diff)
                if self.height_difference(node.left) > 1:
                    print('double rotate, start left left_diff={}'
                            format(self.height_difference(node.left)))
                    self.left_rotate(node.left)
                self.right_rotate(node)
            elif node_diff > 1:
                print('leans right, left rotate')
                if self.height_difference(node.right) < -1:
                    print('double rotate, start right')
                    self.right_rotate(node.right)
                self.left_rotate(node)
            else:
                # nothing to do
                pass

            #
            #
            # if self.height_difference(node) > 0 is self.height_difference(node.parent) > 0:
            #     # inline, rotate based on pos/neg
            #     pass
            # else:
            #     # angled, rotate child than invert the rotate for parent
            #     pass
            # # recurse
            self.set_upstream(node.parent)

    def test_rotations(self, node):
        node_diff = self.height_difference(node)
        if node_diff < -1:
            # leans left, right rotate
            if self.height_difference(node.left) > 1:
                # double rotate, start left
                self.left_rotate(node.left)
            self.right_rotate(node)
        elif node_diff > 1:
            # leans right, left rotate
            if self.height_difference(node.right) < -1:
                # double rotate, start right
                self.right_rotate(node.right)
            self.left_rotate(node)
        else:
            # nothing to do
            pass

    def left_rotate(self, node):
        """
            right becomes head
            head becomes left
        """
        print('left_rotate input={}'.format(node.__repr__))
        if self.head == node:
            self.head = rotated_node
        rotated_node = node.right
        if node.parent is not None:
            node.right.parent = node.parent
            if node.right.value <= node.parent.value:
                node.parent.left = node.right
            elif node.right.value > node.parent.value:
                node.parent.right = node.right
            else:
                raise ValueError('Cannot detemine if child should be right or left')

        node.right.left = node
        node.right = None
        return rotated_node


    def right_rotate(self, node):
        """
            left becomes head
            head becomes right
        """

        rotated_node = node.left
        if self.head == node:
            self.head = rotated_node
        print('begin right_rotate rotated_node={}'.format(rotated_node.__repr__))
        if node.parent is not None:
            node.left.parent = node.parent
            if node.left.value >= node.parent.value:
                node.parent.right = node.left
            elif node.left.value < node.parent.value:
                node.parent.left = node.left
            else:
                raise ValueError('Cannot detemine if child should be right or left')

        node.left.right = node
        node.left = None
        return rotated_node

    def double_rotate_node(self, node):
        pass
