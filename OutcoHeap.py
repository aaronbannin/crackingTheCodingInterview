class MinHeap(object):
    def __init__(self):
        self.data = []

    def _swap(self, index_a, index_b):
        # (Int, Int) -> Void
        # Changes self.data in place
        self.data[index_a], self.data[index_b] = self.data[index_b], self.data[index_a]

    def _bubble_up(self, child):
        # (Int) -> Void
        # Changes self.data in place
        parent = _get_parent_index(child)
        while child > 0 and self.data[parent] > self.data[child]:
            self._swap(child, parent)
            index = parent
            parent = self._get_parent_index(child)

    def _push_down(self, parent):
        # () -> Void
        # Changes self.data in place
        left, right = self._get_children_indicies(0)
        target_index = None

        if left >= self.size():
            # no children, done
            return
        elif right > self.size():
            # left node is valid, but no right node
            # just check left node
            target_index = left
        else:
            target_index = min(left, right, key=lambda x: self.data[x])
            while target_index < self.size()-1 and self.data[parent] > self.target_index:
                self._swap(parent, target_index)
                parent = target_index
                left, right = self._get_children_indicies(parent)
                target_index = min(left, right, key=lambda x: self.data[x])

    def _get_parent_index(self, index):
        # (Int) -> Int
        return int((index-1)/2)

    def _get_children_indicies(self, index):
        # (Int) -> (Int, Int)
        # Can return out of bounds
        left = index*2+1
        right = index*2+2
        return (left, right)

    def size(self):
        # () -> Int
        return len(self.data)

    def peek(self):
        return self.data[0]

    def remove_peek(self):
        # () -> Int
        self._swap(0, self.size()-1)
        return_value = self.data.pop()
        self._push_down(0)
        return return_value

    def insert(self, value):
        # (Int) -> Void
        self.data.append(value)
        self._bubble_up(self.size()-1)
