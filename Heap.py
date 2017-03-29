# Heap2.py
import random
from binarytree import tree, convert, pprint


class MinHeap(object):
    def __init__(self):
        self.data = []

    def _swap_nodes(self, node_a_index, node_b_index):
        self.data[node_a_index], self.data[node_b_index] = self.data[node_b_index], self.data[node_a_index]

    def _push_down(self, element_index):
        # shift for off-by-one
        element_index = element_index
        left_index = (element_index+1) * 2 -1
        right_index = (element_index+1) * 2
        # print('input={} adj={} left={} right={} len={}'
            # .format(element_index-1, element_index, left_index, right_index, len(self.data)))
        if left_index >= len(self.data):
            # print('no child node, tree is sorted')
            return
        elif right_index >= len(self.data):
            # print('no right node, just compare against left')
            if self.data[element_index] > self.data[left_index]:
                self._swap_nodes(element_index, left_index)
                self._push_down(left_index)
        elif self.data[left_index] == self.data[right_index]:
            self._swap_nodes(element_index, left_index)
            self._push_down(left_index)
        else:
            # print('swap with lower of two nodes and recurse')
            if self.data[element_index] > self.data[left_index] < self.data[right_index]:
                self._swap_nodes(element_index, left_index)
                self._push_down(left_index)
            elif self.data[element_index] > self.data[right_index] < self.data[left_index]:
                self._swap_nodes(element_index, right_index)
                self._push_down(right_index)
            else:
                # print('checked left and right, values sorted')
                return


    def _bubble_up(self, element_index):
        # round down to nearest int
        head_index = int((element_index-1)/2)
        # print('_bubble_up head_index={} element_index={}'.format(head_index, element_index))
        if element_index != 0:
            if self.data[head_index] > self.data[element_index]:
                self.data[head_index], self.data[element_index] = self.data[element_index], self.data[head_index]
                self._bubble_up(head_index)

    def pop(self):
        return_value = self.data[0]
        # swap first and last nodes
        # print(self.data[0], self.data[len(self.data)-1])
        self.data[0], self.data[len(self.data)-1] = self.data[len(self.data)-1], self.data[0]
        # print(self.data[0], self.data[len(self.data)-1])
        # remove last node
        del self.data[len(self.data)-1]
        # push down first node
        self._push_down(0)
        return return_value

    def add_element(self, element):
        self.data.append(element)
        self._bubble_up(len(self.data)-1)


m = MinHeap()
m.data = [12, 15, 24, 24, 26, 64, 106, 62, 84, 118, 72, 174, 308, 299, 305, 193, 309, 223, 122, 171, 278, 225, 255, 456, 390, 332, 464, 479, 479, 375, 448, 454, 482, 436, 358, 230, 404, 171, 375, 438, 336, 301, 381, 349, 311]
# l = [4,50,55,90,87,7,3,6,12,33]
# for i in l:
#     m.add_element(i)
#
#
my_tree = convert(m.data)
pprint(my_tree)
# print(m.data)

while m.data:
    print('remove lowest element={}'.format(m.pop()))
    # my_tree = convert(m.data)
    # pprint(my_tree)

# for i in range(10):
#     print(m._push_down(i))
