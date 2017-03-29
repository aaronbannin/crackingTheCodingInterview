import random
from binarytree import tree, convert, pprint
# from BinarySearchAVL import insert_node, find_node, left_rotate
from BinarySearchAVL import AVLTree


# l = [63, 58, 50, 84, 64, 92, 66, 89, 98, 91, 79, 77, 26, 31, 16]
l = [63, 58, 50, 84, 64]
# l = []
# for i in range(15):
#     l.append(random.randint(1,100))

# head = None
# # print(l)
# for i in l:
#     # print('test head={}'.format(head))
#     head = insert_node(i, head)

avl = AVLTree()
for i in l:
    print('begin insert={}'.format(i))
    avl.insert(i)
    print(avl.head)


# print('head audit={}'.format(head.__dict__))
def in_order(node):
    if node != None:
        in_order(node.left)
        # print(node.value, end=' ')
        print('(value={} height={} parent={} diff={})'
                .format(node.value, node.height, node.parent.__repr__, avl.height_difference(node)))
        in_order(node.right)

in_order(avl.head)
print()


pprint(avl.head)

# n = avl.find_node(58)
# print('finding node 58')
# print(n)
#
# avl.test_rotations(n)
#
# print(avl.head)


# print(max(head.left.value, head.value))
# print(max(head, head.left, key=lambda x: x.value).value)





# class Node(object):
#     def __init__(self, value):
#         self.value = value
#         self.left = None
#         self.right = None
#
# head = Node(7)
# tail = Node(8)
